import asyncio
import logging
import warnings

from ..client import AsyncClient, Client
from ..websocket import Websocket

from .endpoint_base import BaseDriverWithEndpoints, TypedBaseDriverWithEndpoints


log = logging.getLogger("mattermostautodriver.api")
log.setLevel(logging.INFO)


class Driver(BaseDriverWithEndpoints):
    def __new__(cls, options=None, client_cls=Client, *args, **kwargs):
        message = (
            "The old dictionary based API interface is deprecated and will be removed in the future. "
            "Please adapt your code by using the TypedDriver class and expand the arguments you would typically pass. "
            "See https://embl-bio-it.github.io/python-mattermost-autodriver/api_deprecation.html "
            "for additional details."
        )
        warnings.warn(message, DeprecationWarning, stacklevel=2)

        return super().__new__(cls)

    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)

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

        See https://developers.mattermost.com/api-documentation/#/websocket for which
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
            # Note self.user.login() can't be used here as it returns JSON
            # due to self.client.post() pre-defined behavior
            response = self.client.make_request(
                "post",
                "/api/v4/users/login",
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                },
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
        result = self.users.logout()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result

    def close(self):
        self.client.close()


class TypedDriver(TypedBaseDriverWithEndpoints):
    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)

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

        See https://developers.mattermost.com/api-documentation/#/websocket for which
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
            # Note self.user.login() can't be used here as it returns JSON
            # due to self.client.post() pre-defined behavior
            response = self.client.make_request(
                "post",
                "/api/v4/users/login",
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                },
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
        result = self.users.logout()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result

    def close(self):
        self.client.close()


class AsyncDriver(BaseDriverWithEndpoints):
    def __new__(cls, options=None, client_cls=Client, *args, **kwargs):
        message = (
            "The old dictionary based API interface is deprecated and will be removed in the future. "
            "Please adapt your code by using the AsyncTypedDriver class and expand the arguments you would typically pass. "
            "See https://embl-bio-it.github.io/python-mattermost-autodriver/api_deprecation.html "
            "for additional details."
        )
        warnings.warn(message, DeprecationWarning, stacklevel=2)

        return super().__new__(cls)

    def __init__(self, options=None, client_cls=AsyncClient, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)

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

        See https://developers.mattermost.com/api-documentation/#/websocket for which
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
            # Note self.user.login() can't be used here as it returns JSON
            # due to self.client.post() pre-defined behavior
            response = await self.client.make_request(
                "post",
                "/api/v4/users/login",
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                },
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
        result = await self.users.logout()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result

    async def close(self):
        await self.client.close()


class AsyncTypedDriver(TypedBaseDriverWithEndpoints):
    def __init__(self, options=None, client_cls=AsyncClient, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)

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

        See https://developers.mattermost.com/api-documentation/#/websocket for which
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
            # Note self.user.login() can't be used here as it returns JSON
            # due to self.client.post() pre-defined behavior
            response = await self.client.make_request(
                "post",
                "/api/v4/users/login",
                {
                    "login_id": self.options["login_id"],
                    "password": self.options["password"],
                    "token": self.options["mfa_token"],
                },
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
        result = await self.users.logout()
        self.client.token = ""
        self.client.userid = ""
        self.client.username = ""
        self.client.cookies = None
        return result

    async def close(self):
        await self.client.close()
