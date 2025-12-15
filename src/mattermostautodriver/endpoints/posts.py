from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Posts"]


class Posts(Base):

    def create_post(
        self,
        channel_id: str,
        message: str,
        root_id: str | None = None,
        file_ids: list[str] | None = None,
        props: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ):
        """Create a post

        channel_id: The channel ID to post in
        message: The message contents, can be formatted with Markdown
        root_id: The post ID to comment on
        file_ids: A list of file IDs to associate with the post. Note that posts are limited to 5 files maximum. Please use additional posts for more files.
        props: A general JSON property bag to attach to the post
        metadata: A JSON object to add post metadata, e.g the post's priority

        `Read in Mattermost API docs (posts - CreatePost) <https://developers.mattermost.com/api-documentation/#/operations/CreatePost>`_

        """
        __options = {
            "channel_id": channel_id,
            "message": message,
            "root_id": root_id,
            "file_ids": file_ids,
            "props": props,
            "metadata": metadata,
        }
        return self.client.post("""/api/v4/posts""", options=__options)

    def create_post_ephemeral(self, user_id: str, post: dict[str, Any]):
        """Create a ephemeral post

        user_id: The target user id for the ephemeral post
        post: Post object to create

        `Read in Mattermost API docs (posts - CreatePostEphemeral) <https://developers.mattermost.com/api-documentation/#/operations/CreatePostEphemeral>`_

        """
        __options = {"user_id": user_id, "post": post}
        return self.client.post("""/api/v4/posts/ephemeral""", options=__options)

    def get_post(self, post_id: str, include_deleted: bool | None = False):
        """Get a post

        post_id: ID of the post to get
        include_deleted: Defines if result should include deleted posts, must have 'manage_system' (admin) permission.

        `Read in Mattermost API docs (posts - GetPost) <https://developers.mattermost.com/api-documentation/#/operations/GetPost>`_

        """
        __params = {"include_deleted": include_deleted}
        return self.client.get(f"/api/v4/posts/{post_id}", params=__params)

    def delete_post(self, post_id: str):
        """Delete a post

        post_id: ID of the post to delete

        `Read in Mattermost API docs (posts - DeletePost) <https://developers.mattermost.com/api-documentation/#/operations/DeletePost>`_

        """
        return self.client.delete(f"/api/v4/posts/{post_id}")

    def update_post(
        self,
        post_id: str,
        id: str,
        is_pinned: bool | None = None,
        message: str | None = None,
        has_reactions: bool | None = None,
        props: str | None = None,
    ):
        """Update a post

        post_id: ID of the post to update
        id: ID of the post to update
        is_pinned: Set to ``true`` to pin the post to the channel it is in
        message: The message text of the post
        has_reactions: Set to ``true`` if the post has reactions to it
        props: A general JSON property bag to attach to the post

        `Read in Mattermost API docs (posts - UpdatePost) <https://developers.mattermost.com/api-documentation/#/operations/UpdatePost>`_

        """
        __options = {
            "id": id,
            "is_pinned": is_pinned,
            "message": message,
            "has_reactions": has_reactions,
            "props": props,
        }
        return self.client.put(f"/api/v4/posts/{post_id}", options=__options)

    def set_post_unread(self, user_id: str, post_id: str):
        """Mark as unread from a post.

        user_id: User GUID
        post_id: Post GUID

        `Read in Mattermost API docs (posts - SetPostUnread) <https://developers.mattermost.com/api-documentation/#/operations/SetPostUnread>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/posts/{post_id}/set_unread")

    def patch_post(
        self,
        post_id: str,
        is_pinned: bool | None = None,
        message: str | None = None,
        file_ids: list[str] | None = None,
        has_reactions: bool | None = None,
        props: str | None = None,
    ):
        """Patch a post

        post_id: Post GUID
        is_pinned: Set to ``true`` to pin the post to the channel it is in
        message: The message text of the post
        file_ids: The list of files attached to this post
        has_reactions: Set to ``true`` if the post has reactions to it
        props: A general JSON property bag to attach to the post

        `Read in Mattermost API docs (posts - PatchPost) <https://developers.mattermost.com/api-documentation/#/operations/PatchPost>`_

        """
        __options = {
            "is_pinned": is_pinned,
            "message": message,
            "file_ids": file_ids,
            "has_reactions": has_reactions,
            "props": props,
        }
        return self.client.put(f"/api/v4/posts/{post_id}/patch", options=__options)

    def get_post_thread(
        self,
        post_id: str,
        perPage: int | None = 0,
        fromPost: str | None = "",
        fromCreateAt: int | None = 0,
        fromUpdateAt: int | None = 0,
        direction: str | None = "",
        skipFetchThreads: bool | None = False,
        collapsedThreads: bool | None = False,
        collapsedThreadsExtended: bool | None = False,
        updatesOnly: bool | None = False,
    ):
        """Get a thread

        post_id: ID of a post in the thread
        perPage: The number of posts per page
        fromPost: The post_id to return the next page of posts from
        fromCreateAt: The create_at timestamp to return the next page of posts from
        fromUpdateAt: The update_at timestamp to return the next page of posts from. You cannot set this flag with direction=down.
        direction: The direction to return the posts. Either up or down.
        skipFetchThreads: Whether to skip fetching threads or not
        collapsedThreads: Whether the client uses CRT or not
        collapsedThreadsExtended: Whether to return the associated users as part of the response or not
        updatesOnly: This flag is used to make the API work with the updateAt value. If you set this flag, you must set a value for fromUpdateAt.

        `Read in Mattermost API docs (posts - GetPostThread) <https://developers.mattermost.com/api-documentation/#/operations/GetPostThread>`_

        """
        __params = {
            "perPage": perPage,
            "fromPost": fromPost,
            "fromCreateAt": fromCreateAt,
            "fromUpdateAt": fromUpdateAt,
            "direction": direction,
            "skipFetchThreads": skipFetchThreads,
            "collapsedThreads": collapsedThreads,
            "collapsedThreadsExtended": collapsedThreadsExtended,
            "updatesOnly": updatesOnly,
        }
        return self.client.get(f"/api/v4/posts/{post_id}/thread", params=__params)

    def get_flagged_posts_for_user(
        self,
        user_id: str,
        team_id: str | None = None,
        channel_id: str | None = None,
        page: int | None = 0,
        per_page: int | None = 60,
    ):
        """Get a list of flagged posts

        user_id: ID of the user
        team_id: Team ID
        channel_id: Channel ID
        page: The page to select
        per_page: The number of posts per page

        `Read in Mattermost API docs (posts - GetFlaggedPostsForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetFlaggedPostsForUser>`_

        """
        __params = {"team_id": team_id, "channel_id": channel_id, "page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/users/{user_id}/posts/flagged", params=__params)

    def get_file_infos_for_post(self, post_id: str, include_deleted: bool | None = False):
        """Get file info for post

        post_id: ID of the post
        include_deleted: Defines if result should include deleted posts, must have 'manage_system' (admin) permission.

        `Read in Mattermost API docs (posts - GetFileInfosForPost) <https://developers.mattermost.com/api-documentation/#/operations/GetFileInfosForPost>`_

        """
        __params = {"include_deleted": include_deleted}
        return self.client.get(f"/api/v4/posts/{post_id}/files/info", params=__params)

    def get_posts_for_channel(
        self,
        channel_id: str,
        page: int | None = 0,
        per_page: int | None = 60,
        since: int | None = None,
        before: str | None = None,
        after: str | None = None,
        include_deleted: bool | None = False,
    ):
        """Get posts for a channel

        channel_id: The channel ID to get the posts for
        page: The page to select
        per_page: The number of posts per page
        since: Provide a non-zero value in Unix time milliseconds to select posts modified after that time
        before: A post id to select the posts that came before this one
        after: A post id to select the posts that came after this one
        include_deleted: Whether to include deleted posts or not. Must have system admin permissions.

        `Read in Mattermost API docs (posts - GetPostsForChannel) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsForChannel>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "since": since,
            "before": before,
            "after": after,
            "include_deleted": include_deleted,
        }
        return self.client.get(f"/api/v4/channels/{channel_id}/posts", params=__params)

    def get_posts_around_last_unread(
        self,
        user_id: str,
        channel_id: str,
        limit_before: int | None = 60,
        limit_after: int | None = 60,
        skipFetchThreads: bool | None = False,
        collapsedThreads: bool | None = False,
        collapsedThreadsExtended: bool | None = False,
    ):
        """Get posts around oldest unread

        user_id: ID of the user
        channel_id: The channel ID to get the posts for
        limit_before: Number of posts before the oldest unread posts. Maximum is 200 posts if limit is set greater than that.
        limit_after: Number of posts after and including the oldest unread post. Maximum is 200 posts if limit is set greater than that.
        skipFetchThreads: Whether to skip fetching threads or not
        collapsedThreads: Whether the client uses CRT or not
        collapsedThreadsExtended: Whether to return the associated users as part of the response or not

        `Read in Mattermost API docs (posts - GetPostsAroundLastUnread) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsAroundLastUnread>`_

        """
        __params = {
            "limit_before": limit_before,
            "limit_after": limit_after,
            "skipFetchThreads": skipFetchThreads,
            "collapsedThreads": collapsedThreads,
            "collapsedThreadsExtended": collapsedThreadsExtended,
        }
        return self.client.get(f"/api/v4/users/{user_id}/channels/{channel_id}/posts/unread", params=__params)

    def search_posts(
        self,
        team_id: str,
        terms: str,
        is_or_search: bool,
        time_zone_offset: int | None = 0,
        include_deleted_channels: bool | None = None,
        page: int | None = 0,
        per_page: int | None = 60,
    ):
        """Search for team posts

        team_id: Team GUID
        terms: The search terms as inputed by the user. To search for posts from a user include ``from:someusername``, using a user's username. To search in a specific channel include ``in:somechannel``, using the channel name (not the display name).
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)

        `Read in Mattermost API docs (posts - SearchPosts) <https://developers.mattermost.com/api-documentation/#/operations/SearchPosts>`_

        """
        __options = {
            "terms": terms,
            "is_or_search": is_or_search,
            "time_zone_offset": time_zone_offset,
            "include_deleted_channels": include_deleted_channels,
            "page": page,
            "per_page": per_page,
        }
        return self.client.post(f"/api/v4/teams/{team_id}/posts/search", options=__options)

    def pin_post(self, post_id: str):
        """Pin a post to the channel

        post_id: Post GUID

        `Read in Mattermost API docs (posts - PinPost) <https://developers.mattermost.com/api-documentation/#/operations/PinPost>`_

        """
        return self.client.post(f"/api/v4/posts/{post_id}/pin")

    def unpin_post(self, post_id: str):
        """Unpin a post to the channel

        post_id: Post GUID

        `Read in Mattermost API docs (posts - UnpinPost) <https://developers.mattermost.com/api-documentation/#/operations/UnpinPost>`_

        """
        return self.client.post(f"/api/v4/posts/{post_id}/unpin")

    def do_post_action(self, post_id: str, action_id: str):
        """Perform a post action

        post_id: Post GUID
        action_id: Action GUID

        `Read in Mattermost API docs (posts - DoPostAction) <https://developers.mattermost.com/api-documentation/#/operations/DoPostAction>`_

        """
        return self.client.post(f"/api/v4/posts/{post_id}/actions/{action_id}")

    def get_posts_by_ids(self, options: list[str]):
        """Get posts by a list of ids
        `Read in Mattermost API docs (posts - getPostsByIds) <https://developers.mattermost.com/api-documentation/#/operations/getPostsByIds>`_

        """
        return self.client.post("""/api/v4/posts/ids""", options=options)

    def set_post_reminder(self, user_id: str, post_id: str, target_time: int):
        """Set a post reminder

        user_id: User GUID
        post_id: Post GUID
        target_time: Target time for the reminder

        `Read in Mattermost API docs (posts - SetPostReminder) <https://developers.mattermost.com/api-documentation/#/operations/SetPostReminder>`_

        """
        __options = {"target_time": target_time}
        return self.client.post(f"/api/v4/users/{user_id}/posts/{post_id}/reminder", options=__options)

    def save_acknowledgement_for_post(self, user_id: str, post_id: str):
        """Acknowledge a post

        user_id: User GUID
        post_id: Post GUID

        `Read in Mattermost API docs (posts - SaveAcknowledgementForPost) <https://developers.mattermost.com/api-documentation/#/operations/SaveAcknowledgementForPost>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/posts/{post_id}/ack")

    def delete_acknowledgement_for_post(self, user_id: str, post_id: str):
        """Delete a post acknowledgement

        user_id: User GUID
        post_id: Post GUID

        `Read in Mattermost API docs (posts - DeleteAcknowledgementForPost) <https://developers.mattermost.com/api-documentation/#/operations/DeleteAcknowledgementForPost>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/posts/{post_id}/ack")

    def move_thread(self, post_id: str, channel_id: str):
        """Move a post (and any posts within that post's thread)

        post_id: The identifier of the post to move
        channel_id: The channel identifier of where the post/thread is to be moved

        `Read in Mattermost API docs (posts - MoveThread) <https://developers.mattermost.com/api-documentation/#/operations/MoveThread>`_

        """
        __options = {"channel_id": channel_id}
        return self.client.post(f"/api/v4/posts/{post_id}/move", options=__options)

    def restore_post_version(self, post_id: str, restore_version_id: str):
        """Restores a past version of a post

        post_id: The identifier of the post to restore
        restore_version_id: The identifier of the past version of post to restore to

        `Read in Mattermost API docs (posts - RestorePostVersion) <https://developers.mattermost.com/api-documentation/#/operations/RestorePostVersion>`_

        """
        return self.client.post(f"/api/v4/posts/{post_id}/restore/{restore_version_id}")

    def rewrite_message(self, agent_id: str, message: str, action: str, custom_prompt: str | None = None):
        """Rewrite a message using AI

        agent_id: The ID of the AI agent to use for rewriting
        message: The message text to rewrite
        action: The rewrite action to perform
        custom_prompt: Custom prompt for rewriting. Required when action is "custom", optional otherwise.

        `Read in Mattermost API docs (posts - RewriteMessage) <https://developers.mattermost.com/api-documentation/#/operations/RewriteMessage>`_

        """
        __options = {"agent_id": agent_id, "message": message, "action": action, "custom_prompt": custom_prompt}
        return self.client.post("""/api/v4/posts/rewrite""", options=__options)
