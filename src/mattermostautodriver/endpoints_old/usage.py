from ._base import Base

__all__ = ["Usage"]


class Usage(Base):

    def get_posts_usage(self):
        """Get current usage of posts
        `Read in Mattermost API docs (usage - GetPostsUsage) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsUsage>`_

        """
        return self.client.get("""/api/v4/usage/posts""")

    def get_storage_usage(self):
        """Get the total file storage usage for the instance in bytes.
        `Read in Mattermost API docs (usage - GetStorageUsage) <https://developers.mattermost.com/api-documentation/#/operations/GetStorageUsage>`_

        """
        return self.client.get("""/api/v4/usage/storage""")
