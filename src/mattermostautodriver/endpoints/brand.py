from .base import Base


class Brand(Base):
    def get_brand_image(self):
        """Get brand image"""
        return self.client.get("""/brand/image""")

    def upload_brand_image(self, files, data=None):
        """Upload brand image

        image: The image to be uploaded
        """
        return self.client.post("""/brand/image""", files=files, data=data)

    def delete_brand_image(self):
        """Delete current brand image"""
        return self.client.delete("""/brand/image""")
