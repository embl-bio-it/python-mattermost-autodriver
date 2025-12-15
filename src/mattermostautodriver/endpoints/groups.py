from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Groups"]


class Groups(Base):

    def unlink_ldap_group(self, remote_id: str):
        """Delete a link for LDAP group

        remote_id: Group GUID

        `Read in Mattermost API docs (groups - UnlinkLdapGroup) <https://developers.mattermost.com/api-documentation/#/operations/UnlinkLdapGroup>`_

        """
        return self.client.delete(f"/api/v4/ldap/groups/{remote_id}/link")

    def get_groups(
        self,
        page: int | None = 0,
        per_page: int | None = 60,
        q: str | None = None,
        include_member_count: bool | None = None,
        not_associated_to_team: str | None = None,
        not_associated_to_channel: str | None = None,
        since: int | None = None,
        filter_allow_reference: bool | None = False,
    ):
        """Get groups

        page: The page to select.
        per_page: The number of groups per page.
        q: String to pattern match the ``name`` and ``display_name`` field. Will return all groups whose ``name`` and ``display_name`` field match any of the text.
        include_member_count: Boolean which adds the ``member_count`` attribute to each group JSON object
        not_associated_to_team: Team GUID which is used to return all the groups not associated to this team
        not_associated_to_channel: Group GUID which is used to return all the groups not associated to this channel
        since: Only return groups that have been modified since the given Unix timestamp (in milliseconds). All modified groups, including deleted and created groups, will be returned.
        *Minimum server version*: 5.24

        filter_allow_reference: Boolean which filters the group entries with the ``allow_reference`` attribute set.

        `Read in Mattermost API docs (groups - GetGroups) <https://developers.mattermost.com/api-documentation/#/operations/GetGroups>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "q": q,
            "include_member_count": include_member_count,
            "not_associated_to_team": not_associated_to_team,
            "not_associated_to_channel": not_associated_to_channel,
            "since": since,
            "filter_allow_reference": filter_allow_reference,
        }
        return self.client.get("""/api/v4/groups""", params=__params)

    def create_group(self, name: str, display_name: str, source: str, allow_reference: bool, user_ids: list[str]):
        """Create a custom group

        name: The unique group name used for at-mentioning.
        display_name: The display name of the group which can include spaces.
        source: Must be ``custom``
        allow_reference: Must be true
        user_ids: The user ids of the group members to add.

        `Read in Mattermost API docs (groups - CreateGroup) <https://developers.mattermost.com/api-documentation/#/operations/CreateGroup>`_

        """
        __options = {
            "name": name,
            "display_name": display_name,
            "source": source,
            "allow_reference": allow_reference,
            "user_ids": user_ids,
        }
        return self.client.post("""/api/v4/groups""", options=__options)

    def get_group(self, group_id: str):
        """Get a group

        group_id: Group GUID

        `Read in Mattermost API docs (groups - GetGroup) <https://developers.mattermost.com/api-documentation/#/operations/GetGroup>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}")

    def delete_group(self, group_id: str):
        """Deletes a custom group

        group_id: The ID of the group.

        `Read in Mattermost API docs (groups - DeleteGroup) <https://developers.mattermost.com/api-documentation/#/operations/DeleteGroup>`_

        """
        return self.client.delete(f"/api/v4/groups/{group_id}")

    def patch_group(
        self, group_id: str, name: str | None = None, display_name: str | None = None, description: str | None = None
    ):
        """Patch a group

        group_id: Group GUID
        name:
        display_name:
        description:

        `Read in Mattermost API docs (groups - PatchGroup) <https://developers.mattermost.com/api-documentation/#/operations/PatchGroup>`_

        """
        __options = {"name": name, "display_name": display_name, "description": description}
        return self.client.put(f"/api/v4/groups/{group_id}/patch", options=__options)

    def restore_group(self, group_id: str):
        """Restore a previously deleted group.

        group_id: Group GUID

        `Read in Mattermost API docs (groups - RestoreGroup) <https://developers.mattermost.com/api-documentation/#/operations/RestoreGroup>`_

        """
        return self.client.post(f"/api/v4/groups/{group_id}/restore")

    def link_group_syncable_for_team(self, group_id: str, team_id: str):
        """Link a team to a group

        group_id: Group GUID
        team_id: Team GUID

        `Read in Mattermost API docs (groups - LinkGroupSyncableForTeam) <https://developers.mattermost.com/api-documentation/#/operations/LinkGroupSyncableForTeam>`_

        """
        return self.client.post(f"/api/v4/groups/{group_id}/teams/{team_id}/link")

    def unlink_group_syncable_for_team(self, group_id: str, team_id: str):
        """Delete a link from a team to a group

        group_id: Group GUID
        team_id: Team GUID

        `Read in Mattermost API docs (groups - UnlinkGroupSyncableForTeam) <https://developers.mattermost.com/api-documentation/#/operations/UnlinkGroupSyncableForTeam>`_

        """
        return self.client.delete(f"/api/v4/groups/{group_id}/teams/{team_id}/link")

    def link_group_syncable_for_channel(self, group_id: str, channel_id: str):
        """Link a channel to a group

        group_id: Group GUID
        channel_id: Channel GUID

        `Read in Mattermost API docs (groups - LinkGroupSyncableForChannel) <https://developers.mattermost.com/api-documentation/#/operations/LinkGroupSyncableForChannel>`_

        """
        return self.client.post(f"/api/v4/groups/{group_id}/channels/{channel_id}/link")

    def unlink_group_syncable_for_channel(self, group_id: str, channel_id: str):
        """Delete a link from a channel to a group

        group_id: Group GUID
        channel_id: Channel GUID

        `Read in Mattermost API docs (groups - UnlinkGroupSyncableForChannel) <https://developers.mattermost.com/api-documentation/#/operations/UnlinkGroupSyncableForChannel>`_

        """
        return self.client.delete(f"/api/v4/groups/{group_id}/channels/{channel_id}/link")

    def get_group_syncable_for_team_id(self, group_id: str, team_id: str):
        """Get GroupSyncable from Team ID

        group_id: Group GUID
        team_id: Team GUID

        `Read in Mattermost API docs (groups - GetGroupSyncableForTeamId) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupSyncableForTeamId>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}/teams/{team_id}")

    def get_group_syncable_for_channel_id(self, group_id: str, channel_id: str):
        """Get GroupSyncable from channel ID

        group_id: Group GUID
        channel_id: Channel GUID

        `Read in Mattermost API docs (groups - GetGroupSyncableForChannelId) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupSyncableForChannelId>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}/channels/{channel_id}")

    def get_group_syncables_teams(self, group_id: str):
        """Get group teams

        group_id: Group GUID

        `Read in Mattermost API docs (groups - GetGroupSyncablesTeams) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupSyncablesTeams>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}/teams")

    def get_group_syncables_channels(self, group_id: str):
        """Get group channels

        group_id: Group GUID

        `Read in Mattermost API docs (groups - GetGroupSyncablesChannels) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupSyncablesChannels>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}/channels")

    def patch_group_syncable_for_team(self, group_id: str, team_id: str, auto_add: bool | None = None):
        """Patch a GroupSyncable associated to Team

        group_id: Group GUID
        team_id: Team GUID
        auto_add:

        `Read in Mattermost API docs (groups - PatchGroupSyncableForTeam) <https://developers.mattermost.com/api-documentation/#/operations/PatchGroupSyncableForTeam>`_

        """
        __options = {"auto_add": auto_add}
        return self.client.put(f"/api/v4/groups/{group_id}/teams/{team_id}/patch", options=__options)

    def patch_group_syncable_for_channel(self, group_id: str, channel_id: str, auto_add: bool | None = None):
        """Patch a GroupSyncable associated to Channel

        group_id: Group GUID
        channel_id: Channel GUID
        auto_add:

        `Read in Mattermost API docs (groups - PatchGroupSyncableForChannel) <https://developers.mattermost.com/api-documentation/#/operations/PatchGroupSyncableForChannel>`_

        """
        __options = {"auto_add": auto_add}
        return self.client.put(f"/api/v4/groups/{group_id}/channels/{channel_id}/patch", options=__options)

    def get_group_users(self, group_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get group users

        group_id: Group GUID
        page: The page to select.
        per_page: The number of groups per page.

        `Read in Mattermost API docs (groups - GetGroupUsers) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupUsers>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/groups/{group_id}/members", params=__params)

    def delete_group_members(self, group_id: str, user_ids: list[str] | None = None):
        """Removes members from a custom group

        group_id: The ID of the group to delete.
        user_ids:

        `Read in Mattermost API docs (groups - DeleteGroupMembers) <https://developers.mattermost.com/api-documentation/#/operations/DeleteGroupMembers>`_

        """
        __params = {"user_ids": user_ids}
        return self.client.delete(f"/api/v4/groups/{group_id}/members", params=__params)

    def add_group_members(self, group_id: str, user_ids: list[str] | None = None):
        """Adds members to a custom group

        group_id: The ID of the group.
        user_ids:

        `Read in Mattermost API docs (groups - AddGroupMembers) <https://developers.mattermost.com/api-documentation/#/operations/AddGroupMembers>`_

        """
        __options = {"user_ids": user_ids}
        return self.client.post(f"/api/v4/groups/{group_id}/members", options=__options)

    def get_group_stats(self, group_id: str):
        """Get group stats

        group_id: Group GUID

        `Read in Mattermost API docs (groups - GetGroupStats) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupStats>`_

        """
        return self.client.get(f"/api/v4/groups/{group_id}/stats")

    def get_groups_by_channel(
        self,
        channel_id: str,
        page: int | None = 0,
        per_page: int | None = 60,
        filter_allow_reference: bool | None = False,
    ):
        """Get channel groups

        channel_id: Channel GUID
        page: The page to select.
        per_page: The number of groups per page.
        filter_allow_reference: Boolean which filters the group entries with the ``allow_reference`` attribute set.

        `Read in Mattermost API docs (groups - GetGroupsByChannel) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupsByChannel>`_

        """
        __params = {"page": page, "per_page": per_page, "filter_allow_reference": filter_allow_reference}
        return self.client.get(f"/api/v4/channels/{channel_id}/groups", params=__params)

    def get_groups_by_team(
        self,
        team_id: str,
        page: int | None = 0,
        per_page: int | None = 60,
        filter_allow_reference: bool | None = False,
        include_member_count: bool | None = False,
        include_timezones: bool | None = False,
        include_total_count: bool | None = False,
        include_archived: bool | None = False,
        filter_archived: bool | None = False,
        filter_parent_team_permitted: bool | None = False,
        filter_has_member: str | None = None,
        include_member_ids: bool | None = False,
        only_syncable_sources: bool | None = False,
    ):
        """Get team groups

        team_id: Team GUID
        page: The page to select.
        per_page: The number of groups per page.
        filter_allow_reference: Boolean which filters in the group entries with the ``allow_reference`` attribute set.
        include_member_count: Boolean which adds a ``member_count`` field to each group object.
        include_timezones: Boolean which adds timezone information for group members.
        include_total_count: Boolean which adds total count of groups in the response.
        include_archived: Boolean which includes archived groups in the response.
        filter_archived: Boolean which filters out archived groups from the response.
        filter_parent_team_permitted: Boolean which filters groups based on parent team permissions.
        filter_has_member: User ID to filter groups that have this member.
        include_member_ids: Boolean which adds member IDs to the group objects.
        only_syncable_sources: Boolean which includes groups from syncable sources.

        `Read in Mattermost API docs (groups - GetGroupsByTeam) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupsByTeam>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "filter_allow_reference": filter_allow_reference,
            "include_member_count": include_member_count,
            "include_timezones": include_timezones,
            "include_total_count": include_total_count,
            "include_archived": include_archived,
            "filter_archived": filter_archived,
            "filter_parent_team_permitted": filter_parent_team_permitted,
            "filter_has_member": filter_has_member,
            "include_member_ids": include_member_ids,
            "only_syncable_sources": only_syncable_sources,
        }
        return self.client.get(f"/api/v4/teams/{team_id}/groups", params=__params)

    def get_groups_associated_to_channels_by_team(
        self,
        team_id: str,
        page: int | None = 0,
        per_page: int | None = 60,
        filter_allow_reference: bool | None = False,
        paginate: bool | None = False,
    ):
        """Get team groups by channels

        team_id: Team GUID
        page: The page to select.
        per_page: The number of groups per page.
        filter_allow_reference: Boolean which filters in the group entries with the ``allow_reference`` attribute set.
        paginate: Boolean to determine whether the pagination should be applied or not

        `Read in Mattermost API docs (groups - GetGroupsAssociatedToChannelsByTeam) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupsAssociatedToChannelsByTeam>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "filter_allow_reference": filter_allow_reference,
            "paginate": paginate,
        }
        return self.client.get(f"/api/v4/teams/{team_id}/groups_by_channels", params=__params)

    def get_groups_by_user_id(self, user_id: str):
        """Get groups for a userId

        user_id: User GUID

        `Read in Mattermost API docs (groups - GetGroupsByUserId) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupsByUserId>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/groups")

    def get_groups_by_names(self, options: list[str]):
        """Get groups by name
        `Read in Mattermost API docs (groups - GetGroupsByNames) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupsByNames>`_

        """
        return self.client.post("""/api/v4/groups/names""", options=options)
