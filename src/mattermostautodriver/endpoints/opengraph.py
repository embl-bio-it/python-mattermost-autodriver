from .base import Base


class OpenGraph(Base):
    def open_graph(self, options):
        """Get open graph metadata for url

        url: The URL to get Open Graph Metadata.

        `Read in Mattermost API docs (OpenGraph - OpenGraph) <https://api.mattermost.com/#tag/OpenGraph/operation/OpenGraph>`_
        """
        return self.client.post("""/api/v4/opengraph""", options=options)
