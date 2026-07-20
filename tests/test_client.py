import io
import time
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

import httpx
import pytest

from conftest import error_response, make_client, rate_limit_response, sequence_handler
from mattermostautodriver.client import BaseClient
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


def test_429_with_unparseable_retry_after_falls_back_to_ratelimit_reset():
    client = make_client(lambda request: rate_limit_response({"Retry-After": "soon", "X-RateLimit-Reset": "3"}))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.retry_after == 3.0


def test_parse_wait_time_seconds():
    assert BaseClient._parse_wait_time("120") == 120.0


def test_parse_wait_time_clamps_negative_to_zero():
    assert BaseClient._parse_wait_time("-5") == 0.0


# Wait values are computed against "now" twice: once when a test builds the
# header value and once when _parse_wait_time subtracts the current time.
# The HTTP-date and epoch formats truncate to whole seconds, eating up to one
# second on their own; the rest is slack for test execution on slow CI runners.
WAIT_SLACK = 5


def test_parse_wait_time_http_date():
    value = format_datetime(datetime.now(timezone.utc) + timedelta(seconds=60))
    assert 60 - WAIT_SLACK < BaseClient._parse_wait_time(value) <= 60


def test_parse_wait_time_http_date_in_the_past():
    value = format_datetime(datetime.now(timezone.utc) - timedelta(seconds=60))
    assert BaseClient._parse_wait_time(value) == 0.0


def test_parse_wait_time_epoch_timestamp():
    value = str(int(time.time()) + 60)
    assert 60 - WAIT_SLACK < BaseClient._parse_wait_time(value) <= 60


def test_parse_wait_time_garbage_returns_none():
    assert BaseClient._parse_wait_time("soon") is None


def test_429_with_http_date_retry_after():
    value = format_datetime(datetime.now(timezone.utc) + timedelta(seconds=60))
    client = make_client(lambda request: rate_limit_response({"Retry-After": value}))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert 60 - WAIT_SLACK < excinfo.value.retry_after <= 60


def test_429_with_epoch_ratelimit_reset_is_retried(sleeps):
    headers = {"X-RateLimit-Reset": str(int(time.time()) + 60)}
    handler, calls = sequence_handler([rate_limit_response(headers), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3, retry_max_sleep=120)

    assert client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2
    assert 60 - WAIT_SLACK < sleeps[0] <= 60


def test_429_with_json_body_exposes_error_fields():
    client = make_client(lambda request: error_response(429))

    with pytest.raises(TooManyRequests) as excinfo:
        client.get("/users/me")

    assert excinfo.value.error_id == "api.some.error"
    assert excinfo.value.request_id == "req1234"


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
    assert sleeps == [0.0]


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
    # First-attempt backoff is 0.5 * 2**0 * (1 + random())
    assert 0.5 <= sleeps[0] <= 1.0


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


@pytest.mark.filterwarnings("ignore::DeprecationWarning")  # httpx warns about stream bodies via data=
def test_put_with_stream_data_is_not_retried(sleeps):
    handler, calls = sequence_handler([error_response(503)])
    client = make_client(handler, max_retries=3)

    with pytest.raises(UnknownMattermostError):
        client.put("/imports", data=io.BytesIO(b"payload"))

    assert len(calls) == 1


def test_put_with_dict_data_is_retried(sleeps):
    handler, calls = sequence_handler([error_response(503), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.put("/users/me/patch", data={"nickname": "x"}) == {"ok": 1}
    assert len(calls) == 2


def test_negative_retry_after_is_clamped_to_zero(sleeps):
    handler, calls = sequence_handler([rate_limit_response({"Retry-After": "-5"}), httpx.Response(200, json={"ok": 1})])
    client = make_client(handler, max_retries=3)

    assert client.get("/users/me") == {"ok": 1}
    assert len(calls) == 2
    assert sleeps == [0.0]
