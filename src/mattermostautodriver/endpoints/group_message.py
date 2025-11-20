from ._base import Base
from typing import Any, BinaryIO

__all__ = ["GroupMessage"]


class GroupMessage(Base):

    def get_group_message_members_common_teams(self, channel_id: str):
        """Get common teams for members of a Group Message.

        channel_id: Channel GUID

        `Read in Mattermost API docs (group_message - GetGroupMessageMembersCommonTeams) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupMessageMembersCommonTeams>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/common_teams")
