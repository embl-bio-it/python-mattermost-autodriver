from ._base import Base

__all__ = ["Views"]


class Views(Base):

    def list_channel_views(self, channel_id, params=None):
        """List channel views

        channel_id: Channel GUID
        per_page: The number of views per page (default 60, max 200)
        page: The 0-based page number for pagination (default 0)
        include_total_count: When true, the response is a ViewsWithCount object containing a views array and a total_count integer. When false or omitted, the response is a plain JSON array of View objects.


        `Read in Mattermost API docs (views - ListChannelViews) <https://developers.mattermost.com/api-documentation/#/operations/ListChannelViews>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/views", params=params)

    def create_channel_view(self, channel_id, options):
        """Create channel view

        channel_id: Channel GUID
        title: The title of the view
        type: The type of the view.
        * ``kanban`` - a kanban view

        description: The description of the view
        sort_order: The display order of the view within the channel
        props: Arbitrary key-value properties for the view

        `Read in Mattermost API docs (views - CreateChannelView) <https://developers.mattermost.com/api-documentation/#/operations/CreateChannelView>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/views", options=options)

    def get_channel_view(self, channel_id, view_id):
        """Get a channel view

        channel_id: Channel GUID
        view_id: View GUID

        `Read in Mattermost API docs (views - GetChannelView) <https://developers.mattermost.com/api-documentation/#/operations/GetChannelView>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/views/{view_id}")

    def update_channel_view(self, channel_id, view_id, options):
        """Update a channel view

        channel_id: Channel GUID
        view_id: View GUID

        `Read in Mattermost API docs (views - UpdateChannelView) <https://developers.mattermost.com/api-documentation/#/operations/UpdateChannelView>`_

        """
        return self.client.patch(f"/api/v4/channels/{channel_id}/views/{view_id}", options=options)

    def delete_channel_view(self, channel_id, view_id):
        """Delete a channel view

        channel_id: Channel GUID
        view_id: View GUID

        `Read in Mattermost API docs (views - DeleteChannelView) <https://developers.mattermost.com/api-documentation/#/operations/DeleteChannelView>`_

        """
        return self.client.delete(f"/api/v4/channels/{channel_id}/views/{view_id}")

    def get_posts_for_view(self, channel_id, view_id, params=None):
        """Get posts for a view

        channel_id: Channel GUID
        view_id: View GUID
        page: The 0-based page number for pagination (default 0)
        per_page: The number of posts per page (default 60, max 200)

        `Read in Mattermost API docs (views - GetPostsForView) <https://developers.mattermost.com/api-documentation/#/operations/GetPostsForView>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/views/{view_id}/posts", params=params)

    def update_channel_view_sort_order(self, channel_id, view_id, options):
        """Update a channel view's sort order

        channel_id: Channel GUID
        view_id: View GUID

        `Read in Mattermost API docs (views - UpdateChannelViewSortOrder) <https://developers.mattermost.com/api-documentation/#/operations/UpdateChannelViewSortOrder>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/views/{view_id}/sort_order", options=options)
