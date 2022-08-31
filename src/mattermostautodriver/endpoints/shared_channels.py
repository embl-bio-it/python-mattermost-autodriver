from .base import Base


class SharedChannels(Base):
    def get_all_shared_channels(self, team_id, params=None):
        """Get all shared channels for team.

        team_id: Team Id
        page: The page to select.
        per_page: The number of sharedchannels per page.

        `Read in Mattermost API docs (shared_channels - GetAllSharedChannels) <https://api.mattermost.com/#tag/shared_channels/operation/GetAllSharedChannels>`_
        """
        return self.client.get(f"/sharedchannels/{team_id}", params=params)

    def get_remote_cluster_info(self, remote_id):
        """Get remote cluster info by ID for user.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (shared_channels - GetRemoteClusterInfo) <https://api.mattermost.com/#tag/shared_channels/operation/GetRemoteClusterInfo>`_
        """
        return self.client.get(f"/sharedchannels/remote_info/{remote_id}")
