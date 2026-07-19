import itertools

import httpx
import pytest

from conftest import make_async_driver, make_driver
from mattermostautodriver.pagination import apaginate, paginate


def make_offset_method(pages):
    """Fake endpoint method serving ``pages[page]`` and recording each call."""
    calls = []

    def method(page=0, per_page=60, **kwargs):
        calls.append({"page": page, "per_page": per_page, **kwargs})
        return pages[page] if page < len(pages) else []

    return method, calls


def test_iterates_across_pages_and_stops_on_short_page():
    method, calls = make_offset_method([[1, 2], [3, 4], [5]])

    assert list(paginate(method, per_page=2)) == [1, 2, 3, 4, 5]
    assert [call["page"] for call in calls] == [0, 1, 2]
    assert all(call["per_page"] == 2 for call in calls)


def test_stops_on_empty_first_page():
    method, calls = make_offset_method([[]])

    assert list(paginate(method, per_page=2)) == []
    assert len(calls) == 1


def test_full_last_page_is_followed_by_one_empty_request():
    method, calls = make_offset_method([[1, 2]])

    assert list(paginate(method, per_page=2)) == [1, 2]
    assert len(calls) == 2


def test_pages_are_fetched_lazily():
    method, calls = make_offset_method([[1, 2], [3, 4], [5]])

    iterator = paginate(method, per_page=2)
    assert calls == []

    assert list(itertools.islice(iterator, 2)) == [1, 2]
    assert len(calls) == 1


def test_extra_arguments_are_passed_through():
    method, calls = make_offset_method([[1]])

    list(paginate(method, per_page=2, in_team="team_id"))
    assert calls[0]["in_team"] == "team_id"


def test_page_argument_sets_the_starting_page():
    method, calls = make_offset_method([[1, 2], [3, 4], [5]])

    assert list(paginate(method, page=2, per_page=2)) == [5]
    assert [call["page"] for call in calls] == [2]


def test_server_capping_per_page_does_not_end_iteration_early():
    # per_page above the server maximum (200) is silently capped by the
    # server, so a page smaller than per_page must not end the iteration
    server_cap = 2
    pages = [[1, 2], [3, 4], [5]]
    calls = []

    def method(page=0, per_page=60):
        calls.append(per_page)
        return pages[page][:server_cap] if page < len(pages) else []

    assert list(paginate(method, per_page=300)) == [1, 2, 3, 4, 5]
    assert calls == [300, 300, 300]


def test_untrusted_per_page_confirms_a_short_first_page_with_an_empty_request():
    method, calls = make_offset_method([[1]])

    assert list(paginate(method, per_page=300)) == [1]
    assert [call["page"] for call in calls] == [0, 1]


def test_max_pages_limits_requests():
    method, calls = make_offset_method([[1, 2], [3, 4], [5, 6], [7, 8]])

    assert list(paginate(method, per_page=2, max_pages=2)) == [1, 2, 3, 4]
    assert len(calls) == 2


def test_items_as_key_unwraps_dict_responses():
    def method(page=0, per_page=60):
        return {"threads": [1, 2] if page == 0 else [3], "total": 3}

    assert list(paginate(method, per_page=2, items="threads")) == [1, 2, 3]


def test_items_as_callable_unwraps_dict_responses():
    def method(page=0, per_page=60):
        return {"order": ["a"], "posts": {"a": {"id": "a"}}} if page == 0 else {"order": [], "posts": {}}

    result = list(paginate(method, per_page=2, items=lambda r: [r["posts"][pid] for pid in r["order"]]))
    assert result == [{"id": "a"}]


def test_dict_response_without_items_raises():
    def method(page=0, per_page=60):
        return {"threads": []}

    with pytest.raises(TypeError, match="items="):
        list(paginate(method))


def test_items_key_with_null_value_is_treated_as_an_empty_page():
    def method(page=0, per_page=60):
        # Go servers serialize empty result slices as null
        return {"threads": None, "total": 0}

    assert list(paginate(method, items="threads")) == []


def test_items_key_missing_from_response_names_the_available_keys():
    def method(page=0, per_page=60):
        return {"threads": [], "total": 0}

    with pytest.raises(KeyError, match="'thread'.*Available keys.*threads"):
        list(paginate(method, items="thread"))


