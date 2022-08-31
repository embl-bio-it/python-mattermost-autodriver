from .base import Base


class Brand(Base):
    def get_brand_image(self):
        """Get brand image
        `Read in Mattermost API docs (brand - GetBrandImage) <https://api.mattermost.com/#tag/brand/operation/GetBrandImage>`_
        """
        return self.client.get("""/brand/image""")

    def upload_brand_image(self, files, data=None):
        """Upload brand image

        image: The image to be uploaded

        `Read in Mattermost API docs (brand - UploadBrandImage) <https://api.mattermost.com/#tag/brand/operation/UploadBrandImage>`_
        """
        return self.client.post("""/brand/image""", files=files, data=data)

    def delete_brand_image(self):
        """Delete current brand image
        `Read in Mattermost API docs (brand - DeleteBrandImage) <https://api.mattermost.com/#tag/brand/operation/DeleteBrandImage>`_
        """
        return self.client.delete("""/brand/image""")
