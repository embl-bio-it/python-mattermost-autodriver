import logging
import warnings

from ..client import Client

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
    """

    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
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
        if self.websocket is not None:
            self.websocket.disconnect()
