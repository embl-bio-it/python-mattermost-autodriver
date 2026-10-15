import httpx
import pytest

from conftest import (
    DRIVER_OPTIONS,
    error_response,
    login_handler,
    make_async_client,
    rate_limit_response,
    sequence_handler,
    session_cookie_response,
)
from mattermostautodriver import AsyncTypedDriver
from mattermostautodriver.exceptions import NoAccessTokenProvided, TooManyRequests, UnknownMattermostError


async def test_successful_json_response_is_returned():
    client = make_async_client(lambda request: httpx.Response(200, json={"id": "me"}))

    assert await client.get("/users/me") == {"id": "me"}


async def test_all_none_json_body_is_sent_as_empty_object():
    # Endpoints declaring a JSON request body reject a request without any
    # body, so a body whose optional values were all left out must still be
    # transmitted as {}
    seen = {}

    def handler(request):
        seen["content"] = request.content
        return httpx.Response(200, json={})

    client = make_async_client(handler)
    await client.post("/endpoint", options={"include_deleted": None, "dry_run": None})

    assert seen["content"] == b"{}"


async def test_429_raises_too_many_requests():
    client = make_async_client(lambda request: rate_limit_response({"Retry-After": "7"}))

    with pytest.raises(TooManyRequests) as excinfo:
        await client.get("/users/me")

    assert excinfo.value.retry_after == 7.0


async def test_429_is_retried_and_honors_retry_after(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "2"}), httpx.Response(200, json={"ok": 1})])
    client = make_async_client(handler, max_retries=3)

    assert await client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2
    assert sleeps == [2.0]


async def test_429_raises_after_retries_are_exhausted(sleeps):
    # Without an ok response in `sequence_handler`, this test will repeat "Retry-After 0 seconds" for all requests, exhausting the client `max_retries`.
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "0"})])

    client = make_async_client(handler, max_retries=3)

    with pytest.raises(TooManyRequests):
        await client.get("/users/me")

    assert len(calls) == 4  # initial request + 3 retries


async def test_get_is_retried_on_503(sleeps):
    handler, calls = sequence_handler([error_response(503), httpx.Response(200, json={"ok": 1})])
    client = make_async_client(handler, max_retries=3)

    assert await client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2


async def test_post_is_not_retried_on_503(sleeps):
    handler, calls = sequence_handler([error_response(503)])
    client = make_async_client(handler, max_retries=3)

    with pytest.raises(UnknownMattermostError):
        await client.post("/posts", options={"message": "hi"})

    assert len(calls) == 1


async def test_get_is_retried_on_connection_error(sleeps):
    handler, calls = sequence_handler([httpx.ConnectError("connection refused"), httpx.Response(200, json={"ok": 1})])
    client = make_async_client(handler, max_retries=3)

    assert await client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2


async def test_post_is_not_retried_on_connection_error(sleeps):
    handler, calls = sequence_handler([httpx.ConnectError("connection refused")])
    client = make_async_client(handler, max_retries=3)

    with pytest.raises(httpx.ConnectError):
        await client.post("/posts", options={"message": "hi"})

    assert len(calls) == 1


async def test_session_cookies_are_not_stored_or_replayed():
    handler, calls = sequence_handler([session_cookie_response(), httpx.Response(200, json={})])
    client = make_async_client(handler)
    client.token = "tok123"

    await client.post("/posts", options={"message": "hi"})
    await client.post("/posts", options={"message": "again"})

    assert len(calls) == 2
    # Only the session cookies are dropped, the load balancer cookie is kept
    assert calls[1].headers["Cookie"] == "AWSALB=lb1"
    assert calls[1].headers["Authorization"] == "Bearer tok123"
    assert dict(client.client.cookies) == {"AWSALB": "lb1"}


async def test_driver_relogin_after_session_cookie_sends_no_cookie():
    handler, calls = login_handler()
    driver = AsyncTypedDriver({**DRIVER_OPTIONS, "transport": httpx.MockTransport(handler)})

    await driver.login()
    assert driver.client.token == "tok123"
    assert driver.client.userid == "u1"
    assert driver.client.username == "bot"

    await driver.posts.create_post("channel1", "hi")  # the server extends the session here
    await driver.login()
    await driver.logout()

    assert [call.url.path for call in calls] == [
        "/api/v4/users/login",
        "/api/v4/posts",
        "/api/v4/users/login",
        "/api/v4/users/logout",
    ]
    assert all("MMAUTHTOKEN" not in call.headers.get("Cookie", "") for call in calls)
    assert calls[2].headers["Cookie"] == "AWSALB=lb1"
    assert driver.client.token == ""
    assert driver.client.userid == ""
    assert driver.client.username == ""


async def test_logout_clears_state_when_server_rejects_it():
    driver = AsyncTypedDriver({**DRIVER_OPTIONS, "transport": httpx.MockTransport(lambda request: error_response(401))})
    driver.client.token = "tok123"
    driver.client.userid = "u1"
    driver.client.username = "bot"

    with pytest.raises(NoAccessTokenProvided):
        await driver.logout()

    assert driver.client.token == ""
    assert driver.client.userid == ""
    assert driver.client.username == ""
