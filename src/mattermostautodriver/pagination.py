"""
Helpers to lazily iterate over all items of paginated API endpoints.

These implement :meth:`TypedDriver.paginate <mattermostautodriver.driver.driver.TypedDriver.paginate>`
and :meth:`AsyncTypedDriver.paginate <mattermostautodriver.driver.driver.AsyncTypedDriver.paginate>`,
which are the documented entry points.
"""

import inspect

import httpx

from .constants import MAX_PER_PAGE


def paginate(
    method, /, *args, per_page=None, items_from=None, next_params=None, max_pages=None, start_page=0, **kwargs
):
    """Lazily yield every item of a paginated endpoint method.

    See :meth:`TypedDriver.paginate <mattermostautodriver.driver.driver.TypedDriver.paginate>`
    for parameter documentation.
    """
    _validate(method, args, kwargs, items_from, next_params, start_page)
    return _paginate_sync(method, _make_pager(method, kwargs, per_page, next_params, start_page), items_from, max_pages)


def apaginate(
    method, /, *args, per_page=None, items_from=None, next_params=None, max_pages=None, start_page=0, **kwargs
):
    """Asynchronous variant of :func:`paginate` returning an async iterator."""
    _validate(method, args, kwargs, items_from, next_params, start_page)
    return _paginate_async(
        method, _make_pager(method, kwargs, per_page, next_params, start_page), items_from, max_pages
    )


def _paginate_sync(method, pager, items_from, max_pages):
    pages_fetched = 0

    while max_pages is None or pages_fetched < max_pages:
        response = method(**pager.request_kwargs())
        batch = _extract_items(response, items_from)
        pages_fetched += 1

        # Advance before yielding, so a repeated page raises without its duplicate items being delivered
        has_more = pager.advance(response, batch)

        yield from batch

        if not has_more:
            return


async def _paginate_async(method, pager, items_from, max_pages):
    pages_fetched = 0

    while max_pages is None or pages_fetched < max_pages:
        response = await method(**pager.request_kwargs())
        batch = _extract_items(response, items_from)
        pages_fetched += 1

        # Advance before yielding, so a repeated page raises without its duplicate items being delivered
        has_more = pager.advance(response, batch)

        for item in batch:
            yield item

        if not has_more:
            return


def _make_pager(method, kwargs, per_page, next_params, start_page):
    if next_params is not None:
        return _CursorPager(kwargs, _cursor_per_page(method, per_page), next_params)
    return _OffsetPager(method, kwargs, per_page, start_page)


class _OffsetPager:
    """Paging decisions for page/per_page based endpoints."""

    def __init__(self, method, kwargs, per_page, start_page):
        self.method_name = getattr(method, "__name__", repr(method))
        self.kwargs = kwargs
        self.page = start_page
        # Default to the largest page size the server serves, not its default of 60
        self.per_page = per_page if per_page is not None else MAX_PER_PAGE
        self.largest_batch = 0
        self.previous_batch = None

    def request_kwargs(self):
        return {**self.kwargs, "page": self.page, "per_page": self.per_page}

    def advance(self, response, batch):
        """Advance to the next page, or return False when this was the last one.

        Up to the server's cap the requested per_page is honored, so a short
        page is the last one. Above the cap a short page is not conclusive
        and only an empty or shrinking page ends the iteration.

        A page identical to the previous one means the server ignored
        page/per_page — the iteration would repeat it forever, so raise instead.
        """
        if batch == self.previous_batch:
            raise RuntimeError(
                f"{self.method_name}() returned an identical page twice in a row, so the server "
                "appears to be ignoring page/per_page. Some endpoints only paginate when an "
                "additional flag is set (e.g. paginate=True on group endpoints) and some stop "
                "paginating for certain parameters (e.g. since= on posts.get_posts_for_channel). "
                "Call the method directly instead."
            )

        limit = self.per_page if self.per_page <= MAX_PER_PAGE else self.largest_batch
        if not batch or len(batch) < limit:
            return False

        self.previous_batch = batch
        self.largest_batch = max(self.largest_batch, len(batch))
        self.page += 1
        return True


class _CursorPager:
    """Paging decisions for cursor based endpoints, driven by next_params."""

    def __init__(self, kwargs, per_page, next_params):
        self.kwargs = kwargs
        if per_page is not None:
            self.kwargs["per_page"] = per_page
        self.cursor_kwargs = {}
        self.next_params = next_params

    def request_kwargs(self):
        return {**self.kwargs, **self.cursor_kwargs}

    def advance(self, response, batch):
        """Advance to the next cursor, or return False when next_params stops.

        Termination is delegated to next_params: empty pages keep iterating
        for as long as it keeps returning parameters for the next call. The
        returned dict replaces the previous cursor parameters wholesale, so
        cursor keys from earlier pages never leak into later requests.
        """
        next_kwargs = self.next_params(response)
        if not next_kwargs:
            return False

        self.cursor_kwargs = next_kwargs
        return True


def _validate(method, args, kwargs, items_from, next_params, start_page):
    if next_params is None and not _supports_offset_pagination(method):
        name = getattr(method, "__name__", repr(method))
        raise TypeError(
            f"{name}() does not accept 'page'/'per_page' and cannot be offset paginated. "
            "Pass next_params= for cursor based endpoints, or call the method directly."
        )

    if "page" in kwargs:
        raise TypeError(
            "page= is not passed through by paginate(). Call the method directly for a "
            "single page, or pass start_page= to begin iteration at a later page."
        )

    if next_params is not None and start_page:
        raise TypeError("start_page= applies to offset pagination only. Drive the paging via next_params instead.")

    if args:
        raise TypeError(
            "paginate() passes only keyword arguments to the endpoint method. "
            "Pass path parameters as keywords too, e.g. channel_id=..., so they "
            "cannot bind to page/per_page or the wrong query parameter."
        )

    if items_from is not None and not (isinstance(items_from, str) or callable(items_from)):
        raise TypeError("items_from= must be a response key (str) or a callable extracting a list from the response")


def _supports_offset_pagination(method):
    try:
        parameters = inspect.signature(method).parameters
    except (TypeError, ValueError):
        # Signature cannot be introspected, assume the caller knows what they are doing
        return True

    if any(parameter.kind is inspect.Parameter.VAR_KEYWORD for parameter in parameters.values()):
        return True

    return "page" in parameters and "per_page" in parameters


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


def _extract_items(response, items_from):
    if isinstance(response, httpx.Response):
        content_type = response.headers.get("Content-Type", "unset")
        raise TypeError(
            f"Server returned a non-JSON response (Content-Type {content_type!r}, "
            f"status {response.status_code}) that cannot be paginated."
        )

    if callable(items_from):
        return list(items_from(response))

    if isinstance(items_from, str):
        if not isinstance(response, dict):
            raise TypeError(
                f"items_from={items_from!r} was given but the response is a {type(response).__name__}, not an object"
            )

        if items_from not in response:
            raise KeyError(f"items_from={items_from!r} not found in the response. Available keys: {sorted(response)}")

        value = response[items_from]

        if value is None:
            # Go servers serialize empty result slices as null
            return []

        if not isinstance(value, list):
            raise TypeError(
                f"items_from={items_from!r} refers to a {type(value).__name__}, not a list. "
                "Pass a callable as items_from= to extract the items instead."
            )

        return value

    if isinstance(response, list):
        return response

    raise TypeError(
        "Response is not a list. Pass items_from= (a response key or a callable) "
        "to tell paginate where to find the items in the response."
    )
