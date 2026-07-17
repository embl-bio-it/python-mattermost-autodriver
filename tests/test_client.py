import httpx
import pytest

from mattermostautodriver.client import Client
from mattermostautodriver.exceptions import (
    ContentTooLarge,
    FeatureDisabled,
    InvalidMattermostError,
    InvalidOrMissingParameters,
    MethodNotAllowed,
    NoAccessTokenProvided,
    NotEnoughPermissions,
    ResourceNotFound,
    TooManyRequests,
    UnknownMattermostError,
)


def make_client(handler, **extra_options):
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
    return Client(options)


def error_response(status, message="something failed", error_id="api.some.error", request_id="req1234"):
    return httpx.Response(status, json={"message": message, "id": error_id, "request_id": request_id})


@pytest.mark.parametrize(
    "status,expected",
    [
        (400, InvalidOrMissingParameters),
        (401, NoAccessTokenProvided),
        (403, NotEnoughPermissions),
        (404, ResourceNotFound),
        (405, MethodNotAllowed),
        (413, ContentTooLarge),
        (501, FeatureDisabled),
        (418, UnknownMattermostError),
    ],
)
def test_error_status_mapping(status, expected):
    client = make_client(lambda request: error_response(status))

    with pytest.raises(expected):
        client.get("/users/me")


def test_error_fields_are_exposed():
    client = make_client(lambda request: error_response(404))

    with pytest.raises(ResourceNotFound) as excinfo:
        client.get("/users/unknown")

    assert excinfo.value.status_code == 404
    assert excinfo.value.error_id == "api.some.error"
    assert excinfo.value.request_id == "req1234"


def test_non_json_error_body_raises_invalid_error():
    client = make_client(lambda request: httpx.Response(502, text="<html>Bad Gateway</html>"))

    with pytest.raises(InvalidMattermostError):
        client.get("/users/me")


def test_successful_json_response_is_returned():
    client = make_client(lambda request: httpx.Response(200, json={"id": "me"}))

    assert client.get("/users/me") == {"id": "me"}


def rate_limit_response(headers=None):
    # Mattermost replies to rate limited requests with a plain text body,
    # see server/channels/app/ratelimit.go
    return httpx.Response(429, text="limit exceeded", headers=headers)


def test_429_with_plain_text_body_raises_too_many_requests():
    client = make_client(lambda request: rate_limit_response({"Retry-After": "7"}))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.retry_after == 7.0
    assert excinfo.value.status_code == 429
    assert excinfo.value.error_id is None


def test_429_without_headers_has_no_retry_after():
    client = make_client(lambda request: rate_limit_response())

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.retry_after is None


def test_429_falls_back_to_ratelimit_reset_header():
    client = make_client(lambda request: rate_limit_response({"X-RateLimit-Reset": "3"}))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.retry_after == 3.0


def test_429_prefers_retry_after_over_ratelimit_reset():
    client = make_client(lambda request: rate_limit_response({"Retry-After": "2", "X-RateLimit-Reset": "9"}))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.retry_after == 2.0


def test_429_with_json_body_exposes_error_fields():
    client = make_client(lambda request: error_response(429))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.error_id == "api.some.error"
    assert excinfo.value.request_id == "req1234"


def test_post_sends_json_options():
    seen = {}

    def handler(request):
        seen["json"] = request.read()
        return httpx.Response(200, json={"id": "post1"})

    client = make_client(handler)
    client.post("/posts", options={"channel_id": "abc", "message": "hi"})

    assert b'"channel_id"' in seen["json"]


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
    slept = []
    monkeypatch.setattr("mattermostautodriver.client.time.sleep", slept.append)
    return slept


def test_429_is_retried_and_honors_retry_after(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "2"}), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2
    assert sleeps == [2.0]


def test_429_is_retried_for_post(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "0"}), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.post("/posts", options={"message": "hi"}) == {"ok": 1}
    assert len(calls) == 2


def test_429_raises_after_retries_are_exhausted(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "0"})])
    client = make_client(handler, max_retries=3)

    with pytest.raises(TooManyRequests):
        client.get("/users/me")

    assert len(calls) == 4  # initial request + 3 retries


def test_max_retries_zero_disables_retrying(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "0"})])
    client = make_client(handler, max_retries=0)

    with pytest.raises(TooManyRequests):
        client.get("/users/me")

    assert len(calls) == 1


def test_retry_after_above_cap_raises_immediately(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "900"})])
    client = make_client(handler, max_retries=3)

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert len(calls) == 1
    assert sleeps == []
    assert excinfo.value.retry_after == 900.0


def test_get_is_retried_on_503(sleeps):
    handler, calls = sequence_handler([error_response(503), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2
    assert 0 < sleeps[0] <= 30


def test_post_is_not_retried_on_503(sleeps):
    handler, calls = sequence_handler([error_response(503)])
    client = make_client(handler, max_retries=3)

    with pytest.raises(UnknownMattermostError):
        client.post("/posts", options={"message": "hi"})

    assert len(calls) == 1


def test_get_is_retried_on_connection_error(sleeps):
    handler, calls = sequence_handler([httpx.ConnectError("connection refused"), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2


def test_post_is_not_retried_on_connection_error(sleeps):
    handler, calls = sequence_handler([httpx.ConnectError("connection refused")])
    client = make_client(handler, max_retries=3)

    with pytest.raises(httpx.ConnectError):
        client.post("/posts", options={"message": "hi"})

    assert len(calls) == 1


def test_requests_with_files_are_not_retried(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "0"})])
    client = make_client(handler, max_retries=3)

    with pytest.raises(TooManyRequests):
        client.post("/files", files={"files": b"content"})

    assert len(calls) == 1
