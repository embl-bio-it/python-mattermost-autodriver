from .base import Base


class Uploads(Base):
    def create_upload(self, options):
        """Create an upload

        channel_id: The ID of the channel to upload to.
        filename: The name of the file to upload.
        file_size: The size of the file to upload in bytes.

        `Read in Mattermost API docs (uploads - CreateUpload) <https://api.mattermost.com/#tag/uploads/operation/CreateUpload>`_
        """
        return self.client.post("""/uploads""", options=options)

    def get_upload(self, upload_id):
        """Get an upload session

        upload_id: The ID of the upload session to get.

        `Read in Mattermost API docs (uploads - GetUpload) <https://api.mattermost.com/#tag/uploads/operation/GetUpload>`_
        """
        return self.client.get(f"/uploads/{upload_id}")

    def upload_data(self, upload_id, files, options=None):
        """Perform a file upload

        upload_id: The ID of the upload session the data belongs to.

        `Read in Mattermost API docs (uploads - UploadData) <https://api.mattermost.com/#tag/uploads/operation/UploadData>`_
        """
        return self.client.post(f"/uploads/{upload_id}", files=files, options=options)
