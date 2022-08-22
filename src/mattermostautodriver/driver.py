import asyncio
import importlib
import logging
import os

from .client import AsyncClient, Client
from .websocket import Websocket

log = logging.getLogger("mattermostautodriver.api")
log.setLevel(logging.INFO)


class BaseDriver:
    """
    Contains the client, api and provides you with functions for
    login, logout and initializing a websocket connection.
    """

    default_options = {
        "scheme": "https",
        "url": "localhost",
        "port": 8065,
        "basepath": "/api/v4",
        "verify": True,
        "timeout": 30,
        "request_timeout": None,
        "login_id": None,
        "password": None,
        "token": None,
        "mfa_token": None,
        "auth": None,
        "keepalive": False,
        "keepalive_delay": 5,
        "websocket_kw_args": None,
        "debug": False,
        "http2": False,
        "proxy": None,
    }
    """
    Required options
        - url

    Either
        - login_id
        - password

    Or
        - token (https://docs.mattermost.com/developer/personal-access-tokens.html)

    Optional
        - scheme ('https')
        - port (8065)
        - verify (True)
        - timeout (30)
        - request_timeout (None)
        - mfa_token (None)
        - auth (None)
        - debug (False)

    Should not be changed
        - basepath ('/api/v4') - unlikely this would do any good
    """

    def __new__(cls, *args, **kwargs):
        cls._initialize_endpoints(cls)
        return super().__new__(cls, *args, **kwargs)

    def _initialize_endpoints(cls):
        module_path = os.path.dirname(os.path.abspath(__file__))
        endpoint_path = os.path.join((module_path), "endpoints")

        log.debug("Module path: %s - Endpoint path: %s", module_path, endpoint_path)

        for endpoint in os.listdir(endpoint_path):
            end = os.path.splitext(os.path.basename(endpoint))[0]

            if end == "base" or end.startswith("_"):
                # Skip base endpoint and any file starting with _ (__init__)
                continue

            # Load module and find the main module class
            # e.g. mattermostautodriver.endpoints.users -> Users
            module = importlib.import_module(f".endpoints.{end}", __package__)
            classnames = [x for x in dir(module) if x != "Base" and not x.startswith("_")]

            assert len(classnames) == 1, f"Unexpected endpoint configuration: {end}. Please report bug"

            _class = getattr(module, classnames.pop())

            # Setting self.module = property(ModuleClass(self.client))
            # Note: We need to bind the _class in the lambda scope or
            # the function won't act as a closure
            setattr(cls, end, property(lambda s, c=_class: c(s.client)))

    def __init__(self, options, client_cls):
        """
        :param options: A dict with the values from `default_options`
        :type options: dict
        """
        self.options = self.default_options.copy()
        if options is not None:
            self.options.update(options)
        self.driver = self.options
        if self.options["debug"]:
            log.setLevel(logging.DEBUG)
            log.warning(
                "Careful!!\nSetting debug to True, will reveal your password in the log output if you do driver.login()!\nThis is NOT for production!"
            )
        self.client = client_cls(self.options)
        self.websocket = None

    def disconnect(self):
        """Disconnects the driver from the server, stopping the websocket event loop."""
        self.websocket.disconnect()


class Driver(BaseDriver):
    def __init__(self, options=None, client_cls=Client):
        super().__init__(options, client_cls)

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(self, *exc_info):
        return self.client.__exit__(*exc_info)

    def init_websocket(self, event_handler, websocket_cls=Websocket):
        """
        Will initialize the websocket connection to the mattermost server.

        This should be run after login(), because the websocket needs to make
        an authentification.

        See https://api.mattermost.com/v4/#tag/WebSocket for which
        websocket events mattermost sends.

        Example of a really simple event_handler function

        .. code:: python

                async def my_event_handler(message):
                        print(message)


        :param event_handler: The function to handle the websocket events. Takes one argument.
        :type event_handler: Function(message)
        :return: The event loop
        """
        self.websocket = websocket_cls(self.options, self.client.token)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.websocket.connect(event_handler))
        return loop

    def login(self):
        """
        Logs the user in.

        The log in information is saved in the client
                - userid
                - username
                - cookies

        :return: The raw response from the request
        """
        if self.options["token"]:
            self.client.token = self.options["token"]
            result = self.users.get_user("me")
        else:
            response = self.users.login_user(
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                }
            )
            if response.status_code == 200:
                self.client.token = response.headers["Token"]
                self.client.cookies = response.cookies
            try:
                result = response.json()
            except ValueError:
                log.debug("Could not convert response to json, returning raw response")
                result = response

        log.debug(result)

        if "id" in result:
            self.client.userid = result["id"]
        if "username" in result:
            self.client.username = result["username"]

        return result

    def logout(self):
        """
        Log the user out.

        :return: The JSON response from the server
        """
        result = self.users.logout_user()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result


class AsyncDriver(BaseDriver):
    def __init__(self, options=None, client_cls=AsyncClient):
        super().__init__(options, client_cls)

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *exc_info):
        return await self.client.__aexit__(*exc_info)

    def init_websocket(self, event_handler, websocket_cls=Websocket):
        """
        Will initialize the websocket connection to the mattermost server.
        unlike the Driver.init_websocket, this one assumes you are async aware
        and returns a coroutine that can be awaited.  It will not return
        until shutdown() is called.

        This should be run after login(), because the websocket needs to make
        an authentification.

        See https://api.mattermost.com/v4/#tag/WebSocket for which
        websocket events mattermost sends.

        Example of a really simple event_handler function

        .. code:: python

                async def my_event_handler(message):
                        print(message)


        :param event_handler: The function to handle the websocket events. Takes one argument.
        :type event_handler: Function(message)
        :return: coroutine
        """
        self.websocket = websocket_cls(self.options, self.client.token)
        return self.websocket.connect(event_handler)

    async def login(self):
        """
        Logs the user in.

        The log in information is saved in the client
                - userid
                - username
                - cookies

        :return: The raw response from the request
        """
        if self.options["token"]:
            self.client.token = self.options["token"]
            result = await self.users.get_user("me")
        else:
            response = await self.users.login_user(
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                }
            )
            if response.status_code == 200:
                self.client.token = response.headers["Token"]
                self.client.cookies = response.cookies
            try:
                result = response.json()
            except ValueError:
                log.debug("Could not convert response to json, returning raw response")
                result = response

        log.debug(result)

        if "id" in result:
            self.client.userid = result["id"]
        if "username" in result:
            self.client.username = result["username"]

        return result

    async def logout(self):
        """
        Log the user out.

        :return: The JSON response from the server
        """
        result = await self.users.logout_user()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result
