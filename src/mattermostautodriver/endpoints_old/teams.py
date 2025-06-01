from ._base import Base

__all__ = ["Teams"]


class Teams(Base):

    def create_team(self, options):
        """Create a team

        name: Unique handler for a team, will be present in the team URL
        display_name: Non-unique UI name for the team
        type: ``'O'`` for open, ``'I'`` for invite only

        `Read in Mattermost API docs (teams - CreateTeam) <https://api.mattermost.com/#tag/teams/operation/CreateTeam>`_

        """
        return self.client.post("""/api/v4/teams""", options=options)

    def get_all_teams(self, params=None):
        """Get teams

        page: The page to select.
        per_page: The number of teams per page.
        include_total_count: Appends a total count of returned teams inside the response object - ex: ``{ "teams": [], "total_count" : 0 }``.
        exclude_policy_constrained: If set to true, teams which are part of a data retention policy will be excluded. The ``sysconsole_read_compliance`` permission is required to use this parameter.
        *Minimum server version*: 5.35

        `Read in Mattermost API docs (teams - GetAllTeams) <https://api.mattermost.com/#tag/teams/operation/GetAllTeams>`_

        """
        return self.client.get("""/api/v4/teams""", params=params)

    def get_team(self, team_id):
        """Get a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeam) <https://api.mattermost.com/#tag/teams/operation/GetTeam>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}")

    def update_team(self, team_id, options):
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
        return self.client.put(f"/api/v4/teams/{team_id}", options=options)

    def soft_delete_team(self, team_id):
        """Delete a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - SoftDeleteTeam) <https://api.mattermost.com/#tag/teams/operation/SoftDeleteTeam>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}")

    def patch_team(self, team_id, options):
        """Patch a team

        team_id: Team GUID
        display_name:
        description:
        company_name:
        invite_id:
        allow_open_invite:

        `Read in Mattermost API docs (teams - PatchTeam) <https://api.mattermost.com/#tag/teams/operation/PatchTeam>`_

        """
        return self.client.put(f"/api/v4/teams/{team_id}/patch", options=options)

    def update_team_privacy(self, team_id, options):
        """Update teams's privacy

        team_id: Team GUID
        privacy: Team privacy setting: 'O' for a public (open) team, 'I' for a private (invitation only) team

        `Read in Mattermost API docs (teams - UpdateTeamPrivacy) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamPrivacy>`_

        """
        return self.client.put(f"/api/v4/teams/{team_id}/privacy", options=options)

    def restore_team(self, team_id):
        """Restore a team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RestoreTeam) <https://api.mattermost.com/#tag/teams/operation/RestoreTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/restore")

    def get_team_by_name(self, name):
        """Get a team by name

        name: Team Name

        `Read in Mattermost API docs (teams - GetTeamByName) <https://api.mattermost.com/#tag/teams/operation/GetTeamByName>`_

        """
        return self.client.get(f"/api/v4/teams/name/{name}")

    def search_teams(self, options):
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
        return self.client.post("""/api/v4/teams/search""", options=options)

    def team_exists(self, name):
        """Check if team exists

        name: Team Name

        `Read in Mattermost API docs (teams - TeamExists) <https://api.mattermost.com/#tag/teams/operation/TeamExists>`_

        """
        return self.client.get(f"/api/v4/teams/name/{name}/exists")

    def get_teams_for_user(self, user_id):
        """Get a user's teams

        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamsForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamsForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams")

    def get_team_members(self, team_id, params=None):
        """Get team members

        team_id: Team GUID
        page: The page to select.
        per_page: The number of users per page.
        sort: To sort by Username, set to 'Username', otherwise sort is by 'UserID'
        exclude_deleted_users: Excludes deleted users from the results

        `Read in Mattermost API docs (teams - GetTeamMembers) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembers>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/members", params=params)

    def add_team_member(self, team_id, options):
        """Add user to team

        team_id: Team GUID
        team_id:
        user_id:

        `Read in Mattermost API docs (teams - AddTeamMember) <https://api.mattermost.com/#tag/teams/operation/AddTeamMember>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/members", options=options)

    def add_team_member_from_invite(self):
        """Add user to team from invite
        `Read in Mattermost API docs (teams - AddTeamMemberFromInvite) <https://api.mattermost.com/#tag/teams/operation/AddTeamMemberFromInvite>`_

        """
        return self.client.post("""/api/v4/teams/members/invite""")

    def add_team_members(self, team_id, options):
        """Add multiple users to team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - AddTeamMembers) <https://api.mattermost.com/#tag/teams/operation/AddTeamMembers>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/members/batch", options=options)

    def get_team_members_for_user(self, user_id):
        """Get team members for a user

        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamMembersForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembersForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/members")

    def get_team_member(self, team_id, user_id):
        """Get a team member

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (teams - GetTeamMember) <https://api.mattermost.com/#tag/teams/operation/GetTeamMember>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/members/{user_id}")

    def remove_team_member(self, team_id, user_id):
        """Remove user from team

        team_id: Team GUID
        user_id: User GUID

        `Read in Mattermost API docs (teams - RemoveTeamMember) <https://api.mattermost.com/#tag/teams/operation/RemoveTeamMember>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}/members/{user_id}")

    def get_team_members_by_ids(self, team_id, options):
        """Get team members by ids

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamMembersByIds) <https://api.mattermost.com/#tag/teams/operation/GetTeamMembersByIds>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/members/ids", options=options)

    def get_team_stats(self, team_id):
        """Get a team stats

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamStats) <https://api.mattermost.com/#tag/teams/operation/GetTeamStats>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/stats")

    def regenerate_team_invite_id(self, team_id):
        """Regenerate the Invite ID from a Team

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RegenerateTeamInviteId) <https://api.mattermost.com/#tag/teams/operation/RegenerateTeamInviteId>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/regenerate_invite_id")

    def get_team_icon(self, team_id):
        """Get the team icon

        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamIcon) <https://api.mattermost.com/#tag/teams/operation/GetTeamIcon>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/image")

    def set_team_icon(self, team_id, files, data=None):
        """Sets the team icon

        team_id: Team GUID
        image: The image to be uploaded

        `Read in Mattermost API docs (teams - SetTeamIcon) <https://api.mattermost.com/#tag/teams/operation/SetTeamIcon>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/image", files=files, data=data)

    def remove_team_icon(self, team_id):
        """Remove the team icon

        team_id: Team GUID

        `Read in Mattermost API docs (teams - RemoveTeamIcon) <https://api.mattermost.com/#tag/teams/operation/RemoveTeamIcon>`_

        """
        return self.client.delete(f"/api/v4/teams/{team_id}/image")

    def update_team_member_roles(self, team_id, user_id, options):
        """Update a team member roles

        team_id: Team GUID
        user_id: User GUID
        roles:

        `Read in Mattermost API docs (teams - UpdateTeamMemberRoles) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamMemberRoles>`_

        """
        return self.client.put(f"/api/v4/teams/{team_id}/members/{user_id}/roles", options=options)

    def update_team_member_scheme_roles(self, team_id, user_id, options):
        """Update the scheme-derived roles of a team member.

        team_id: Team GUID
        user_id: User GUID
        scheme_admin:
        scheme_user:

        `Read in Mattermost API docs (teams - UpdateTeamMemberSchemeRoles) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamMemberSchemeRoles>`_

        """
        return self.client.put(f"/api/v4/teams/{team_id}/members/{user_id}/schemeRoles", options=options)

    def get_teams_unread_for_user(self, user_id, params=None):
        """Get team unreads for a user

        user_id: User GUID
        exclude_team: Optional team id to be excluded from the results
        include_collapsed_threads: Boolean to determine whether the collapsed threads should be included or not

        `Read in Mattermost API docs (teams - GetTeamsUnreadForUser) <https://api.mattermost.com/#tag/teams/operation/GetTeamsUnreadForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/unread", params=params)

    def get_team_unread(self, user_id, team_id):
        """Get unreads for a team

        user_id: User GUID
        team_id: Team GUID

        `Read in Mattermost API docs (teams - GetTeamUnread) <https://api.mattermost.com/#tag/teams/operation/GetTeamUnread>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/unread")

    def invite_users_to_team(self, team_id, options):
        """Invite users to the team by email

        team_id: Team GUID

        `Read in Mattermost API docs (teams - InviteUsersToTeam) <https://api.mattermost.com/#tag/teams/operation/InviteUsersToTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/invite/email", options=options)

    def invite_guests_to_team(self, team_id, options):
        """Invite guests to the team by email

        team_id: Team GUID
        emails: List of emails
        channels: List of channel ids
        message: Message to include in the invite

        `Read in Mattermost API docs (teams - InviteGuestsToTeam) <https://api.mattermost.com/#tag/teams/operation/InviteGuestsToTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/invite-guests/email", options=options)

    def invalidate_email_invites(self):
        """Invalidate active email invitations
        `Read in Mattermost API docs (teams - InvalidateEmailInvites) <https://api.mattermost.com/#tag/teams/operation/InvalidateEmailInvites>`_

        """
        return self.client.delete("""/api/v4/teams/invites/email""")

    def import_team(self, team_id, files, data=None):
        """Import a Team from other application

        team_id: Team GUID
        file: A file to be uploaded in zip format.
        filesize: The size of the zip file to be imported.
        importFrom: String that defines from which application the team was exported to be imported into Mattermost.

        `Read in Mattermost API docs (teams - ImportTeam) <https://api.mattermost.com/#tag/teams/operation/ImportTeam>`_

        """
        return self.client.post(f"/api/v4/teams/{team_id}/import", files=files, data=data)

    def get_team_invite_info(self, invite_id):
        """Get invite info for a team

        invite_id: Invite id for a team

        `Read in Mattermost API docs (teams - GetTeamInviteInfo) <https://api.mattermost.com/#tag/teams/operation/GetTeamInviteInfo>`_

        """
        return self.client.get(f"/api/v4/teams/invite/{invite_id}")

    def update_team_scheme(self, team_id, options):
        """Set a team's scheme

        team_id: Team GUID
        scheme_id: The ID of the scheme.

        `Read in Mattermost API docs (teams - UpdateTeamScheme) <https://api.mattermost.com/#tag/teams/operation/UpdateTeamScheme>`_

        """
        return self.client.put(f"/api/v4/teams/{team_id}/scheme", options=options)

    def team_members_minus_group_members(self, team_id, params=None):
        """Team members minus group members.

        team_id: Team GUID
        group_ids: A comma-separated list of group ids.
        page: The page to select.
        per_page: The number of users per page.

        `Read in Mattermost API docs (teams - TeamMembersMinusGroupMembers) <https://api.mattermost.com/#tag/teams/operation/TeamMembersMinusGroupMembers>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/members_minus_group_members", params=params)

    def search_files(self, team_id, data):
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
        return self.client.post(f"/api/v4/teams/{team_id}/files/search", data=data)
