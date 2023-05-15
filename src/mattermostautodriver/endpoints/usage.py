from .base import Base


class Usage(Base):
    def get_posts_usage(self):
        """Get current usage of posts
        `Read in Mattermost API docs (usage - GetPostsUsage) <https://api.mattermost.com/#tag/usage/operation/GetPostsUsage>`_
        """
        return self.client.get("""/api/v4/usage/posts""")

    def get_storage_usage(self):
        """Get the total file storage usage for the instance in bytes.
        `Read in Mattermost API docs (usage - GetStorageUsage) <https://api.mattermost.com/#tag/usage/operation/GetStorageUsage>`_
        """
        return self.client.get("""/api/v4/usage/storage""")
