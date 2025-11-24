from ._base import Base

__all__ = ["SharedChannels"]


class SharedChannels(Base):

    def get_shared_channel_remotes(self, channel_id):
        """Get remote clusters for a shared channel

        channel_id: Channel GUID

        `Read in Mattermost API docs (shared_channels - GetSharedChannelRemotes) <https://developers.mattermost.com/api-documentation/#/operations/GetSharedChannelRemotes>`_

        """
        return self.client.get(f"/api/v4/sharedchannels/{channel_id}/remotes")

    def get_all_shared_channels(self, team_id, params=None):
        """Get all shared channels for team.

        team_id: Team Id
        page: The page to select.
        per_page: The number of sharedchannels per page.

        `Read in Mattermost API docs (shared_channels - GetAllSharedChannels) <https://developers.mattermost.com/api-documentation/#/operations/GetAllSharedChannels>`_

        """
        return self.client.get(f"/api/v4/sharedchannels/{team_id}", params=params)

    def get_shared_channel_remotes_by_remote_cluster(self, remote_id, params=None):
        """Get shared channel remotes by remote cluster.

        remote_id: The remote cluster GUID
        include_unconfirmed: Include those Shared channel remotes that are unconfirmed
        exclude_confirmed: Show only those Shared channel remotes that are not confirmed yet
        exclude_home: Show only those Shared channel remotes that were shared with this server
        exclude_remote: Show only those Shared channel remotes that were shared from this server
        include_deleted: Include those Shared channel remotes that have been deleted
        page: The page to select
        per_page: The number of shared channels per page

        `Read in Mattermost API docs (shared_channels - GetSharedChannelRemotesByRemoteCluster) <https://developers.mattermost.com/api-documentation/#/operations/GetSharedChannelRemotesByRemoteCluster>`_

        """
        return self.client.get(f"/api/v4/remotecluster/{remote_id}/sharedchannelremotes", params=params)

    def get_remote_cluster_info(self, remote_id):
        """Get remote cluster info by ID for user.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (shared_channels - GetRemoteClusterInfo) <https://developers.mattermost.com/api-documentation/#/operations/GetRemoteClusterInfo>`_

        """
        return self.client.get(f"/api/v4/sharedchannels/remote_info/{remote_id}")

    def invite_remote_cluster_to_channel(self, remote_id, channel_id):
        """Invites a remote cluster to a channel.

        remote_id: The remote cluster GUID
        channel_id: The channel GUID to invite the remote cluster to

        `Read in Mattermost API docs (shared_channels - InviteRemoteClusterToChannel) <https://developers.mattermost.com/api-documentation/#/operations/InviteRemoteClusterToChannel>`_

        """
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/invite")

    def uninvite_remote_cluster_to_channel(self, remote_id, channel_id):
        """Uninvites a remote cluster to a channel.

        remote_id: The remote cluster GUID
        channel_id: The channel GUID to uninvite the remote cluster to

        `Read in Mattermost API docs (shared_channels - UninviteRemoteClusterToChannel) <https://developers.mattermost.com/api-documentation/#/operations/UninviteRemoteClusterToChannel>`_

        """
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/channels/{channel_id}/uninvite")

    def can_user_direct_message(self, user_id, other_user_id):
        """Check if user can DM another user in shared channels context

        user_id: User GUID
        other_user_id: Other user GUID

        `Read in Mattermost API docs (shared_channels - CanUserDirectMessage) <https://developers.mattermost.com/api-documentation/#/operations/CanUserDirectMessage>`_

        """
        return self.client.get(f"/api/v4/sharedchannels/users/{user_id}/can_dm/{other_user_id}")
