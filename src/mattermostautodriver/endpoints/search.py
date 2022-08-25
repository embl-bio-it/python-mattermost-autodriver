from .base import Base


class Search(Base):
    def search_files(self, team_id, data):
        """Search files in a team

        team_id: Team GUID
        terms: The search terms as inputed by the user. To search for files from a user include ``from:someusername``, using a user's username. To search in a specific channel include ``in:somechannel``, using the channel name (not the display name). To search for specific extensions included ``ext:extension``.
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)
        """
        return self.client.post(f"/teams/{team_id}/files/search", data=data)
