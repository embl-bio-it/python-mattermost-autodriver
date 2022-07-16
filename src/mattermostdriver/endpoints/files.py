from .base import Base


class Files(Base):
    def upload_file(self, data=None):
        """Upload a file

        files: A file to be uploaded
        channel_id: The ID of the channel that this file will be uploaded to
        client_ids: A unique identifier for the file that will be returned in the response
        """
        return self.client.post("""/files""", data=data)

    def get_file(self, file_id):
        """Get a file

        file_id: The ID of the file to get
        """
        return self.client.get(f"/files/{file_id}")

    def get_file_thumbnail(self, file_id):
        """Get a file's thumbnail

        file_id: The ID of the file to get
        """
        return self.client.get(f"/files/{file_id}/thumbnail")

    def get_file_preview(self, file_id):
        """Get a file's preview

        file_id: The ID of the file to get
        """
        return self.client.get(f"/files/{file_id}/preview")

    def get_file_link(self, file_id):
        """Get a public file link

        file_id: The ID of the file to get a link for
        """
        return self.client.get(f"/files/{file_id}/link")

    def get_file_info(self, file_id):
        """Get metadata for a file

        file_id: The ID of the file info to get
        """
        return self.client.get(f"/files/{file_id}/info")

    def get_file_public(self, file_id, params=None):
        """Get a public file

        file_id: The ID of the file to get
        h: File hash
        """
        return self.client.get(f"/files/{file_id}/public", params=params)

    def search_files(self, team_id, data):
        """Search files in a team

        team_id: Team GUID
        terms: The search terms as inputed by the user. To search for files from a user include `from:someusername`, using a user's username. To search in a specific channel include `in:somechannel`, using the channel name (not the display name). To search for specific extensions included `ext:extension`.
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)
        """
        return self.client.post(f"/teams/{team_id}/files/search", data=data)
