from .base import Base


class Uploads(Base):
    def create_upload(self, options):
        """Create an upload

        channel_id: The ID of the channel to upload to.
        filename: The name of the file to upload.
        file_size: The size of the file to upload in bytes.
        """
        return self.client.post("""/uploads""", options=options)

    def get_upload(self, upload_id):
        """Get an upload session

        upload_id: The ID of the upload session to get.
        """
        return self.client.get(f"/uploads/{upload_id}")

    def upload_data(self, upload_id, options=None, files=None):
        """Perform a file upload

        upload_id: The ID of the upload session the data belongs to.
        """
        return self.client.post(f"/uploads/{upload_id}", options=options, files=files)
