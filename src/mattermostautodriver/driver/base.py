import importlib
import logging
import os
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

    def __new__(cls, options=None, client_cls=Client, *args, **kwargs):
        old_api = kwargs.get("old_api", False)
        if old_api:
            message = (
                "The old dictionary based API interface is deprecated and will be removed in the future. "
                "Please adapt your code to expand the arguments you would typically pass. "
                "See https://embl-bio-it.github.io/python-mattermost-autodriver/api_deprecation.html "
                "for additional details."
            )
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            cls._endpoints_path = "endpoints_old"
        else:
            cls._endpoints_path = "endpoints"
        cls._initialize_endpoints(cls)
        return super().__new__(cls)

    def _initialize_endpoints(cls):
        module_path = os.path.dirname(os.path.abspath(__file__))
        endpoint_path = os.path.join((module_path), cls._endpoints_path)

        log.debug("Module path: %s - Endpoint path: %s", module_path, endpoint_path)

        for endpoint in os.listdir(endpoint_path):
            end = os.path.splitext(os.path.basename(endpoint))[0]

            if end.startswith("_"):
                # Skip _base endpoint and any other file starting with _ (e.g. __init__)
                continue

            # Load module and find the main module class
            # e.g. mattermostautodriver.endpoints.users -> Users
            module = importlib.import_module(f".{cls._endpoints_path}.{end}", __package__)
            classnames = module.__all__

            assert len(classnames) == 1, f"Unexpected endpoint configuration: {end}. Please report bug"

            _class = getattr(module, classnames[0])

            # Setting self.module = property(ModuleClass(self.client))
            # Note: We need to bind the _class in the lambda scope or
            # the function won't act as a closure
            setattr(cls, end, property(lambda s, c=_class: c(s.client)))

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