def test_items_key_pointing_at_a_non_list_raises():
    def method(page=0, per_page=60):
        return {"order": ["a"], "posts": {"a": {"id": "a"}}}

    with pytest.raises(TypeError, match="'posts' refers to a dict"):
        list(paginate(method, items="posts"))


def test_items_key_with_a_list_response_raises():
    def method(page=0, per_page=60):
        return [{"id": "u1"}]

    with pytest.raises(TypeError, match="response is a list"):
        list(paginate(method, items="threads"))


def test_invalid_items_raises_before_any_call():
    method, calls = make_offset_method([[1]])

    with pytest.raises(TypeError, match="items="):
        paginate(method, items=42)
    assert calls == []


def test_method_without_page_arguments_raises_before_any_call():
    calls = []

    def not_paginated(user_id):
        calls.append(user_id)

    with pytest.raises(TypeError, match="does not accept 'page'/'per_page'"):
        paginate(not_paginated, "me")
    assert calls == []


def test_positional_arguments_raise_before_any_call():
    calls = []

    def method(channel_id=None, page=0, per_page=60):
        calls.append(channel_id)

    with pytest.raises(TypeError, match="only keyword arguments"):
        paginate(method, "cid")
    with pytest.raises(TypeError, match="only keyword arguments"):
        paginate(method, "cid", next_args=lambda r: None)
    assert calls == []


def test_cursor_mode_follows_next_args():
    pages = {None: [1, 2], 2: [3, 4], 4: []}
    calls = []

    def method(after=None):
        calls.append(after)
        return pages[after]

    result = list(paginate(method, next_args=lambda r: {"after": r[-1]} if r else None))
    assert result == [1, 2, 3, 4]
    assert calls == [None, 2, 4]


def test_cursor_mode_stops_when_next_args_returns_none():
    def method(after=None):
        return [1]

    assert list(paginate(method, next_args=lambda r: None)) == [1]


def test_cursor_mode_merges_multiple_parameters():
    calls = []

    def method(from_id=None, from_column_value=None):
        calls.append((from_id, from_column_value))
        return [{"id": "u1", "username": "alice"}] if from_id is None else []

    next_args = lambda r: {"from_id": r[-1]["id"], "from_column_value": r[-1]["username"]} if r else None
    assert len(list(paginate(method, next_args=next_args))) == 1
    assert calls == [(None, None), ("u1", "alice")]


def test_page_argument_in_cursor_mode_raises_before_any_call():
    calls = []

    def method(page=0, per_page=60, before=None):
        calls.append(page)
        return []

    with pytest.raises(TypeError, match="page= applies to offset pagination"):
        paginate(method, page=2, next_args=lambda r: None)
    assert calls == []


def test_cursor_arguments_replace_rather_than_merge():
    calls = []
    responses = iter([[1], [2], [3]])

    def method(after=None, before=None):
        calls.append({"after": after, "before": before})
        return next(responses)

    steps = iter([{"after": "a1"}, {"before": "b1"}, None])
    assert list(paginate(method, next_args=lambda r: next(steps))) == [1, 2, 3]

    # Switching cursor keys mid-walk must not leak the stale key
    assert calls == [
        {"after": None, "before": None},
        {"after": "a1", "before": None},
        {"after": None, "before": "b1"},
    ]


def test_cursor_arguments_override_a_starting_cursor():
    calls = []

    def method(before=None):
        calls.append(before)
        return [1] if before == "start" else []

    assert list(paginate(method, before="start", next_args=lambda r: {"before": "b2"} if r else None)) == [1]
    assert calls == ["start", "b2"]


def test_cursor_mode_consults_next_args_even_for_pages_without_items():
    pages = {
        None: {"items": [1], "next": "a"},
        "a": {"items": [], "next": "b"},
        "b": {"items": [2], "next": None},
    }
    calls = []

    def method(after=None):
        calls.append(after)
        return pages[after]

    result = list(paginate(method, items="items", next_args=lambda r: {"after": r["next"]} if r["next"] else None))
    assert result == [1, 2]
    assert calls == [None, "a", "b"]


