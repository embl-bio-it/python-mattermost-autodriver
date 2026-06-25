from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Files"]


class Files(Base):

    def upload_file(self, files: BinaryIO | None = None, channel_id: str | None = None, client_ids: str | None = None):
        """Upload a file

        files: A file to be uploaded
        channel_id: The ID of the channel that this file will be uploaded to
        client_ids: A unique identifier for the file that will be returned in the response

        `Read in Mattermost API docs (files - UploadFile) <https://developers.mattermost.com/api-documentation/#/operations/UploadFile>`_

        """
        __files = {"files": files}
        __data = {"channel_id": channel_id, "client_ids": client_ids}
        return self.client.post("""/api/v4/files""", files=__files, data=__data)

    def get_file(self, file_id: str):
        """Get a file

        file_id: The ID of the file to get

        `Read in Mattermost API docs (files - GetFile) <https://developers.mattermost.com/api-documentation/#/operations/GetFile>`_

        """
        return self.client.get(f"/api/v4/files/{file_id}")

    def get_file_thumbnail(self, file_id: str):
        """Get a file's thumbnail

        file_id: The ID of the file to get

        `Read in Mattermost API docs (files - GetFileThumbnail) <https://developers.mattermost.com/api-documentation/#/operations/GetFileThumbnail>`_

        """
        return self.client.get(f"/api/v4/files/{file_id}/thumbnail")

    def get_file_preview(self, file_id: str):
        """Get a file's preview

        file_id: The ID of the file to get

        `Read in Mattermost API docs (files - GetFilePreview) <https://developers.mattermost.com/api-documentation/#/operations/GetFilePreview>`_

        """
        return self.client.get(f"/api/v4/files/{file_id}/preview")

    def get_file_link(self, file_id: str):
        """Get a public file link

        file_id: The ID of the file to get a link for

        `Read in Mattermost API docs (files - GetFileLink) <https://developers.mattermost.com/api-documentation/#/operations/GetFileLink>`_

        """
        return self.client.get(f"/api/v4/files/{file_id}/link")

    def get_file_info(self, file_id: str):
        """Get metadata for a file

        file_id: The ID of the file info to get

        `Read in Mattermost API docs (files - GetFileInfo) <https://developers.mattermost.com/api-documentation/#/operations/GetFileInfo>`_

        """
        return self.client.get(f"/api/v4/files/{file_id}/info")

    def get_file_public(self, file_id: str, h: str):
        """Get a public file

        file_id: The ID of the file to get
        h: File hash

        `Read in Mattermost API docs (files - GetFilePublic) <https://developers.mattermost.com/api-documentation/#/operations/GetFilePublic>`_

        """
        __params = {"h": h}
        return self.client.get(f"/files/{file_id}/public", params=__params)

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

        `Read in Mattermost API docs (files - SearchFiles) <https://developers.mattermost.com/api-documentation/#/operations/SearchFiles>`_

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

        `Read in Mattermost API docs (files - SearchFiles) <https://developers.mattermost.com/api-documentation/#/operations/SearchFiles>`_

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
