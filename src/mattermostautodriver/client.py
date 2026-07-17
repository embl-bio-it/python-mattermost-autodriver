"""
Client for the driver, which holds information about the logged in user
and actually makes the requests to the mattermost server
"""

import asyncio
import logging
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import httpx

from .exceptions import (
    InvalidMattermostError,
    InvalidOrMissingParameters,
    NoAccessTokenProvided,
    NotEnoughPermissions,
    ResourceNotFound,
    MethodNotAllowed,
    ContentTooLarge,
    FeatureDisabled,
    TooManyRequests,
    UnknownMattermostError,
)

log = logging.getLogger("mattermostautodriver.websocket")
log.setLevel(logging.INFO)


class BaseClient:
    _RETRY_STATUS_CODES = (502, 503, 504)
    _IDEMPOTENT_METHODS = ("get", "put", "delete", "head")

    def __init__(self, options):
        self._url = self._make_url(options["scheme"], options["url"], options["port"])
        self._scheme = options["scheme"]
        self._port = options["port"]
        self._auth = options["auth"]
        if options["debug"]:
            self.activate_verbose_logging()

        self._options = options
        self._token = ""
        self._cookies = None
        self._userid = ""
        self._username = ""
        self._proxy = None
        if options["proxy"]:
            self._proxy = {"all://": options["proxy"]}

        self._max_retries = options.get("max_retries", 3)
        self._retry_max_sleep = options.get("retry_max_sleep", 30)

    @staticmethod
    def _make_url(scheme, url, port):
        return f"{scheme:s}://{url:s}:{port:d}"

    @staticmethod
    def activate_verbose_logging(level=logging.DEBUG):
        # We register handlers for mattermostautodriver which takes care of
        # mattermostautodriver.websocket and mattermostautodriver.api
        #
        # In addition we also add handlers to httpx and httpcore loggers
        # if none are present

        loggers = (
            "mattermostautodriver",
            "httpx",
            "httpcore",
        )

        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(levelname)s [%(asctime)s] %(name)s - %(message)s"))

        for logger in loggers:
            _logger = logging.getLogger(logger)
            _logger.setLevel(level)

            if not _logger.hasHandlers():
                _logger.addHandler(handler)

    @property
    def userid(self):
        """
        :return: The user id of the logged in user
        """
        return self._userid

    @userid.setter
    def userid(self, user_id):
        self._userid = user_id

    @property
    def username(self):
        """
        :return: The username of the logged in user. If none, returns an emtpy string.
        """
        return self._username

    @property
    def request_timeout(self):
        """
        :return: The configured timeout for the requests
        """
        return self._options["request_timeout"]

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def url(self):
        return self._url

    @property
    def cookies(self):
        """
        :return: The cookie given on login
        """
        return self._cookies

    @cookies.setter
    def cookies(self, cookies):
        self._cookies = cookies

    @property
    def token(self):
        """
        :return: The token for the login
        """
        return self._token

    @token.setter
    def token(self, t):
        self._token = t

    def auth_header(self):
        if self._auth:
            return None
        if self._token == "":
            return {}
        return {"Authorization": "Bearer {token:s}".format(token=self._token)}

    def _build_request(self, method, options=None, params=None, data=None, files=None):
        def filter_dict_or_none(d):
            if not isinstance(d, dict):
                # this method is only meant to filter dicts, return everything else unchanged
                return d

            filtered_d = {k: v for k, v in d.items() if v is not None}

            if filtered_d:
                return filtered_d

            return None

        request_params = {"headers": self.auth_header(), "timeout": self.request_timeout}

        filtered_params = filter_dict_or_none(params)
        filtered_options = filter_dict_or_none(options)
        filtered_data = filter_dict_or_none(data)
        filtered_files = filter_dict_or_none(files)

        if filtered_params is not None:
            request_params["params"] = filtered_params

        if method in ("post", "put"):
            if filtered_options is not None:
                request_params["json"] = filtered_options
            if filtered_data is not None:
                request_params["data"] = filtered_data
            if filtered_files is not None:
                request_params["files"] = filtered_files

        if self._auth is not None:
            request_params["auth"] = self._auth()

        return self._get_request_method(method, self.client), self.url, request_params

    # Numeric header values above this are far too large to be a wait time
    # in seconds and are interpreted as an absolute unix timestamp instead
    _EPOCH_THRESHOLD = 1e8

    @staticmethod
    def _parse_wait_time(value):
        """Parse a rate limit header value into seconds to wait from now.

        Handles the conventions used in the wild:

        - delay in seconds ("120") - RFC 7231 ``Retry-After`` and Mattermost's
          relative ``X-RateLimit-Reset``
        - HTTP-date ("Wed, 21 Oct 2015 07:28:00 GMT") - the alternative
          ``Retry-After`` form, sent by some proxies and CDNs
        - absolute unix timestamp ("1794000000") - the ``X-RateLimit-Reset``
          convention of many API gateways

        Returns non-negative seconds, or None if the value is unparseable.
        """
        try:
            seconds = float(value)
        except ValueError:
            try:
                when = parsedate_to_datetime(value)
            except (TypeError, ValueError):
                return None
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
            seconds = (when - datetime.now(timezone.utc)).total_seconds()
        else:
            if seconds > BaseClient._EPOCH_THRESHOLD:
                seconds -= time.time()
        return max(0.0, seconds)

    @staticmethod
    def _parse_retry_after(response):
        for header in ("Retry-After", "X-RateLimit-Reset"):
            value = response.headers.get(header)
            if value is not None:
                wait = BaseClient._parse_wait_time(value)
                if wait is not None:
                    return wait
        return None

    @staticmethod
    def _parse_error_fields(response):
        """Extract the fields of a standard Mattermost JSON error body.

        Returns (message, error_id, request_id, is_oauth_error). Raises
        ValueError when the body does not follow the standard error schema,
        with the original parsing error as its cause.
        """
        try:
            data = response.json()
            return (
                data["message"],
                data["id"],
                data["request_id"],
                data.get("is_oauth", False),  # is_oauth is not always present
            )
        except (ValueError, KeyError, TypeError) as err:
            raise ValueError("Response body does not follow the Mattermost error schema") from err

    @staticmethod
    def _make_rate_limit_error(response):
        # Mattermost's rate limiter replies with a plain text body ("limit exceeded")
        # rather than the standard JSON error, so both the wait time and the error
        # details are parsed on a best effort basis.
        retry_after = BaseClient._parse_retry_after(response)

        try:
            message, error_id, request_id, is_oauth_error = BaseClient._parse_error_fields(response)
        except ValueError:
            message = response.text
            error_id = None
            request_id = None
            is_oauth_error = False

        return TooManyRequests(message, retry_after, error_id, request_id, is_oauth_error)

    @staticmethod
    def _body_is_replayable(data, files):
        """Whether the request body can safely be sent a second time.

        Files and non-dict ``data`` bodies (e.g. a file object or generator)
        are consumed when the request is first sent, so resending them would
        transmit an empty body.
        """
        return files is None and (data is None or isinstance(data, dict))

    def _retry_delay(self, method, attempt, data=None, files=None, response=None):
        """Seconds to wait before retrying the request, or None if it must not be retried.

        A 429 is retried for any method since the server rejected the request
        outright. Connection errors (``response is None``) and 502/503/504
        responses are only retried for idempotent methods, as a POST may
        already have been processed. Requests whose body is not replayable
        are never retried.
        """
        if not self._body_is_replayable(data, files):
            return None

        if attempt >= self._max_retries:
            return None

        method = method.lower()
        backoff = min(0.5 * 2**attempt * (1 + random.random()), self._retry_max_sleep)

        if response is None:
            if method in self._IDEMPOTENT_METHODS:
                return backoff
            return None

        if response.status_code == 429:
            retry_after = self._parse_retry_after(response)
            if retry_after is None:
                return backoff
            if retry_after > self._retry_max_sleep:
                return None
            return retry_after

        if response.status_code in self._RETRY_STATUS_CODES and method in self._IDEMPOTENT_METHODS:
            return backoff

        return None

    @staticmethod
    def _check_response(response):
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                raise BaseClient._make_rate_limit_error(e.response) from None
            try:
                message, error_id, request_id, is_oauth_error = BaseClient._parse_error_fields(e.response)
            except ValueError as val_err:
                raise InvalidMattermostError(e.response.text, e.response.status_code) from val_err
            log.error(message)

            if e.response.status_code == 400:
                raise InvalidOrMissingParameters(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 401:
                raise NoAccessTokenProvided(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 403:
                raise NotEnoughPermissions(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 404:
                raise ResourceNotFound(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 405:
                raise MethodNotAllowed(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 413:
                raise ContentTooLarge(message, error_id, request_id, is_oauth_error) from None
            elif e.response.status_code == 501:
                raise FeatureDisabled(message, error_id, request_id, is_oauth_error) from None
            else:
                raise UnknownMattermostError(
                    message, e.response.status_code, error_id, request_id, is_oauth_error
                ) from e

        log.debug(response)

    @staticmethod
    def _get_request_method(method, client):
        method = method.lower()
        if method == "post":
            return client.post
        elif method == "put":
            return client.put
        elif method == "delete":
            return client.delete
        elif method == "head":
            return client.head
        else:
            return client.get


class Client(BaseClient):
    def __init__(self, options):
        super().__init__(options)
        self.client = httpx.Client(
            http2=options.get("http2", False),
            proxy=self._proxy,
            verify=options.get("verify", True),
            transport=options.get("transport"),
        )

    def make_request(self, method, endpoint, options=None, params=None, data=None, files=None, basepath=None):
        if basepath is not None:
            raise DeprecationWarning(
                "'basepath' no longer has any effect and will be removed in version 3.x. "
                "Please remove it from your code."
            )
        request, url, request_params = self._build_request(method, options, params, data, files)

        attempt = 0
        while True:
            try:
                response = request(url + endpoint, **request_params)
            except httpx.TransportError as e:
                delay = self._retry_delay(method, attempt, data=data, files=files)
                if delay is None:
                    raise
                log.warning("Received %r - retrying in %.1f seconds", e, delay)
            else:
                delay = self._retry_delay(method, attempt, data=data, files=files, response=response)
                if delay is None:
                    self._check_response(response)
                    return response
                log.warning("Received status %d - retrying in %.1f seconds", response.status_code, delay)
            time.sleep(delay)
            attempt += 1

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(self, *exc_info):
        return self.client.__exit__(*exc_info)

    def get(self, endpoint, options=None, params=None):
        response = self.make_request("get", endpoint, options=options, params=params)

        if response.headers["Content-Type"] != "application/json":
            log.debug("Response is not application/json, returning raw response")
            return response

        try:
            return response.json()
        except ValueError:
            log.debug("Could not convert response to json, returning raw response")
            return response

    def post(self, endpoint, options=None, params=None, data=None, files=None):
        return self.make_request("post", endpoint, options=options, params=params, data=data, files=files).json()

    def put(self, endpoint, options=None, params=None, data=None):
        return self.make_request("put", endpoint, options=options, params=params, data=data).json()

    def delete(self, endpoint, options=None, params=None, data=None):
        return self.make_request("delete", endpoint, options=options, params=params, data=data).json()

    def head(self, endpoint, options=None, params=None):
        # HEAD responses carry no body; return the raw response for headers/status
        return self.make_request("head", endpoint, options=options, params=params)

    def call_webhook(self, hook_id, options=None):
        return self.make_request("post", "/hooks/" + hook_id, options=options)

    def close(self):
        self.client.close()


class AsyncClient(BaseClient):
    def __init__(self, options):
        super().__init__(options)
        self.client = httpx.AsyncClient(
            http2=options.get("http2", False),
            proxy=self._proxy,
            verify=options.get("verify", True),
            transport=options.get("transport"),
        )

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *exc_info):
        return await self.client.__aexit__(*exc_info)

    async def make_request(self, method, endpoint, options=None, params=None, data=None, files=None, basepath=None):
        if basepath is not None:
            raise DeprecationWarning(
                "'basepath' no longer has any effect and will be removed in version 3.x. "
                "Please remove it from your code."
            )
        request, url, request_params = self._build_request(method, options, params, data, files)

        attempt = 0
        while True:
            try:
                response = await request(url + endpoint, **request_params)
            except httpx.TransportError as e:
                delay = self._retry_delay(method, attempt, data=data, files=files)
                if delay is None:
                    raise
                log.warning("Received %r - retrying in %.1f seconds", e, delay)
            else:
                delay = self._retry_delay(method, attempt, data=data, files=files, response=response)
                if delay is None:
                    self._check_response(response)
                    return response
                log.warning("Received status %d - retrying in %.1f seconds", response.status_code, delay)
            await asyncio.sleep(delay)
            attempt += 1

    async def get(self, endpoint, options=None, params=None):
        response = await self.make_request("get", endpoint, options=options, params=params)

        if response.headers["Content-Type"] != "application/json":
            log.debug("Response is not application/json, returning raw response")
            return response

        try:
            return response.json()
        except ValueError:
            log.debug("Could not convert response to json, returning raw response")
            return response

    async def post(self, endpoint, options=None, params=None, data=None, files=None):
        response = await self.make_request("post", endpoint, options=options, params=params, data=data, files=files)
        return response.json()

    async def put(self, endpoint, options=None, params=None, data=None):
        response = await self.make_request("put", endpoint, options=options, params=params, data=data)
        return response.json()

    async def delete(self, endpoint, options=None, params=None, data=None):
        response = await self.make_request("delete", endpoint, options=options, params=params, data=data)
        return response.json()

    async def head(self, endpoint, options=None, params=None):
        # HEAD responses carry no body; return the raw response for headers/status
        return await self.make_request("head", endpoint, options=options, params=params)

    async def call_webhook(self, hook_id, options=None):
        response = await self.make_request("post", "/hooks/" + hook_id, options=options)
        return response.json()

    async def close(self):
        await self.client.aclose()
