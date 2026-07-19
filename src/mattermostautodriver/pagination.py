"""
Helpers to lazily iterate over all items of paginated API endpoints.

These implement :meth:`TypedDriver.paginate <mattermostautodriver.driver.driver.TypedDriver.paginate>`
and :meth:`AsyncTypedDriver.paginate <mattermostautodriver.driver.driver.AsyncTypedDriver.paginate>`,
which are the documented entry points.
"""

import inspect

import httpx

from .constants import MAX_PER_PAGE


def paginate(method, *args, per_page=None, items=None, next_args=None, max_pages=None, **kwargs):
    """Lazily yield every item of a paginated endpoint method.

    See :meth:`TypedDriver.paginate <mattermostautodriver.driver.driver.TypedDriver.paginate>`
    for parameter documentation.
    """
    _validate(method, args, kwargs, items, next_args)

    if next_args is not None:
        per_page = _cursor_per_page(method, per_page)
        if per_page is not None:
            kwargs["per_page"] = per_page
        return _paginate_cursor(method, kwargs, items, next_args, max_pages)

    return _paginate_offset(method, kwargs, items, per_page, max_pages)


def apaginate(method, *args, per_page=None, items=None, next_args=None, max_pages=None, **kwargs):
    """Asynchronous variant of :func:`paginate` returning an async iterator."""
    _validate(method, args, kwargs, items, next_args)

    if next_args is not None:
        per_page = _cursor_per_page(method, per_page)
        if per_page is not None:
            kwargs["per_page"] = per_page
        return _apaginate_cursor(method, kwargs, items, next_args, max_pages)

    return _apaginate_offset(method, kwargs, items, per_page, max_pages)


def _paginate_offset(method, kwargs, items, per_page, max_pages):
    page, per_page = _offset_start(kwargs, per_page)
    pages_fetched = 0
    largest_batch = 0

    while max_pages is None or pages_fetched < max_pages:
        batch = _extract_items(method(page=page, per_page=per_page, **kwargs), items)
        pages_fetched += 1

        yield from batch

        # Up to the server's cap the requested per_page is honored, so a short
        # page is the last one. Above the cap a short page is not conclusive
        # and only an empty or shrinking page ends the iteration.
        limit = per_page if per_page <= MAX_PER_PAGE else largest_batch
        if not batch or len(batch) < limit:
            return

        largest_batch = max(largest_batch, len(batch))
        page += 1


async def _apaginate_offset(method, kwargs, items, per_page, max_pages):
    page, per_page = _offset_start(kwargs, per_page)
    pages_fetched = 0
    largest_batch = 0

    while max_pages is None or pages_fetched < max_pages:
        batch = _extract_items(await method(page=page, per_page=per_page, **kwargs), items)
        pages_fetched += 1

        for item in batch:
            yield item

        # Up to the server's cap the requested per_page is honored, so a short
        # page is the last one. Above the cap a short page is not conclusive
        # and only an empty or shrinking page ends the iteration.
        limit = per_page if per_page <= MAX_PER_PAGE else largest_batch
        if not batch or len(batch) < limit:
            return

        largest_batch = max(largest_batch, len(batch))
        page += 1


def _paginate_cursor(method, kwargs, items, next_args, max_pages):
    pages_fetched = 0
    cursor_kwargs = {}

    while max_pages is None or pages_fetched < max_pages:
        response = method(**{**kwargs, **cursor_kwargs})
        batch = _extract_items(response, items)
        pages_fetched += 1

        yield from batch

        # Termination is delegated to next_args: empty pages keep iterating
        # for as long as it keeps returning arguments for the next call
        next_kwargs = next_args(response)
        if not next_kwargs:
            return

        # The returned dict replaces the previous cursor arguments wholesale,
        # so cursor keys from earlier pages never leak into later requests
        cursor_kwargs = next_kwargs


async def _apaginate_cursor(method, kwargs, items, next_args, max_pages):
    pages_fetched = 0
    cursor_kwargs = {}

    while max_pages is None or pages_fetched < max_pages:
        response = await method(**{**kwargs, **cursor_kwargs})
        batch = _extract_items(response, items)
        pages_fetched += 1

        for item in batch:
            yield item

        # Termination is delegated to next_args: empty pages keep iterating
        # for as long as it keeps returning arguments for the next call
        next_kwargs = next_args(response)
        if not next_kwargs:
            return

        # The returned dict replaces the previous cursor arguments wholesale,
        # so cursor keys from earlier pages never leak into later requests
        cursor_kwargs = next_kwargs


def _validate(method, args, kwargs, items, next_args):
    if next_args is None and not _supports_offset_pagination(method):
        name = getattr(method, "__name__", repr(method))
        raise TypeError(
            f"{name}() does not accept 'page'/'per_page' and cannot be offset paginated. "
            "Pass next_args= for cursor based endpoints, or call the method directly."
        )

    if next_args is not None and "page" in kwargs:
        raise TypeError(
            "page= applies to offset pagination only and would be re-sent verbatim on "
            "every request in cursor mode. Drive the paging via next_args instead."
        )

    if args:
        raise TypeError(
            "paginate() passes only keyword arguments to the endpoint method. "
            "Pass path parameters as keywords too, e.g. channel_id=..., so they "
            "cannot bind to page/per_page or the wrong query parameter."
        )

    if items is not None and not (isinstance(items, str) or callable(items)):
        raise TypeError("items= must be a response key (str) or a callable extracting a list from the response")


def _supports_offset_pagination(method):
    try:
        parameters = inspect.signature(method).parameters
    except (TypeError, ValueError):
        # Signature cannot be introspected, assume the caller knows what they are doing
        return True

    if any(parameter.kind is inspect.Parameter.VAR_KEYWORD for parameter in parameters.values()):
        return True

    return "page" in parameters and "per_page" in parameters


def _offset_start(kwargs, per_page):
    page = kwargs.pop("page", None) or 0
    # Default to the largest page size the server serves, not its default of 60
    return page, per_page if per_page is not None else MAX_PER_PAGE


def _cursor_per_page(method, per_page):
    if per_page is not None:
        return per_page

    # Default to the largest page size here as well, but only for methods
    # that are known to accept per_page
    try:
        parameters = inspect.signature(method).parameters
    except (TypeError, ValueError):
        return None

    return MAX_PER_PAGE if "per_page" in parameters else None


def _extract_items(response, items):
    if isinstance(response, httpx.Response):
        content_type = response.headers.get("Content-Type", "unset")
        raise TypeError(
            f"Server returned a non-JSON response (Content-Type {content_type!r}, "
            f"status {response.status_code}) that cannot be paginated."
        )

    if callable(items):
        return list(items(response))

    if isinstance(items, str):
        if not isinstance(response, dict):
            raise TypeError(f"items={items!r} was given but the response is a {type(response).__name__}, not an object")

        if items not in response:
            raise KeyError(f"items={items!r} not found in the response. Available keys: {sorted(response)}")

        value = response[items]

        if value is None:
            # Go servers serialize empty result slices as null
            return []

        if not isinstance(value, list):
            raise TypeError(
                f"items={items!r} refers to a {type(value).__name__}, not a list. "
                "Pass a callable as items= to extract the items instead."
            )

        return value

    if isinstance(response, list):
        return response

    raise TypeError(
        "Response is not a list. Pass items= (a response key or a callable) "
        "to tell paginate where to find the items in the response."
    )
