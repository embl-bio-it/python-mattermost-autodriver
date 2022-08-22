from .base import Base


class Usage(Base):
    def get_posts_usage(self):
        """Get current usage of posts"""
        return self.client.get("""/usage/posts""")

    def get_storage_usage(self):
        """Get the total file storage usage for the instance in bytes."""
        return self.client.get("""/usage/storage""")
