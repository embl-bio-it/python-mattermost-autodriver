from ._base import Base, FileType
from typing import Any

__all__ = ["Reports"]


class Reports(Base):

    def get_users_for_reporting(
        self,
        sort_column: str | None = None,
        direction: str | None = None,
        sort_direction: str | None = None,
        page_size: int | None = None,
        from_column_value: str | None = None,
        from_id: str | None = None,
        date_range: str | None = None,
        role_filter: str | None = None,
        team_filter: str | None = None,
        has_no_team: bool | None = None,
        hide_active: bool | None = None,
        hide_inactive: bool | None = None,
        search_term: str | None = None,
    ):
        """Get a list of paged and sorted users for admin reporting purposes

        sort_column: The column to sort the users by. Must be one of ("CreateAt", "Username", "FirstName", "LastName", "Nickname", "Email") or the API will return an error. Default: ``'Username'`` (applied server-side when omitted)
        direction: The direction to accept paging values from. Will return values ahead of the cursor if "prev", and below the cursor if "next". Default is "next". Default: ``'next'`` (applied server-side when omitted)
        sort_direction: The sorting direction. Must be one of ("asc", "desc"). Will default to 'asc' if not specified or the input is invalid. Default: ``'asc'`` (applied server-side when omitted)
        page_size: The maximum number of users to return. Default: ``50`` (applied server-side when omitted)
        from_column_value: The value of the sorted column corresponding to the cursor to read from. Should be blank for the first page asked for.
        from_id: The value of the user id corresponding to the cursor to read from. Should be blank for the first page asked for.
        date_range: The date range of the post statistics to display. Must be one of ("last30days", "previousmonth", "last6months", "alltime"). Will default to 'alltime' if the input is not valid. Default: ``'alltime'`` (applied server-side when omitted)
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

    def start_batch_users_export(self, date_range: str | None = None):
        """Starts a job to export the users to a report file.

        date_range: The date range of the post statistics to display. Must be one of ("last30days", "previousmonth", "last6months", "alltime"). Will default to 'alltime' if the input is not valid. Default: ``'alltime'`` (applied server-side when omitted)

        `Read in Mattermost API docs (reports - StartBatchUsersExport) <https://developers.mattermost.com/api-documentation/#/operations/StartBatchUsersExport>`_

        """
        __params = {"date_range": date_range}
        return self.client.post("""/api/v4/reports/users/export""", params=__params)

    def get_posts_for_reporting(
        self,
        channel_id: str,
        cursor: str | None = None,
        start_time: int | None = None,
        time_field: str | None = None,
        sort_direction: str | None = None,
        per_page: int | None = None,
        include_deleted: bool | None = None,
        exclude_system_posts: bool | None = None,
        include_metadata: bool | None = None,
    ):
        """Get posts for reporting and compliance purposes using cursor-based pagination

        channel_id: The ID of the channel to retrieve posts from
        cursor: Opaque cursor string for pagination. Omit or use empty string for the first request. For subsequent requests, use the exact cursor value from the previous response's next_cursor. The cursor is base64-encoded and contains all pagination state including time, post ID, and query parameters. Do not attempt to parse or modify the cursor value. Default: ``''`` (applied server-side when omitted)
        start_time: Optional start time for query range in Unix milliseconds. Only used for the first request (ignored when cursor is provided). - For "asc" (ascending): starts retrieving from this time going forward - For "desc" (descending): starts retrieving from this time going backward If omitted, defaults to 0 for ascending or MaxInt64 for descending.

        time_field: Which timestamp field to use for sorting and filtering. Use "create_at" to retrieve posts by creation time, or "update_at" to retrieve posts by last modification time. Default: ``'create_at'`` (applied server-side when omitted)
        sort_direction: Sort direction for pagination. Use "asc" to retrieve posts from oldest to newest, or "desc" to retrieve from newest to oldest. Default: ``'asc'`` (applied server-side when omitted)
        per_page: Number of posts to return per page. Maximum 1000. Default: ``100`` (applied server-side when omitted)
        include_deleted: If true, include posts that have been deleted (DeleteAt > 0). By default, only non-deleted posts are returned. Default: ``False`` (applied server-side when omitted)
        exclude_system_posts: If true, exclude all system posts. Default: ``False`` (applied server-side when omitted)
        include_metadata: If true, enrich posts with additional metadata including file information, reactions, custom emojis, priority, and acknowledgements. Note that this may increase response time for large result sets. Default: ``False`` (applied server-side when omitted)

        `Read in Mattermost API docs (reports - GetPostsForReporting) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsForReporting>`_

        """
        __options = {
            "channel_id": channel_id,
            "cursor": cursor,
            "start_time": start_time,
            "time_field": time_field,
            "sort_direction": sort_direction,
            "per_page": per_page,
            "include_deleted": include_deleted,
            "exclude_system_posts": exclude_system_posts,
            "include_metadata": include_metadata,
        }
        return self.client.post("""/api/v4/reports/posts""", options=__options)
