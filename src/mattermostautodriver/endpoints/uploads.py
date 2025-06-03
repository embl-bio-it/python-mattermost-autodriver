from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Uploads"]


class Uploads(Base):

    def create_upload(self, channel_id: str, filename: str, file_size: int):
        """Create an upload

        channel_id: The ID of the channel to upload to.
        filename: The name of the file to upload.
        file_size: The size of the file to upload in bytes.

        `Read in Mattermost API docs (uploads - CreateUpload) <https://developers.mattermost.com/api-documentation/#/operations/CreateUpload>`_

        """
        __options = {"channel_id": channel_id, "filename": filename, "file_size": file_size}
        return self.client.post("""/api/v4/uploads""", options=__options)

    def get_upload(self, upload_id: str):
        """Get an upload session

        upload_id: The ID of the upload session to get.

        `Read in Mattermost API docs (uploads - GetUpload) <https://developers.mattermost.com/api-documentation/#/operations/GetUpload>`_

        """
        return self.client.get(f"/api/v4/uploads/{upload_id}")

    def upload_data(self, upload_id: str, data: dict[str, Any] | None = None):
        """Perform a file upload

        upload_id: The ID of the upload session the data belongs to.

        `Read in Mattermost API docs (uploads - UploadData) <https://developers.mattermost.com/api-documentation/#/operations/UploadData>`_

        """
        return self.client.post(f"/api/v4/uploads/{upload_id}", data=data)
