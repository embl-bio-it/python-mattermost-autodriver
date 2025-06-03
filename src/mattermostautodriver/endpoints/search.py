from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Search"]


class Search(Base):

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

        `Read in Mattermost API docs (search - SearchFiles) <https://developers.mattermost.com/api-documentation/#/operations/SearchFiles>`_

        """
        __data = {
            "terms": terms,
            "is_or_search": is_or_search,
            "time_zone_offset": time_zone_offset,
            "include_deleted_channels": include_deleted_channels,
            "page": page,
            "per_page": per_page,
        }
        return self.client.post(f"/api/v4/teams/{team_id}/files/search", data=__data)

    def search_files(
        self,
        terms: str,
        is_or_search: bool,
        time_zone_offset: int | None = 0,
        include_deleted_channels: bool | None = None,
        page: int | None = 0,
        per_page: int | None = 60,
    ):
        """Search files across the teams of the current user

        terms: The search terms as entered by the user. To search for files from a user include ``from:someusername``, using a user's username. To search in a specific channel include ``in:somechannel``, using the channel name (not the display name). To search for specific extensions include ``ext:extension``.
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)

        `Read in Mattermost API docs (search - SearchFiles) <https://developers.mattermost.com/api-documentation/#/operations/SearchFiles>`_

        """
        __data = {
            "terms": terms,
            "is_or_search": is_or_search,
            "time_zone_offset": time_zone_offset,
            "include_deleted_channels": include_deleted_channels,
            "page": page,
            "per_page": per_page,
        }
        return self.client.post("""/api/v4/files/search""", data=__data)
