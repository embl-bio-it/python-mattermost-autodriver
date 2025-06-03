from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Reports"]


class Reports(Base):

    def get_users_for_reporting(
        self,
        sort_column: str | None = "Username",
        direction: str | None = "next",
        sort_direction: str | None = "asc",
        page_size: int | None = 50,
        from_column_value: str | None = None,
        from_id: str | None = None,
        date_range: str | None = "alltime",
        role_filter: str | None = None,
        team_filter: str | None = None,
        has_no_team: bool | None = None,
        hide_active: bool | None = None,
        hide_inactive: bool | None = None,
        search_term: str | None = None,
    ):
        """Get a list of paged and sorted users for admin reporting purposes

        sort_column: The column to sort the users by. Must be one of ("CreateAt", "Username", "FirstName", "LastName", "Nickname", "Email") or the API will return an error.
        direction: The direction to accept paging values from. Will return values ahead of the cursor if "prev", and below the cursor if "next". Default is "next".
        sort_direction: The sorting direction. Must be one of ("asc", "desc"). Will default to 'asc' if not specified or the input is invalid.
        page_size: The maximum number of users to return.
        from_column_value: The value of the sorted column corresponding to the cursor to read from. Should be blank for the first page asked for.
        from_id: The value of the user id corresponding to the cursor to read from. Should be blank for the first page asked for.
        date_range: The date range of the post statistics to display. Must be one of ("last30days", "previousmonth", "last6months", "alltime"). Will default to 'alltime' if the input is not valid.
        role_filter: Filter users by their role.
        team_filter: Filter users by a specified team ID.
        has_no_team: If true, show only users that have no team. Will ignore provided "team_filter" if true.
        hide_active: If true, show only users that are inactive. Cannot be used at the same time as "hide_inactive"
        hide_inactive: If true, show only users that are active. Cannot be used at the same time as "hide_active"
        search_term: A filtering search term that allows filtering by Username, FirstName, LastName, Nickname or Email

        `Read in Mattermost API docs (reports - GetUsersForReporting) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersForReporting>`_

        """
        __params = {
            "sort_column": sort_column,
            "direction": direction,
            "sort_direction": sort_direction,
            "page_size": page_size,
            "from_column_value": from_column_value,
            "from_id": from_id,
            "date_range": date_range,
            "role_filter": role_filter,
            "team_filter": team_filter,
            "has_no_team": has_no_team,
            "hide_active": hide_active,
            "hide_inactive": hide_inactive,
            "search_term": search_term,
        }
        return self.client.get("""/api/v4/reports/users""", params=__params)

    def get_user_count_for_reporting(
        self,
        role_filter: str | None = None,
        team_filter: str | None = None,
        has_no_team: bool | None = None,
        hide_active: bool | None = None,
        hide_inactive: bool | None = None,
        search_term: str | None = None,
    ):
        """Gets the full count of users that match the filter.

        role_filter: Filter users by their role.
        team_filter: Filter users by a specified team ID.
        has_no_team: If true, show only users that have no team. Will ignore provided "team_filter" if true.
        hide_active: If true, show only users that are inactive. Cannot be used at the same time as "hide_inactive"
        hide_inactive: If true, show only users that are active. Cannot be used at the same time as "hide_active"
        search_term: A filtering search term that allows filtering by Username, FirstName, LastName, Nickname or Email

        `Read in Mattermost API docs (reports - GetUserCountForReporting) <https://developers.mattermost.com/api-documentation/#/operations/GetUserCountForReporting>`_

        """
        __params = {
            "role_filter": role_filter,
            "team_filter": team_filter,
            "has_no_team": has_no_team,
            "hide_active": hide_active,
            "hide_inactive": hide_inactive,
            "search_term": search_term,
        }
        return self.client.get("""/api/v4/reports/users/count""", params=__params)

    def start_batch_users_export(self):
        """Starts a job to export the users to a report file.
        `Read in Mattermost API docs (reports - StartBatchUsersExport) <https://developers.mattermost.com/api-documentation/#/operations/StartBatchUsersExport>`_

        """
        return self.client.post("""/api/v4/reports/users/export""")
