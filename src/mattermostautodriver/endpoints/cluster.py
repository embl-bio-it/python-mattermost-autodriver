from .base import Base


class Cluster(Base):

    def get_cluster_status(self):
        """Get cluster status
        `Read in Mattermost API docs (cluster - GetClusterStatus) <https://api.mattermost.com/#tag/cluster/operation/GetClusterStatus>`_

        """
        return self.client.get("""/api/v4/cluster/status""")
