from ._base import Base
from typing import Any, BinaryIO

__all__ = ["RemoteClusters"]


class RemoteClusters(Base):

    def get_remote_clusters(
        self,
        page: int | None = None,
        per_page: int | None = None,
        exclude_offline: bool | None = None,
        in_channel: str | None = None,
        not_in_channel: str | None = None,
        only_confirmed: bool | None = None,
        only_plugins: bool | None = None,
        exclude_plugins: bool | None = None,
        include_deleted: bool | None = None,
    ):
        """Get a list of remote clusters.

        page: The page to select
        per_page: The number of remote clusters per page
        exclude_offline: Exclude offline remote clusters
        in_channel: Select remote clusters in channel
        not_in_channel: Select remote clusters not in this channel
        only_confirmed: Select only remote clusters already confirmed
        only_plugins: Select only remote clusters that belong to a plugin
        exclude_plugins: Select only remote clusters that don't belong to a plugin
        include_deleted: Include those remote clusters that have been deleted

        `Read in Mattermost API docs (remote_clusters - GetRemoteClusters) <https://developers.mattermost.com/api-documentation/#/operations/GetRemoteClusters>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "exclude_offline": exclude_offline,
            "in_channel": in_channel,
            "not_in_channel": not_in_channel,
            "only_confirmed": only_confirmed,
            "only_plugins": only_plugins,
            "exclude_plugins": exclude_plugins,
            "include_deleted": include_deleted,
        }
        return self.client.get("""/api/v4/remotecluster""", params=__params)

    def create_remote_cluster(
        self, name: str, default_team_id: str, display_name: str | None = None, password: str | None = None
    ):
        """Create a new remote cluster.

        name:
        display_name:
        default_team_id:
        password: The password to use in the invite code. If empty,
        the server will generate one and it will be part
        of the response


        `Read in Mattermost API docs (remote_clusters - CreateRemoteCluster) <https://developers.mattermost.com/api-documentation/#/operations/CreateRemoteCluster>`_

        """
        __options = {
            "name": name,
            "display_name": display_name,
            "default_team_id": default_team_id,
            "password": password,
        }
        return self.client.post("""/api/v4/remotecluster""", options=__options)

    def get_remote_cluster(self, remote_id: str):
        """Get a remote cluster.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (remote_clusters - GetRemoteCluster) <https://developers.mattermost.com/api-documentation/#/operations/GetRemoteCluster>`_

        """
        return self.client.get(f"/api/v4/remotecluster/{remote_id}")

    def patch_remote_cluster(self, remote_id: str, display_name: str | None = None, default_team_id: str | None = None):
        """Patch a remote cluster.

        remote_id: Remote Cluster GUID
        display_name:
        default_team_id: The team where channels from invites are created

        `Read in Mattermost API docs (remote_clusters - PatchRemoteCluster) <https://developers.mattermost.com/api-documentation/#/operations/PatchRemoteCluster>`_

        """
        __options = {"display_name": display_name, "default_team_id": default_team_id}
        return self.client.patch(f"/api/v4/remotecluster/{remote_id}", options=__options)

    def delete_remote_cluster(self, remote_id: str):
        """Delete a remote cluster.

        remote_id: Remote Cluster GUID

        `Read in Mattermost API docs (remote_clusters - DeleteRemoteCluster) <https://developers.mattermost.com/api-documentation/#/operations/DeleteRemoteCluster>`_

        """
        return self.client.delete(f"/api/v4/remotecluster/{remote_id}")

    def generate_remote_cluster_invite(self, password: str):
        """Generate invite code.

        password: The password to encrypt the invite code with.

        `Read in Mattermost API docs (remote_clusters - GenerateRemoteClusterInvite) <https://developers.mattermost.com/api-documentation/#/operations/GenerateRemoteClusterInvite>`_

        """
        __options = {"password": password}
        return self.client.post(f"/api/v4/remotecluster/{remote_id}/generate_invite", options=__options)

    def accept_remote_cluster_invite(
        self, invite: str, name: str, default_team_id: str, password: str, display_name: str | None = None
    ):
        """Accept a remote cluster invite code.

        invite:
        name:
        display_name:
        default_team_id:
        password: The password to decrypt the invite code.

        `Read in Mattermost API docs (remote_clusters - AcceptRemoteClusterInvite) <https://developers.mattermost.com/api-documentation/#/operations/AcceptRemoteClusterInvite>`_

        """
        __options = {
            "invite": invite,
            "name": name,
            "display_name": display_name,
            "default_team_id": default_team_id,
            "password": password,
        }
        return self.client.post("""/api/v4/remotecluster/accept_invite""", options=__options)
