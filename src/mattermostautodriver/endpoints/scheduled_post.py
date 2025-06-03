from ._base import Base
from typing import Any, BinaryIO

__all__ = ["ScheduledPost"]


class ScheduledPost(Base):

    def create_scheduled_post(
        self,
        scheduled_at: int,
        channel_id: str,
        message: str,
        root_id: str | None = None,
        file_ids: list[Any] | None = None,
        props: dict[str, Any] | None = None,
    ):
        """Creates a scheduled post

        scheduled_at: UNIX timestamp in milliseconds of the time when the scheduled post should be sent
        channel_id: The channel ID to post in
        message: The message contents, can be formatted with Markdown
        root_id: The post ID to comment on
        file_ids: A list of file IDs to associate with the post. Note that posts are limited to 5 files maximum. Please use additional posts for more files.
        props: A general JSON property bag to attach to the post

        `Read in Mattermost API docs (scheduled_post - CreateScheduledPost) <https://developers.mattermost.com/api-documentation/#/operations/CreateScheduledPost>`_

        """
        __options = {
            "scheduled_at": scheduled_at,
            "channel_id": channel_id,
            "message": message,
            "root_id": root_id,
            "file_ids": file_ids,
            "props": props,
        }
        return self.client.post("""/api/v4/posts/schedule""", options=__options)

    def get_user_scheduled_posts(self, includeDirectChannels: bool | None = False):
        """Gets all scheduled posts for a user for the specified team..

        includeDirectChannels: Whether to include scheduled posts from DMs an GMs or not. Default is false

        `Read in Mattermost API docs (scheduled_post - GetUserScheduledPosts) <https://developers.mattermost.com/api-documentation/#/operations/GetUserScheduledPosts>`_

        """
        __params = {"includeDirectChannels": includeDirectChannels}
        return self.client.get(f"/api/v4/posts/scheduled/team/{team_id}", params=__params)

    def update_scheduled_post(
        self, scheduled_post_id: str, id: str, channel_id: str, user_id: str, scheduled_at: int, message: str
    ):
        """Update a scheduled post

        scheduled_post_id: ID of the scheduled post to update
        id: ID of the scheduled post to update
        channel_id: The channel ID to post in
        user_id: The current user ID
        scheduled_at: UNIX timestamp in milliseconds of the time when the scheduled post should be sent
        message: The message contents, can be formatted with Markdown

        `Read in Mattermost API docs (scheduled_post - UpdateScheduledPost) <https://developers.mattermost.com/api-documentation/#/operations/UpdateScheduledPost>`_

        """
        __options = {
            "id": id,
            "channel_id": channel_id,
            "user_id": user_id,
            "scheduled_at": scheduled_at,
            "message": message,
        }
        return self.client.put(f"/api/v4/posts/schedule/{scheduled_post_id}", options=__options)

    def delete_scheduled_post(self, scheduled_post_id: str):
        """Delete a scheduled post

        scheduled_post_id: ID of the scheduled post to delete

        `Read in Mattermost API docs (scheduled_post - DeleteScheduledPost) <https://developers.mattermost.com/api-documentation/#/operations/DeleteScheduledPost>`_

        """
        return self.client.delete(f"/api/v4/posts/schedule/{scheduled_post_id}")
