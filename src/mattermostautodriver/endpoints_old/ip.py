from ._base import Base

__all__ = ["Ip"]


class Ip(Base):

    def get_ip_filters(self):
        """Get all IP filters
        `Read in Mattermost API docs (ip - GetIPFilters) <https://api.mattermost.com/#tag/ip/operation/GetIPFilters>`_

        """
        return self.client.get("""/api/v4/ip_filtering""")

    def apply_ip_filters(self, options):
        """Get all IP filters
        `Read in Mattermost API docs (ip - ApplyIPFilters) <https://api.mattermost.com/#tag/ip/operation/ApplyIPFilters>`_

        """
        return self.client.post("""/api/v4/ip_filtering""", options=options)

    def my_ip(self):
        """Get all IP filters
        `Read in Mattermost API docs (ip - MyIP) <https://api.mattermost.com/#tag/ip/operation/MyIP>`_

        """
        return self.client.get("""/api/v4/ip_filtering/my_ip""")
