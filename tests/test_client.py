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


def test_post_sends_json_options():
    seen = {}

    def handler(request):
        seen["json"] = request.read()
        return httpx.Response(200, json={"id": "post1"})

    client = make_client(handler)
    client.post("/posts", options={"channel_id": "abc", "message": "hi"})

    assert b'"channel_id"' in seen["json"]
