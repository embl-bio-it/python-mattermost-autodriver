from .base import Base
from typing import Any, BinaryIO


class Uploads(Base):

    def create_upload(self, channel_id: str, filename: str, file_size: int):
        """Create an upload

        channel_id: The ID of the channel to upload to.
        filename: The name of the file to upload.
        file_size: The size of the file to upload in bytes.

        `Read in Mattermost API docs (uploads - CreateUpload) <https://api.mattermost.com/#tag/uploads/operation/CreateUpload>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "channel_id": channel_id,
            "filename": filename,
            "file_size": file_size,
        }
        return self.client.post("""/api/v4/uploads""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_upload(self, upload_id: str):
        """Get an upload session

        upload_id: The ID of the upload session to get.

        `Read in Mattermost API docs (uploads - GetUpload) <https://api.mattermost.com/#tag/uploads/operation/GetUpload>`_

        """
        return self.client.get(f"/api/v4/uploads/{upload_id}")

    def upload_data(self, upload_id: str, data: dict[str, Any] | None = None):
        """Perform a file upload

        upload_id: The ID of the upload session the data belongs to.

        `Read in Mattermost API docs (uploads - UploadData) <https://api.mattermost.com/#tag/uploads/operation/UploadData>`_

        """
        return self.client.post(f"/api/v4/uploads/{upload_id}", data=data)
