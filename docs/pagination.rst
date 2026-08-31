Pagination
==========

Many Mattermost endpoints return results one page at a time, using ``page``
and ``per_page`` query parameters. ``driver.paginate()`` wraps any such
endpoint method and lazily iterates over the items of every page — the next
page is only requested when iteration reaches it.

.. code:: python

    for user in driver.paginate(driver.users.get_users, in_team=team_id):
        print(user["username"])

The same method exists on ``AsyncTypedDriver``, returning an async iterator:

.. code:: python

    async for user in driver.paginate(driver.users.get_users, in_team=team_id):
        print(user["username"])

All endpoint parameters — including path parameters such as ``channel_id``
— are passed as keyword arguments and forwarded to the endpoint method.
Positional arguments raise ``TypeError`` before any request is made, as
they could bind to ``page``/``per_page`` or the wrong query parameter.
``per_page`` defaults to 200. Iteration stops when a page returns fewer
items than ``per_page``. Values above 200 — the most the Mattermost server
serves per page — are silently capped by the server, so with a larger
``per_page`` a short page is not conclusive and iteration only stops on an
empty or shrinking page. ``start_page=`` may be passed to start at a later
page, and ``max_pages=`` caps the number of requests. ``page=`` itself is
never passed through and raises ``TypeError`` — call the method directly
to fetch a single page.

Wrapped responses
-----------------

Some endpoints do not return a plain list but wrap the items in an object,
for example ``threads.get_user_threads`` returns
``{"threads": [...], "total": ...}``. Use ``items_from=`` to say where the items
are — either a response key or a callable receiving the response and
returning the list:

.. code:: python

    for thread in driver.paginate(
        driver.threads.get_user_threads, user_id=user_id, team_id=team_id, items_from="threads"
    ):
        print(thread["id"])

Without ``items_from=``, a non-list response raises ``TypeError``.

Cursor based endpoints
----------------------

A few endpoints paginate with cursors instead of page numbers, such as the
``before``/``after`` post IDs of ``posts.get_posts_for_channel`` or the
keyset parameters of the reporting endpoints. Pass ``next_params=``, a callable
that receives each response and returns the keyword arguments for the next
call — or ``None`` (or an empty dict) to stop. Walking a channel's full post
history:

.. code:: python

    for post in driver.paginate(
        driver.posts.get_posts_for_channel,
        channel_id=channel_id,
        items_from=lambda r: [r["posts"][pid] for pid in r["order"]],
        next_params=lambda r: {"before": r["order"][-1]} if r["order"] and r["prev_post_id"] else None,
    ):
        print(post["message"])

In cursor mode the ``page``/``per_page`` requirement does not apply, and
``next_params`` alone decides when iteration ends: it is consulted even for
pages without items, so an ``items_from=`` callable that filters a whole page
away does not end the iteration early. Each returned dict *replaces* the
previous one rather than merging with it, so cursor keys from earlier
pages never leak into later requests — a ``next_params`` may e.g. switch
from ``after`` to ``before`` mid-walk, and a cursor passed directly to
``paginate()`` (such as a starting ``before=``) is overridden once
``next_params`` takes over. ``per_page`` defaults to 200 when the endpoint
accepts it and is otherwise omitted. ``start_page=`` applies to offset
pagination only and raises ``TypeError`` here — ``next_params`` alone
drives the paging.

Endpoints ignoring page/per_page
--------------------------------

A small number of endpoints accept ``page``/``per_page`` but ignore them in
some configurations, serving the identical full result set for every page.
``paginate()`` detects the repeated page and raises ``RuntimeError`` after the
second request instead of looping forever. This happens in two situations:

- Endpoints that only paginate when an additional flag is set — for example
  ``groups.get_groups_associated_to_channels_by_team`` requires
  ``paginate=True``. Such flags pass through like any other keyword argument.
- Parameters that disable pagination server side — for example a non-zero
  ``since=`` makes ``posts.get_posts_for_channel`` return all matching posts
  in a single response. Call such methods directly instead of paginating.
  (Other endpoints, such as ``groups.get_groups`` and
  ``threads.get_user_threads``, treat ``since=`` as a plain filter and
  paginate normally.)

With the required flag, the flagged endpoints paginate like any other:

.. code:: python

    for channel_id, groups in driver.paginate(
        driver.groups.get_groups_associated_to_channels_by_team,
        team_id=team_id,
        paginate=True,
        items_from=lambda r: list(r["groups"].items()),
    ):
        ...

Unsupported methods
-------------------

Passing a method that accepts neither ``page``/``per_page`` nor ``next_params=``
raises ``TypeError`` immediately, before any request is made. Such endpoints
are not paginated — call them directly.
