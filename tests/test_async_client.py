import httpx
import pytest

from mattermostautodriver.client import AsyncClient
from mattermostautodriver.exceptions import TooManyRequests, UnknownMattermostError

from .test_client import error_response, rate_limit_response, sequence_handler


def make_async_client(handler, **extra_options):
    options = {
        "scheme": "http",
        "url": "localhost",
        "port": 8065,
        "auth": None,
        "debug": False,
        "proxy": None,
        "request_timeout": None,
        "max_retries": 0,  # retry tests opt in explicitly
        "transport": httpx.MockTransport(handler),
    }
    options.update(extra_options)
    return AsyncClient(options)


@pytest.fixture
def sleeps(monkeypatch):
    slept = []

    async def fake_sleep(seconds):
        slept.append(seconds)

    monkeypatch.setattr("mattermostautodriver.client.asyncio.sleep", fake_sleep)
    return slept


async def test_successful_json_response_is_returned():
    client = make_async_client(lambda request: httpx.Response(200, json={"id": "me"}))

    assert await client.get("/users/me") == {"id": "me"}


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
