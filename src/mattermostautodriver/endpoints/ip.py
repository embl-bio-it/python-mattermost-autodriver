from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Ip"]


class Ip(Base):

    def get_ip_filters(self):
        """Get all IP filters
        `Read in Mattermost API docs (ip - GetIPFilters) <https://developers.mattermost.com/api-documentation/#/operations/GetIPFilters>`_

        """
        return self.client.get("""/api/v4/ip_filtering""")

    def apply_ip_filters(self, options: list[Any]):
        """Get all IP filters
        `Read in Mattermost API docs (ip - ApplyIPFilters) <https://developers.mattermost.com/api-documentation/#/operations/ApplyIPFilters>`_

        """
        return self.client.post("""/api/v4/ip_filtering""", options=options)

    def my_ip(self):
        """Get all IP filters
        `Read in Mattermost API docs (ip - MyIP) <https://developers.mattermost.com/api-documentation/#/operations/MyIP>`_

        """
        return self.client.get("""/api/v4/ip_filtering/my_ip""")
