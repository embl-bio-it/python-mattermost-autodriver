from ._base import Base

__all__ = ["Brand"]


class Brand(Base):

    def get_brand_image(self):
        """Get brand image
        `Read in Mattermost API docs (brand - GetBrandImage) <https://developers.mattermost.com/api-documentation/#/operations/GetBrandImage>`_

        """
        return self.client.get("""/api/v4/brand/image""")

    def upload_brand_image(self, files, data=None):
        """Upload brand image

        image: The image to be uploaded

        `Read in Mattermost API docs (brand - UploadBrandImage) <https://developers.mattermost.com/api-documentation/#/operations/UploadBrandImage>`_

        """
        return self.client.post("""/api/v4/brand/image""", files=files, data=data)

    def delete_brand_image(self):
        """Delete current brand image
        `Read in Mattermost API docs (brand - DeleteBrandImage) <https://developers.mattermost.com/api-documentation/#/operations/DeleteBrandImage>`_

        """
        return self.client.delete("""/api/v4/brand/image""")
