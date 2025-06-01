from .base import Base
from typing import Any, BinaryIO


class Teams(Base):

    def create_team(self, name: str, display_name: str, type: str):
        """Create a team

        name: Unique handler for a team, will be present in the team URL
        display_name: Non-unique UI name for the team
        type: ``'O'`` for open, ``'I'`` for invite only

        `Read in Mattermost API docs (teams - CreateTeam) <https://api.mattermost.com/#tag/teams/operation/CreateTeam>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"name": name, "display_name": display_name, "type": type}
        return self.client.post("""/api/v4/teams""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_all_teams(
        self,
        page: int | None = 0,
        per_page: int | None = 60,
        include_total_count: bool | None = False,
        exclude_policy_constrained: bool | None = False,
    ):
        """Get teams

        page: The page to select.
        per_page: The number of teams per page.
        include_total_count: Appends a total count of returned teams inside the response object - ex: ``{ "teams": [], "total_count" : 0 }``.
        exclude_policy_constrained: If set to true, teams which are part of a data retention policy will be excluded. The ``sysconsole_read_compliance`` permission is required to use this parameter.
        *Minimum server version*: 5.35

        `Read in Mattermost API docs (teams - GetAllTeams) <https://api.mattermost.com/#tag/teams/operation/GetAllTeams>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "page": page,
            "per_page": per_page,
            "include_total_count": include_total_count,
            "exclude_policy_constrained": exclude_policy_constrained,
        }
        return self.client.get("""/api/v4/teams""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_team(self, team_id: str):
        """Get a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeam) <https://api.mattermost.com/#tag/teams/operation/GetTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}")

    def update_team(
        self,
        team_id: str,
        id: str,
        display_name: str,
        description: str,
        company_name: str,
        allowed_domains: str,
        invite_id: str,
        allow_open_invite: str,
    ):
        """Update a team

        team_id: Team GUID
        id:
        display_name:
        description:
        company_name:
        allowed_domains:
        invite_id:
        allow_open_invite:

        `Read in Mattermost API docs (teams - UpdateTeam) <https://api.mattermost.com/#tag/teams/operation/UpdateTeam>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "id": id,
            "display_name": display_name,
            "description": description,
            "company_name": company_name,
            "allowed_domains": allowed_domains,
            "invite_id": invite_id,
            "allow_open_invite": allow_open_invite,
        }
        return self.client.put(f"/api/v4/teams/{team_id}", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def soft_delete_team(self, team_id: str):
        """Delete a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - SoftDeleteTeam) <https://api.mattermost.com/#tag/teams/operation/SoftDeleteTeam>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}")

    def patch_team(
        self,
        team_id: str,
        display_name: str | None = None,
        description: str | None = None,
        company_name: str | None = None,
        invite_id: str | None = None,
        allow_open_invite: bool | None = None,
    ):
        """Patch a team

        team_id: Team GUID
        display_name:
        description:
        company_name:
        invite_id:
        allow_open_invite:

        `Read in Mattermost API docs (teams - PatchTeam) <https://api.mattermost.com/#tag/teams/operation/PatchTeam>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "display_name": display_name,
            "description": description,
            "company_name": company_name,
            "invite_id": invite_id,
            "allow_open_invite": allow_open_invite,
        }
        return self.client.put(f"/api/v4/teams/{team_id}/patch", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def update_team_privacy(self, team_id: str, privacy: str):
        """Update teams's privacy

        team_id: Team GUID
        privacy: Team privacy setting: 'O' for a public (open) team, 'I' for a private (invitation only) team

        `Read in Mattermost API docs (teams - UpdateTeamPrivacy) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamPrivacy>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"privacy": privacy}
        return self.client.put(f"/api/v4/teams/{team_id}/privacy", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def restore_team(self, team_id: str):
        """Restore a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RestoreTeam) <https://api.mattermost.com/#tag/teams/operation/RestoreTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/restore")

    def get_team_by_name(self, name: str):
        """Get a team by name

        name: Team Name

        `Read in Mattermost API docs (teams - GetTeamByName) <https://api.mattermost.com/#tag/teams/operation/GetTeamByName>`_

        """
        return self.client.get(f"/api/v4/teams/name/{name}")

    def search_teams(
        self,
        term: str | None = None,
        page: str | None = None,
        per_page: str | None = None,
        allow_open_invite: bool | None = None,
        group_constrained: bool | None = None,
        exclude_policy_constrained: bool | None = False,
    ):
        """Search teams

        term: The search term to match against the name or display name of teams
        page: The page number to return, if paginated. If this parameter is not present with the ``per_page`` parameter then the results will be returned un-paged.
        per_page: The number of entries to return per page, if paginated. If this parameter is not present with the ``page`` parameter then the results will be returned un-paged.
        allow_open_invite: Filters results to teams where ``allow_open_invite`` is set to true or false, excludes group constrained channels if this filter option is passed.
        If this filter option is not passed then the query will remain unchanged.
        *Minimum server version*: 5.28

        group_constrained: Filters results to teams where ``group_constrained`` is set to true or false, returns the union of results when used with ``allow_open_invite``
        If the filter option is not passed then the query will remain unchanged.
        *Minimum server version*: 5.28

        exclude_policy_constrained: If set to true, only teams which do not have a granular retention policy assigned to them will be returned. The ``sysconsole_read_compliance_data_retention`` permission is required to use this parameter.
        *Minimum server version*: 5.35


        `Read in Mattermost API docs (teams - SearchTeams) <https://api.mattermost.com/#tag/teams/operation/SearchTeams>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "term": term,
            "page": page,
            "per_page": per_page,
            "allow_open_invite": allow_open_invite,
            "group_constrained": group_constrained,
            "exclude_policy_constrained": exclude_policy_constrained,
        }
        return self.client.post("""/api/v4/teams/search""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def team_exists(self, name: str):
        """Check if team exists

        name: Team Name

        `Read in Mattermost API docs (teams - TeamExists) <https://api.mattermost.com/#tag/teams/operation/TeamExists>`_

        """
        return self.client.get(f"/api/v4/teams/name/{name}/exists")

    def get_teams_for_user(self, user_id: str):
        """Get a user's teams

        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamsForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamsForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams")

    def get_team_members(
        self,
        team_id: str,
        page: int | None = 0,
        per_page: int | None = 60,
        sort: str | None = "",
        exclude_deleted_users: bool | None = False,
    ):
        """Get team members

        team_id: Team GUID
        page: The page to select.
        per_page: The number of users per page.
        sort: To sort by Username, set to 'Username', otherwise sort is by 'UserID'
        exclude_deleted_users: Excludes deleted users from the results

        `Read in Mattermost API docs (teams - GetTeamMembers) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembers>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "exclude_deleted_users": exclude_deleted_users,
        }
        return self.client.get(f"/api/v4/teams/{team_id}/members", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def add_team_member(self, team_id: str, team_id: str | None = None, user_id: str | None = None):
        """Add user to team

        team_id: Team GUID
        team_id:
        user_id:

        `Read in Mattermost API docs (teams - AddTeamMember) <https://api.mattermost.com/#tag/teams/operation/AddTeamMember>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"team_id": team_id, "user_id": user_id}
        return self.client.post(f"/api/v4/teams/{team_id}/members", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def add_team_member_from_invite(self):
        """Add user to team from invite
        `Read in Mattermost API docs (teams - AddTeamMemberFromInvite) <https://api.mattermost.com/#tag/teams/operation/AddTeamMemberFromInvite>`_

        """
        return self.client.post("""/api/v4/teams/members/invite""")

    def add_team_members(self, team_id: str, options: list[Any]):
        """Add multiple users to team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - AddTeamMembers) <https://api.mattermost.com/#tag/teams/operation/AddTeamMembers>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/members/batch", options=options)

    def get_team_members_for_user(self, user_id: str):
        """Get team members for a user

        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamMembersForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembersForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/members")

    def get_team_member(self, team_id: str, user_id: str):
        """Get a team member

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamMember) <https://api.mattermost.com/#tag/teams/operation/GetTeamMember>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/members/{user_id}")

    def remove_team_member(self, team_id: str, user_id: str):
        """Remove user from team

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (teams - RemoveTeamMember) <https://api.mattermost.com/#tag/teams/operation/RemoveTeamMember>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}/members/{user_id}")

    def get_team_members_by_ids(self, team_id: str, options: list[str]):
        """Get team members by ids

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamMembersByIds) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembersByIds>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/members/ids", options=options)

    def get_team_stats(self, team_id: str):
        """Get a team stats

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamStats) <https://api.mattermost.com/#tag/teams/operation/GetTeamStats>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/stats")

    def regenerate_team_invite_id(self, team_id: str):
        """Regenerate the Invite ID from a Team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RegenerateTeamInviteId) <https://api.mattermost.com/#tag/teams/operation/RegenerateTeamInviteId>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/regenerate_invite_id")

    def get_team_icon(self, team_id: str):
        """Get the team icon

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamIcon) <https://api.mattermost.com/#tag/teams/operation/GetTeamIcon>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/image")

    def set_team_icon(self, team_id: str, image: BinaryIO):
        """Sets the team icon

        team_id: Team GUID
        image: The image to be uploaded

        `Read in Mattermost API docs (teams - SetTeamIcon) <https://api.mattermost.com/#tag/teams/operation/SetTeamIcon>`_

        """
        files_71f8b7431cd64fcfa0dabd300d0636d2 = {"image": image}
        return self.client.post(f"/api/v4/teams/{team_id}/image", files=files_71f8b7431cd64fcfa0dabd300d0636d2)

    def remove_team_icon(self, team_id: str):
        """Remove the team icon

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RemoveTeamIcon) <https://api.mattermost.com/#tag/teams/operation/RemoveTeamIcon>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}/image")

    def update_team_member_roles(self, team_id: str, user_id: str, roles: str):
        """Update a team member roles

        team_id: Team GUID
        user_id: User GUID
        roles:

        `Read in Mattermost API docs (teams - UpdateTeamMemberRoles) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamMemberRoles>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"roles": roles}
        return self.client.put(
            f"/api/v4/teams/{team_id}/members/{user_id}/roles", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def update_team_member_scheme_roles(self, team_id: str, user_id: str, scheme_admin: bool, scheme_user: bool):
        """Update the scheme-derived roles of a team member.

        team_id: Team GUID
        user_id: User GUID
        scheme_admin:
        scheme_user:

        `Read in Mattermost API docs (teams - UpdateTeamMemberSchemeRoles) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamMemberSchemeRoles>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"scheme_admin": scheme_admin, "scheme_user": scheme_user}
        return self.client.put(
            f"/api/v4/teams/{team_id}/members/{user_id}/schemeRoles", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def get_teams_unread_for_user(
        self, user_id: str, exclude_team: str, include_collapsed_threads: bool | None = False
    ):
        """Get team unreads for a user

        user_id: User GUID
        exclude_team: Optional team id to be excluded from the results
        include_collapsed_threads: Boolean to determine whether the collapsed threads should be included or not

        `Read in Mattermost API docs (teams - GetTeamsUnreadForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamsUnreadForUser>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "exclude_team": exclude_team,
            "include_collapsed_threads": include_collapsed_threads,
        }
        return self.client.get(f"/api/v4/users/{user_id}/teams/unread", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_team_unread(self, user_id: str, team_id: str):
        """Get unreads for a team

        user_id: User GUID
        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamUnread) <https://api.mattermost.com/#tag/teams/operation/GetTeamUnread>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/unread")

    def invite_users_to_team(self, team_id: str, options: list[str]):
        """Invite users to the team by email

        team_id: Team GUID

        `Read in Mattermost API docs (teams - InviteUsersToTeam) <https://api.mattermost.com/#tag/teams/operation/InviteUsersToTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/invite/email", options=options)

    def invite_guests_to_team(self, team_id: str, emails: list[str], channels: list[str], message: str | None = None):
        """Invite guests to the team by email

        team_id: Team GUID
        emails: List of emails
        channels: List of channel ids
        message: Message to include in the invite

        `Read in Mattermost API docs (teams - InviteGuestsToTeam) <https://api.mattermost.com/#tag/teams/operation/InviteGuestsToTeam>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"emails": emails, "channels": channels, "message": message}
        return self.client.post(
            f"/api/v4/teams/{team_id}/invite-guests/email", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def invalidate_email_invites(self):
        """Invalidate active email invitations
        `Read in Mattermost API docs (teams - InvalidateEmailInvites) <https://api.mattermost.com/#tag/teams/operation/InvalidateEmailInvites>`_

        """
        return self.client.delete("""/api/v4/teams/invites/email""")

    def import_team(self, team_id: str, file: BinaryIO, filesize: int, importFrom: str):
        """Import a Team from other application

        team_id: Team GUID
        file: A file to be uploaded in zip format.
        filesize: The size of the zip file to be imported.
        importFrom: String that defines from which application the team was exported to be imported into Mattermost.

        `Read in Mattermost API docs (teams - ImportTeam) <https://api.mattermost.com/#tag/teams/operation/ImportTeam>`_

        """
        files_71f8b7431cd64fcfa0dabd300d0636d2 = {"file": file}
        data_71f8b7431cd64fcfa0dabd300d0636d2 = {"filesize": filesize, "importFrom": importFrom}
        return self.client.post(
            f"/api/v4/teams/{team_id}/import",
            files=files_71f8b7431cd64fcfa0dabd300d0636d2,
            data=data_71f8b7431cd64fcfa0dabd300d0636d2,
        )

    def get_team_invite_info(self, invite_id: str):
        """Get invite info for a team

        invite_id: Invite id for a team

        `Read in Mattermost API docs (teams - GetTeamInviteInfo) <https://api.mattermost.com/#tag/teams/operation/GetTeamInviteInfo>`_

        """
        return self.client.get(f"/api/v4/teams/invite/{invite_id}")

    def update_team_scheme(self, team_id: str, scheme_id: str):
        """Set a team's scheme

        team_id: Team GUID
        scheme_id: The ID of the scheme.

        `Read in Mattermost API docs (teams - UpdateTeamScheme) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamScheme>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"scheme_id": scheme_id}
        return self.client.put(f"/api/v4/teams/{team_id}/scheme", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def team_members_minus_group_members(
        self, team_id: str, group_ids: str = "", page: int | None = 0, per_page: int | None = 0
    ):
        """Team members minus group members.

        team_id: Team GUID
        group_ids: A comma-separated list of group ids.
        page: The page to select.
        per_page: The number of users per page.

        `Read in Mattermost API docs (teams - TeamMembersMinusGroupMembers) <https://api.mattermost.com/#tag/teams/operation/TeamMembersMinusGroupMembers>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"group_ids": group_ids, "page": page, "per_page": per_page}
        return self.client.get(
            f"/api/v4/teams/{team_id}/members_minus_group_members", params=params_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def search_files(
        self,
        team_id: str,
        terms: str,
        is_or_search: bool,
        time_zone_offset: int | None = 0,
        include_deleted_channels: bool | None = None,
        page: int | None = 0,
        per_page: int | None = 60,
    ):
        """Search files in a team

        team_id: Team GUID
        terms: The search terms as inputed by the user. To search for files from a user include ``from:someusername``, using a user's username. To search in a specific channel include ``in:somechannel``, using the channel name (not the display name). To search for specific extensions include ``ext:extension``.
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)

        `Read in Mattermost API docs (teams - SearchFiles) <https://api.mattermost.com/#tag/teams/operation/SearchFiles>`_

        """
        data_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "terms": terms,
            "is_or_search": is_or_search,
            "time_zone_offset": time_zone_offset,
            "include_deleted_channels": include_deleted_channels,
            "page": page,
            "per_page": per_page,
        }
        return self.client.post(f"/api/v4/teams/{team_id}/files/search", data=data_71f8b7431cd64fcfa0dabd300d0636d2)
