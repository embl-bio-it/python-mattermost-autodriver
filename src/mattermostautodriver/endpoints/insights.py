from .base import Base


class Insights(Base):
    def get_top_reactions_for_team(self, team_id, params=None):
        """Get a list of the top reactions for a team.

        team_id: Team GUID
        time_range: Time range can be "today", "7_day", or "28_day".
        - ``today``: reactions posted on the current day.
        - ``7_day``: reactions posted in the last 7 days.
        - ``28_day``: reactions posted in the last 28 days.

        page: The page to select.
        per_page: The number of items per page, up to a maximum of 200.

        `Read in Mattermost API docs (insights - GetTopReactionsForTeam) <https://api.mattermost.com/#tag/insights/operation/GetTopReactionsForTeam>`_
        """
        return self.client.get(f"/teams/{team_id}/top/reactions", params=params)

    def get_top_reactions_for_user(self, params=None):
        """Get a list of the top reactions for a user.

        time_range: Time range can be "today", "7_day", or "28_day".
        - ``today``: reactions posted on the current day.
        - ``7_day``: reactions posted in the last 7 days.
        - ``28_day``: reactions posted in the last 28 days.

        page: The page to select.
        per_page: The number of items per page, up to a maximum of 200.
        team_id: Team ID will scope the response to a given team and exclude direct and group messages.
        ##### Permissions
        Must have ``view_team`` permission for the team.


        `Read in Mattermost API docs (insights - GetTopReactionsForUser) <https://api.mattermost.com/#tag/insights/operation/GetTopReactionsForUser>`_
        """
        return self.client.get("""/users/me/top/reactions""", params=params)

    def get_top_channels_for_team(self, team_id, params=None):
        """Get a list of the top channels for a team.

        team_id: Team GUID
        time_range: Time range can be "today", "7_day", or "28_day".
        - ``today``: channels with posts on the current day.
        - ``7_day``: channels with posts in the last 7 days.
        - ``28_day``: channels with posts in the last 28 days.

        page: The page to select.
        per_page: The number of items per page, up to a maximum of 200.

        `Read in Mattermost API docs (insights - GetTopChannelsForTeam) <https://api.mattermost.com/#tag/insights/operation/GetTopChannelsForTeam>`_
        """
        return self.client.get(f"/teams/{team_id}/top/channels", params=params)

    def get_top_channels_for_user(self, params=None):
        """Get a list of the top channels for a user.

        time_range: Time range can be "today", "7_day", or "28_day".
        - ``today``: channels with posts on the current day.
        - ``7_day``: channels with posts in the last 7 days.
        - ``28_day``: channels with posts in the last 28 days.

        page: The page to select.
        per_page: The number of items per page, up to a maximum of 200.
        team_id: Team ID will scope the response to a given team.
        ##### Permissions
        Must have ``view_team`` permission for the team.


        `Read in Mattermost API docs (insights - GetTopChannelsForUser) <https://api.mattermost.com/#tag/insights/operation/GetTopChannelsForUser>`_
        """
        return self.client.get("""/users/me/top/channels""", params=params)

    def get_new_team_members(self, team_id, params=None):
        """Get a list of new team members.

        team_id: Team GUID
        time_range: Time range can be "today", "7_day", or "28_day".
        - ``today``: team members who joined during the current day.
        - ``7_day``: team members who joined in the last 7 days.
        - ``28_day``: team members who joined in the last 28 days.

        page: The page to select.
        per_page: The number of items per page.

        `Read in Mattermost API docs (insights - GetNewTeamMembers) <https://api.mattermost.com/#tag/insights/operation/GetNewTeamMembers>`_
        """
        return self.client.get(f"/teams/{team_id}/top/team_members", params=params)
