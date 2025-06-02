from .base import BaseDriver
from ..client import Client

class BaseDriverWithEndpoints(BaseDriver):
    def __init__(self, options=None, client_cls=Client, *args, **kwargs):
        super().__init__(options, client_cls, *args, **kwargs)
