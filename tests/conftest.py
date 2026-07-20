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
