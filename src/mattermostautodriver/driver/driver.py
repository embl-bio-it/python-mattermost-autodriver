import asyncio
import logging

from ..client import AsyncClient, Client
from ..pagination import apaginate as _apaginate, paginate as _paginate
from ..websocket import Websocket

from .endpoint_base import TypedBaseDriverWithEndpoints

log = logging.getLogger("mattermostautodriver.api")
log.setLevel(logging.INFO)


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

    def paginate(self, method, *args, per_page=None, items=None, next_args=None, max_pages=None, **kwargs):
        """
        Lazily iterate over every item of a paginated endpoint method.

        Wraps any endpoint method accepting ``page``/``per_page`` and yields
        the items of each page, fetching the next page only when iteration
        reaches it. Iteration stops when a page returns fewer items than
        ``per_page``. As the server silently caps ``per_page`` above 200,
        larger values make a short page inconclusive and iteration only
        stops on an empty or shrinking page.

        .. code:: python

                for user in driver.paginate(driver.users.get_users, in_team=team_id):
                        print(user["username"])

        Endpoints wrapping the items in an object need ``items=`` to say where
        the items are, e.g. ``items="threads"`` for ``threads.get_user_threads``.

        Cursor based endpoints (no ``page``/``per_page``, or cursor parameters
        such as ``before``/``after``) are supported by passing ``next_args=``,
        a callable receiving each response and returning the extra keyword
        arguments for the next call, or ``None`` to stop:

        .. code:: python

                for post in driver.paginate(
                        driver.posts.get_posts_for_channel, channel_id,
                        items=lambda r: [r["posts"][pid] for pid in r["order"]],
                        next_args=lambda r: {"before": r["order"][-1]} if r["prev_post_id"] else None,
                ):
                        print(post["message"])

        Methods that support neither raise ``TypeError`` before any request is made.

        :param method: The endpoint method to paginate, e.g. ``driver.users.get_users``
        :param args: Positional arguments (e.g. path parameters) passed through to ``method``
        :param per_page: Page size, defaults to 200. In cursor mode the default
                is only applied when ``method`` accepts a ``per_page`` parameter.
        :param items: Where to find the items when the response is not a plain
                list: a response key or a callable ``response -> list``
        :param next_args: Enables cursor mode: callable ``response -> dict | None``
                returning the keyword arguments for the next call
        :param max_pages: Optional hard limit on the number of pages fetched
        :param kwargs: Keyword arguments passed through to ``method``. ``page``
                may be given as the starting page (defaults to 0).
        :return: Generator yielding one item at a time
        """
        return _paginate(
            method, *args, per_page=per_page, items=items, next_args=next_args, max_pages=max_pages, **kwargs
        )

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

    def paginate(self, method, *args, per_page=None, items=None, next_args=None, max_pages=None, **kwargs):
        """
        Lazily iterate over every item of a paginated endpoint method.

        Asynchronous variant of :meth:`TypedDriver.paginate` — identical
        parameters, but returns an async generator:

        .. code:: python

                async for user in driver.paginate(driver.users.get_users, in_team=team_id):
                        print(user["username"])

        :return: Async generator yielding one item at a time
        """
        return _apaginate(
            method, *args, per_page=per_page, items=items, next_args=next_args, max_pages=max_pages, **kwargs
        )

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
