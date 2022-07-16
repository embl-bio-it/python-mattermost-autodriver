from .base import Base


class Cluster(Base):
    def get_cluster_status(self):
        """Get cluster status"""
        return self.client.get("""/cluster/status""")
