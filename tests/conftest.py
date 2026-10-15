import httpx
import pytest

from mattermostautodriver.client import AsyncClient, Client

_BASE_OPTIONS = {
    "scheme": "http",
    "url": "localhost",
    "port": 8065,
    "auth": None,
    "debug": False,
    "proxy": None,
    "request_timeout": None,
    "max_retries": 0,  # retry tests opt in explicitly
}


def _client_options(handler, extra_options):
    options = {**_BASE_OPTIONS, "transport": httpx.MockTransport(handler)}
    options.update(extra_options)
    return options


def make_client(handler, **extra_options):
    return Client(_client_options(handler, extra_options))


def make_async_client(handler, **extra_options):
    return AsyncClient(_client_options(handler, extra_options))


def error_response(status, message="something failed", error_id="api.some.error", request_id="req1234"):
    return httpx.Response(status, json={"message": message, "id": error_id, "request_id": request_id})


# Offline driver options for password login against a mock transport
DRIVER_OPTIONS = {**_BASE_OPTIONS, "login_id": "bot", "password": "pw"}


def session_cookie_response():
    """A response pushing the Mattermost session cookies plus a load balancer cookie.

    The server attaches its session cookies to e.g. ``POST /api/v4/posts``
    when it extends the session expiry (``ExtendSessionExpiryIfNeeded``).
    """
    return httpx.Response(
        200,
        json={"id": "post1"},
        headers=[
            ("Set-Cookie", "MMAUTHTOKEN=tok123; Path=/; Max-Age=2592000; HttpOnly"),
            ("Set-Cookie", "MMUSERID=u1; Path=/; Max-Age=2592000"),
            ("Set-Cookie", "MMCSRF=csrf1; Path=/; Max-Age=2592000"),
            ("Set-Cookie", "AWSALB=lb1; Path=/"),
        ],
    )


def login_handler():
    """Handler emulating login, a post that extends the session, and logout."""
    calls = []

    def handler(request):
        calls.append(request)
        if request.url.path == "/api/v4/users/login":
            return httpx.Response(200, json={"id": "u1", "username": "bot"}, headers={"Token": "tok123"})
        if request.url.path == "/api/v4/posts":
            return session_cookie_response()
        return httpx.Response(200, json={"status": "OK"})

    return handler, calls


def rate_limit_response(headers=None):
    # Mattermost replies to rate limited requests with a plain text body,
    # see server/channels/app/ratelimit.go
    return httpx.Response(429, text="limit exceeded", headers=headers)


def sequence_handler(responses):
    """Handler returning (or raising) each item in turn, repeating the last one."""
    calls = []

    def handler(request):
        item = responses[min(len(calls), len(responses) - 1)]
        calls.append(request)
        if isinstance(item, Exception):
            raise item
        return item

    return handler, calls


@pytest.fixture
def sleeps(monkeypatch):
    """Record retry sleeps from either client instead of actually sleeping."""
    slept = []

    async def fake_async_sleep(seconds):
        slept.append(seconds)

    monkeypatch.setattr("mattermostautodriver.client.time.sleep", slept.append)
    monkeypatch.setattr("mattermostautodriver.client.asyncio.sleep", fake_async_sleep)
    return slept