def test_cursor_mode_defaults_per_page_when_method_accepts_it():
    calls = []

    def method(per_page=60, before=None):
        calls.append(per_page)
        return []

    list(paginate(method, next_args=lambda r: None))
    assert calls == [200]


def test_cursor_mode_omits_per_page_when_method_does_not_accept_it():
    calls = []

    def method(before=None):
        calls.append(before)
        return []

    list(paginate(method, next_args=lambda r: None))
    assert calls == [None]


def test_raw_response_gives_a_helpful_error():
    def method(page=0, per_page=60):
        return httpx.Response(200, text="<html>maintenance</html>", headers={"Content-Type": "text/html"})

    with pytest.raises(TypeError, match="non-JSON response"):
        list(paginate(method))


def test_cursor_mode_forwards_explicit_per_page():
    calls = []

    def method(per_page=60, before=None):
        calls.append(per_page)
        return []

    list(paginate(method, per_page=5, next_args=lambda r: None))
    assert calls == [5]


async def test_apaginate_iterates_across_pages():
    pages = [[1, 2], [3]]
    calls = []

    async def method(page=0, per_page=60):
        calls.append(page)
        return pages[page] if page < len(pages) else []

    assert [item async for item in apaginate(method, per_page=2)] == [1, 2, 3]
    assert calls == [0, 1]


async def test_apaginate_validates_before_any_call():
    async def not_paginated(user_id):
        pass  # pragma: no cover

    with pytest.raises(TypeError, match="does not accept 'page'/'per_page'"):
        apaginate(not_paginated, "me")


async def test_apaginate_cursor_mode():
    pages = {None: [1, 2], 2: []}

    async def method(after=None):
        return pages[after]

    result = [item async for item in apaginate(method, next_args=lambda r: {"after": r[-1]} if r else None)]
    assert result == [1, 2]


# Integration tests through the drivers and real endpoint methods


def make_users_handler(users):
    """MockTransport handler serving ``users`` through /api/v4/users pagination."""
    requests = []

    def handler(request):
        requests.append(request)
        page = int(request.url.params.get("page", 0))
        per_page = int(request.url.params.get("per_page", 60))
        return httpx.Response(200, json=users[page * per_page : (page + 1) * per_page])

    return handler, requests


def test_driver_paginate_users():
    users = [{"id": f"user{i}"} for i in range(5)]
    handler, requests = make_users_handler(users)
    driver = make_driver(handler)

    assert list(driver.paginate(driver.users.get_users, per_page=2)) == users
    assert [request.url.params["page"] for request in requests] == ["0", "1", "2"]


def test_driver_paginate_is_lazy():
    users = [{"id": f"user{i}"} for i in range(5)]
    handler, requests = make_users_handler(users)
    driver = make_driver(handler)

    iterator = driver.paginate(driver.users.get_users, per_page=2)
    assert requests == []

    next(iterator)
    assert len(requests) == 1


async def test_async_driver_paginate_users():
    users = [{"id": f"user{i}"} for i in range(3)]
    handler, requests = make_users_handler(users)
    driver = make_async_driver(handler)

    result = [user async for user in driver.paginate(driver.users.get_users, per_page=2)]
    assert result == users
    assert [request.url.params["page"] for request in requests] == ["0", "1"]


async def test_async_driver_paginate_posts_with_cursor():
    # Two pages of channel posts in reverse chronological order, linked by prev_post_id
    pages = {
        None: {"order": ["p4", "p3"], "posts": {"p4": {"id": "p4"}, "p3": {"id": "p3"}}, "prev_post_id": "p2"},
        "p3": {"order": ["p2", "p1"], "posts": {"p2": {"id": "p2"}, "p1": {"id": "p1"}}, "prev_post_id": ""},
    }
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json=pages[request.url.params.get("before")])

    driver = make_async_driver(handler)

    posts = [
        post
        async for post in driver.paginate(
            driver.posts.get_posts_for_channel,
            channel_id="channel_id",
            items=lambda r: [r["posts"][pid] for pid in r["order"]],
            next_args=lambda r: {"before": r["order"][-1]} if r["order"] and r["prev_post_id"] else None,
        )
    ]

    assert [post["id"] for post in posts] == ["p4", "p3", "p2", "p1"]
    assert [request.url.params.get("before") for request in requests] == [None, "p3"]
