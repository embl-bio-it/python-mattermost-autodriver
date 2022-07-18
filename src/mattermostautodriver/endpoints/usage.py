from .base import Base


class Usage(Base):
    def get_posts_usage(self):
        """Get current usage of posts"""
        return self.client.get("""/usage/posts""")
