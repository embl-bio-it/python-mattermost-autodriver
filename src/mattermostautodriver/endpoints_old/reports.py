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

    def get_posts_for_reporting(self, options):
        """Get posts for reporting and compliance purposes using cursor-based pagination

        channel_id: The ID of the channel to retrieve posts from
        cursor: Opaque cursor string for pagination. Omit or use empty string for the first request. For subsequent requests, use the exact cursor value from the previous response's next_cursor. The cursor is base64-encoded and contains all pagination state including time, post ID, and query parameters. Do not attempt to parse or modify the cursor value.

        start_time: Optional start time for query range in Unix milliseconds. Only used for the first request (ignored when cursor is provided). - For "asc" (ascending): starts retrieving from this time going forward - For "desc" (descending): starts retrieving from this time going backward If omitted, defaults to 0 for ascending or MaxInt64 for descending.

        time_field: Which timestamp field to use for sorting and filtering. Use "create_at" to retrieve posts by creation time, or "update_at" to retrieve posts by last modification time.

        sort_direction: Sort direction for pagination. Use "asc" to retrieve posts from oldest to newest, or "desc" to retrieve from newest to oldest.

        per_page: Number of posts to return per page. Maximum 1000.
        include_deleted: If true, include posts that have been deleted (DeleteAt > 0). By default, only non-deleted posts are returned.

        exclude_system_posts: If true, exclude all system posts.

        include_metadata: If true, enrich posts with additional metadata including file information, reactions, custom emojis, priority, and acknowledgements. Note that this may increase response time for large result sets.


        `Read in Mattermost API docs (reports - GetPostsForReporting) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsForReporting>`_

        """
        return self.client.post("""/api/v4/reports/posts""", options=options)
