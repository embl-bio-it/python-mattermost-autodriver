from ._base import Base

__all__ = ["Reports"]


class Reports(Base):

    def get_users_for_reporting(self, params=None):
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
        return self.client.get("""/api/v4/reports/users""", params=params)

    def get_user_count_for_reporting(self, params=None):
        """Gets the full count of users that match the filter.

        role_filter: Filter users by their role.
        team_filter: Filter users by a specified team ID.
        has_no_team: If true, show only users that have no team. Will ignore provided "team_filter" if true.
        hide_active: If true, show only users that are inactive. Cannot be used at the same time as "hide_inactive"
        hide_inactive: If true, show only users that are active. Cannot be used at the same time as "hide_active"
        search_term: A filtering search term that allows filtering by Username, FirstName, LastName, Nickname or Email

        `Read in Mattermost API docs (reports - GetUserCountForReporting) <https://developers.mattermost.com/api-documentation/#/operations/GetUserCountForReporting>`_

        """
        return self.client.get("""/api/v4/reports/users/count""", params=params)

    def start_batch_users_export(self):
        """Starts a job to export the users to a report file.
        `Read in Mattermost API docs (reports - StartBatchUsersExport) <https://developers.mattermost.com/api-documentation/#/operations/StartBatchUsersExport>`_

        """
        return self.client.post("""/api/v4/reports/users/export""")
