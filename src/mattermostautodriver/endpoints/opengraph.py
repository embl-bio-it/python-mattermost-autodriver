from .base import Base


class OpenGraph(Base):
    def open_graph(self, options):
        """Get open graph metadata for url

        url: The URL to get Open Graph Metadata.
        """
        return self.client.post("""/opengraph""", options=options)
