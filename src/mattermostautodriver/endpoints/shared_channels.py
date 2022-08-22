from .base import Base


class SharedChannels(Base):
    def get_all_shared_channels(self, team_id, params=None):
        """Get all shared channels for team.

        team_id: Team Id
        page:
        per_page:
        """
        return self.client.get(f"/sharedchannels/{team_id}", params=params)

    def get_remote_cluster_info(self, remote_id):
        """Get remote cluster info by ID for user.

        remote_id: Remote Cluster GUID
        """
        return self.client.get(f"/sharedchannels/remote_info/{remote_id}")
