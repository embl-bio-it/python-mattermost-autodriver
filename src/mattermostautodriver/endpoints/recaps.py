from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Recaps"]


class Recaps(Base):

    def create_recap(self, title: str, channel_ids: list[str], agent_id: str):
        """Create a channel recap

        title: Title for the recap
        channel_ids: List of channel IDs to include in the recap
        agent_id: ID of the AI agent to use for generating the recap

        `Read in Mattermost API docs (recaps - CreateRecap) <https://developers.mattermost.com/api-documentation/#/operations/CreateRecap>`_

        """
        __options = {"title": title, "channel_ids": channel_ids, "agent_id": agent_id}
        return self.client.post("""/api/v4/recaps""", options=__options)

    def get_recaps_for_user(self, page: int | None = 0, per_page: int | None = 60):
        """Get current user's recaps

        page: The page to select.
        per_page: The number of recaps per page.

        `Read in Mattermost API docs (recaps - GetRecapsForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetRecapsForUser>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/recaps""", params=__params)

    def get_recap(self, recap_id: str):
        """Get a specific recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - GetRecap) <https://developers.mattermost.com/api-documentation/#/operations/GetRecap>`_

        """
        return self.client.get(f"/api/v4/recaps/{recap_id}")

    def delete_recap(self, recap_id: str):
        """Delete a recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - DeleteRecap) <https://developers.mattermost.com/api-documentation/#/operations/DeleteRecap>`_

        """
        return self.client.delete(f"/api/v4/recaps/{recap_id}")

    def mark_recap_as_read(self, recap_id: str):
        """Mark a recap as read

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - MarkRecapAsRead) <https://developers.mattermost.com/api-documentation/#/operations/MarkRecapAsRead>`_

        """
        return self.client.post(f"/api/v4/recaps/{recap_id}/read")

    def regenerate_recap(self, recap_id: str):
        """Regenerate a recap

        recap_id: Recap GUID

        `Read in Mattermost API docs (recaps - RegenerateRecap) <https://developers.mattermost.com/api-documentation/#/operations/RegenerateRecap>`_

        """
        return self.client.post(f"/api/v4/recaps/{recap_id}/regenerate")
