from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Drafts"]


class Drafts(Base):

    def upsert_draft(self, options: Any):
        """Upsert synced draft
        `Read in Mattermost API docs (drafts - UpsertDraft) <https://developers.mattermost.com/api-documentation/#/operations/UpsertDraft>`_

        """
        return self.client.post("""/api/v4/drafts""", options=options)

    def get_drafts(self, user_id: str, team_id: str):
        """Get synced drafts for a team

        user_id: User ID
        team_id: Team ID

        `Read in Mattermost API docs (drafts - GetDrafts) <https://developers.mattermost.com/api-documentation/#/operations/GetDrafts>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/teams/{team_id}/drafts")

    def delete_draft(self, user_id: str, channel_id: str):
        """Delete synced draft

        user_id: User ID
        channel_id: Channel ID

        `Read in Mattermost API docs (drafts - DeleteDraft) <https://developers.mattermost.com/api-documentation/#/operations/DeleteDraft>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/channels/{channel_id}/drafts")

    def delete_draft_for_thread(self, user_id: str, channel_id: str, thread_id: str):
        """Delete synced thread draft

        user_id: User ID
        channel_id: Channel ID
        thread_id: Root post ID of the thread

        `Read in Mattermost API docs (drafts - DeleteDraftForThread) <https://developers.mattermost.com/api-documentation/#/operations/DeleteDraftForThread>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/channels/{channel_id}/drafts/{thread_id}")
