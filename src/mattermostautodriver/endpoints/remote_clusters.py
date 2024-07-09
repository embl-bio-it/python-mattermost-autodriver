from .base import Base


class RemoteClusters(Base):

    def get_remote_clusters(self, params=None):
        """Get a list of remote clusters.

        page: The page to select
        per_page: The number of remote clusters per page
        exclude_offline: Exclude offline remote clusters
        in_channel: Select remote clusters in channel
        not_in_channel: Select remote clusters not in this channel
        only_confirmed: Select only remote clusters already confirmed
        only_plugins: Select only remote clusters that belong to a plugin
        exclude_plugins: Select only remote clusters that don't belong to a plugin

        `Read in Mattermost API docs (remote_clusters - GetRemoteClusters) <https://api.mattermost.com/#tag/remote_clusters/operation/GetRemoteClusters>`_

        """
        return self.client.get("""/api/v4/remotecluster""", params=params)

    def create_remote_cluster(self, options=None):
        """Create a new remote cluster.

        name:
        display_name:
        password: The password to use in the invite code.

        `Read in Mattermost API docs (remote_clusters - CreateRemoteCluster) <https://api.mattermost.com/#tag/remote_clusters/operation/CreateRemoteCluster>`_

        """
        return self.client.post("""/api/v4/remotecluster""", options=options)

    def get_remote_cluster(self, remote_id):
        """Get a remote cluster.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (remote_clusters - GetRemoteCluster) <https://api.mattermost.com/#tag/remote_clusters/operation/GetRemoteCluster>`_

        """
        return self.client.get(f"/api/v4/remotecluster/{remote_id}")

    def patch_remote_cluster(self, remote_id, options=None):
        """Patch a remote cluster.

        remote_id: Remote Cluster GUID
        display_name:

        `Read in Mattermost API docs (remote_clusters - PatchRemoteCluster) <https://api.mattermost.com/#tag/remote_clusters/operation/PatchRemoteCluster>`_

        """
        return self.client.patch(f"/api/v4/remotecluster/{remote_id}", options=options)

    def delete_remote_cluster(self, remote_id):
        """Delete a remote cluster.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (remote_clusters - DeleteRemoteCluster) <https://api.mattermost.com/#tag/remote_clusters/operation/DeleteRemoteCluster>`_

        """
        return self.client.delete(f"/api/v4/remotecluster/{remote_id}")

    def generate_remote_cluster_invite(self, options=None):
        """Generate invite code.

        password: The password to encrypt the invite code with.

        `Read in Mattermost API docs (remote_clusters - GenerateRemoteClusterInvite) <https://api.mattermost.com/#tag/remote_clusters/operation/GenerateRemoteClusterInvite>`_

        """
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/generate_invite", options=options)

    def accept_remote_cluster_invite(self, options=None):
        """Accept a remote cluster invite code.

        invite:
        name:
        display_name:
        password: The password to decrypt the invite code.

        `Read in Mattermost API docs (remote_clusters - AcceptRemoteClusterInvite) <https://api.mattermost.com/#tag/remote_clusters/operation/AcceptRemoteClusterInvite>`_

        """
        return self.client.post("""/api/v4/remotecluster/accept_invite""", options=options)
