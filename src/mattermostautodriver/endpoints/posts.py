from .base import Base


class Posts(Base):
    def create_post(self, options):
        """Create a post

        channel_id: The channel ID to post in
        message: The message contents, can be formatted with Markdown
        root_id: The post ID to comment on
        file_ids: A list of file IDs to associate with the post. Note that posts are limited to 5 files maximum. Please use additional posts for more files.
        props: A general JSON property bag to attach to the post
        """
        return self.client.post("""/posts""", options=options)

    def create_post_ephemeral(self, options):
        """Create a ephemeral post

        user_id: The target user id for the ephemeral post
        post: Post object to create
        """
        return self.client.post("""/posts/ephemeral""", options=options)

    def get_post(self, post_id, params=None):
        """Get a post

        post_id: ID of the post to get
        include_deleted: Defines if result should include deleted posts, must have 'manage_system' (admin) permission.
        """
        return self.client.get(f"/posts/{post_id}", params=params)

    def delete_post(self, post_id):
        """Delete a post

        post_id: ID of the post to delete
        """
        return self.client.delete(f"/posts/{post_id}")

    def update_post(self, post_id, options):
        """Update a post

        post_id: ID of the post to update
        id: ID of the post to update
        is_pinned: Set to `true` to pin the post to the channel it is in
        message: The message text of the post
        has_reactions: Set to `true` if the post has reactions to it
        props: A general JSON property bag to attach to the post
        """
        return self.client.put(f"/posts/{post_id}", options=options)

    def set_post_unread(self, user_id, post_id):
        """Mark as unread from a post.

        user_id: User GUID
        post_id: Post GUID
        """
        return self.client.post(f"/users/{user_id}/posts/{post_id}/set_unread")

    def patch_post(self, post_id, options):
        """Patch a post

        post_id: Post GUID
        is_pinned: Set to `true` to pin the post to the channel it is in
        message: The message text of the post
        file_ids: The list of files attached to this post
        has_reactions: Set to `true` if the post has reactions to it
        props: A general JSON property bag to attach to the post
        """
        return self.client.put(f"/posts/{post_id}/patch", options=options)

    def get_post_thread(self, post_id, params=None):
        """Get a thread

        post_id: ID of a post in the thread
        perPage: The number of posts per page
        fromPost: The post_id to return the next page of posts from
        fromCreateAt: The create_at timestamp to return the next page of posts from
        direction: The direction to return the posts. Either up or down.
        skipFetchThreads: Whether to skip fetching threads or not
        collapsedThreads: Whether the client uses CRT or not
        collapsedThreadsExtended: Whether to return the associated users as part of the response or not
        """
        return self.client.get(f"/posts/{post_id}/thread", params=params)

    def get_flagged_posts_for_user(self, user_id, params=None):
        """Get a list of flagged posts

        user_id: ID of the user
        team_id: Team ID
        channel_id: Channel ID
        page: The page to select
        per_page: The number of posts per page
        """
        return self.client.get(f"/users/{user_id}/posts/flagged", params=params)

    def get_file_infos_for_post(self, post_id, params=None):
        """Get file info for post

        post_id: ID of the post
        include_deleted: Defines if result should include deleted posts, must have 'manage_system' (admin) permission.
        """
        return self.client.get(f"/posts/{post_id}/files/info", params=params)

    def get_posts_for_channel(self, channel_id, params=None):
        """Get posts for a channel

        channel_id: The channel ID to get the posts for
        page: The page to select
        per_page: The number of posts per page
        since: Provide a non-zero value in Unix time milliseconds to select posts modified after that time
        before: A post id to select the posts that came before this one
        after: A post id to select the posts that came after this one
        include_deleted: Whether to include deleted posts or not. Must have system admin permissions.
        """
        return self.client.get(f"/channels/{channel_id}/posts", params=params)

    def get_posts_around_last_unread(self, user_id, channel_id, params=None):
        """Get posts around oldest unread

        user_id: ID of the user
        channel_id: The channel ID to get the posts for
        limit_before: Number of posts before the oldest unread posts. Maximum is 200 posts if limit is set greater than that.
        limit_after: Number of posts after and including the oldest unread post. Maximum is 200 posts if limit is set greater than that.
        skipFetchThreads: Whether to skip fetching threads or not
        collapsedThreads: Whether the client uses CRT or not
        collapsedThreadsExtended: Whether to return the associated users as part of the response or not
        """
        return self.client.get(f"/users/{user_id}/channels/{channel_id}/posts/unread", params=params)

    def search_posts(self, team_id, options):
        """Search for team posts

        team_id: Team GUID
        terms: The search terms as inputed by the user. To search for posts from a user include `from:someusername`, using a user's username. To search in a specific channel include `in:somechannel`, using the channel name (not the display name).
        is_or_search: Set to true if an Or search should be performed vs an And search.
        time_zone_offset: Offset from UTC of user timezone for date searches.
        include_deleted_channels: Set to true if deleted channels should be included in the search. (archived channels)
        page: The page to select. (Only works with Elasticsearch)
        per_page: The number of posts per page. (Only works with Elasticsearch)
        """
        return self.client.post(f"/teams/{team_id}/posts/search", options=options)

    def pin_post(self, post_id):
        """Pin a post to the channel

        post_id: Post GUID
        """
        return self.client.post(f"/posts/{post_id}/pin")

    def unpin_post(self, post_id):
        """Unpin a post to the channel

        post_id: Post GUID
        """
        return self.client.post(f"/posts/{post_id}/unpin")

    def do_post_action(self, post_id, action_id):
        """Perform a post action

        post_id: Post GUID
        action_id: Action GUID
        """
        return self.client.post(f"/posts/{post_id}/actions/{action_id}")

    def get_posts_by_ids(self, options):
        """Get posts by a list of ids"""
        return self.client.post("""/posts/ids""", options=options)

    def set_post_reminder(self, user_id, post_id, options):
        """Set a post reminder

        user_id: User GUID
        post_id: Post GUID
        target_time: Target time for the reminder
        """
        return self.client.post(f"/users/{user_id}/posts/{post_id}/reminder", options=options)
