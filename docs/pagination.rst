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

Positional and keyword arguments are passed through to the endpoint method,
and ``per_page`` defaults to 200. Iteration stops when a page returns fewer
items than ``per_page``. Values above 200 — the most the Mattermost server
serves per page — are silently capped by the server, so with a larger
``per_page`` a short page is not conclusive and iteration only stops on an
empty or shrinking page. ``page=`` may be passed to start at a later page,
and ``max_pages=`` caps the number of requests.

Wrapped responses
-----------------

Some endpoints do not return a plain list but wrap the items in an object,
for example ``threads.get_user_threads`` returns
``{"threads": [...], "total": ...}``. Use ``items=`` to say where the items
are — either a response key or a callable receiving the response and
returning the list:

.. code:: python

    for thread in driver.paginate(
        driver.threads.get_user_threads, user_id, team_id, items="threads"
    ):
        print(thread["id"])

Without ``items=``, a non-list response raises ``TypeError``.

Cursor based endpoints
----------------------

A few endpoints paginate with cursors instead of page numbers, such as the
``before``/``after`` post IDs of ``posts.get_posts_for_channel`` or the
keyset parameters of the reporting endpoints. Pass ``next_args=``, a callable
that receives each response and returns the keyword arguments for the next
call — or ``None`` to stop. Walking a channel's full post history:

.. code:: python

    for post in driver.paginate(
        driver.posts.get_posts_for_channel, channel_id,
        items=lambda r: [r["posts"][pid] for pid in r["order"]],
        next_args=lambda r: {"before": r["order"][-1]} if r["prev_post_id"] else None,
    ):
        print(post["message"])

In cursor mode the ``page``/``per_page`` requirement does not apply;
``per_page`` is only forwarded to the endpoint when explicitly given.
Iteration also stops when a page contains no items.

Unsupported methods
-------------------

Passing a method that accepts neither ``page``/``per_page`` nor ``next_args=``
raises ``TypeError`` immediately, before any request is made. Such endpoints
are not paginated — call them directly.
