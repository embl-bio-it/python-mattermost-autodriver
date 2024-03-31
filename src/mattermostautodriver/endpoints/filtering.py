from .base import Base


class Filtering(Base):

    def get_ip_filters(self):
        """Get all IP filters
        `Read in Mattermost API docs (filtering - GetIPFilters) <https://api.mattermost.com/#tag/filtering/operation/GetIPFilters>`_

        """
        return self.client.get("""/api/v4/ip_filtering""")

    def apply_ip_filters(self, options):
        """Get all IP filters
        `Read in Mattermost API docs (filtering - ApplyIPFilters) <https://api.mattermost.com/#tag/filtering/operation/ApplyIPFilters>`_

        """
        return self.client.post("""/api/v4/ip_filtering""", options=options)

    def my_ip(self):
        """Get all IP filters
        `Read in Mattermost API docs (filtering - MyIP) <https://api.mattermost.com/#tag/filtering/operation/MyIP>`_

        """
        return self.client.get("""/api/v4/ip_filtering/my_ip""")
