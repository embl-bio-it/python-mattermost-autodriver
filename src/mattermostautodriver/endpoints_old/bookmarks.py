from ._base import Base

__all__ = ["Bookmarks"]


class Bookmarks(Base):

    def list_channel_bookmarks_for_channel(self, channel_id, params=None):
        """Get channel bookmarks for Channel

        channel_id: Channel GUID
        bookmarks_since: Timestamp to filter the bookmarks with. If set, the
        endpoint returns bookmarks that have been added, updated
        or deleted since its value


        `Read in Mattermost API docs (bookmarks - ListChannelBookmarksForChannel) <https://developers.mattermost.com/api-documentation/#/operations/ListChannelBookmarksForChannel>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/bookmarks", params=params)

    def create_channel_bookmark(self, channel_id, options):
        """Create channel bookmark

        channel_id: Channel GUID
        file_id: The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
        display_name: The name of the channel bookmark
        link_url: The URL associated with the channel bookmark. Required for bookmarks of type 'link'
        image_url: The URL of the image associated with the channel bookmark. Optional, only applies for bookmarks of type 'link'
        emoji: The emoji of the channel bookmark
        type: * ``link`` for channel bookmarks that reference a link. ``link_url`` is requied
        * ``file`` for channel bookmarks that reference a file. ``file_id`` is required


        `Read in Mattermost API docs (bookmarks - CreateChannelBookmark) <https://developers.mattermost.com/api-documentation/#/operations/CreateChannelBookmark>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/bookmarks", options=options)

    def update_channel_bookmark(self, channel_id, bookmark_id, options):
        """Update channel bookmark

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID
        file_id: The ID of the file associated with the channel bookmark. Required for bookmarks of type 'file'
        display_name: The name of the channel bookmark
        sort_order: The order of the channel bookmark
        link_url: The URL associated with the channel bookmark. Required for type bookmarks of type 'link'
        image_url: The URL of the image associated with the channel bookmark
        emoji: The emoji of the channel bookmark
        type: * ``link`` for channel bookmarks that reference a link. ``link_url`` is requied
        * ``file`` for channel bookmarks that reference a file. ``file_id`` is required


        `Read in Mattermost API docs (bookmarks - UpdateChannelBookmark) <https://developers.mattermost.com/api-documentation/#/operations/UpdateChannelBookmark>`_

        """
        return self.client.patch(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}", options=options)

    def delete_channel_bookmark(self, channel_id, bookmark_id):
        """Delete channel bookmark

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID

        `Read in Mattermost API docs (bookmarks - DeleteChannelBookmark) <https://developers.mattermost.com/api-documentation/#/operations/DeleteChannelBookmark>`_

        """
        return self.client.delete(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}")

    def update_channel_bookmark_sort_order(self, channel_id, bookmark_id, options=None):
        """Update channel bookmark's order

        channel_id: Channel GUID
        bookmark_id: Bookmark GUID

        `Read in Mattermost API docs (bookmarks - UpdateChannelBookmarkSortOrder) <https://developers.mattermost.com/api-documentation/#/operations/UpdateChannelBookmarkSortOrder>`_

        """
        return self.client.post(f"/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order", options=options)
