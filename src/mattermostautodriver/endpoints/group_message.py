from ._base import Base, FileType
from typing import Any

__all__ = ["GroupMessage"]


class GroupMessage(Base):

    def get_group_message_members_common_teams(self, channel_id: str):
        """Get common teams for members of a Group Message.

        channel_id: Channel GUID

        `Read in Mattermost API docs (group_message - GetGroupMessageMembersCommonTeams) <https://developers.mattermost.com/api-documentation/#/operations/GetGroupMessageMembersCommonTeams>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/common_teams")

    def convert_group_message_to_channel(self, channel_id: str, team_id: str):
        """Convert group message to private channel

        channel_id: Group message channel ID
        channel_id:
        team_id:

        `Read in Mattermost API docs (group_message - ConvertGroupMessageToChannel) <https://developers.mattermost.com/api-documentation/#/operations/ConvertGroupMessageToChannel>`_

        """
        __options = {"channel_id": channel_id, "team_id": team_id}
        return self.client.post(f"/api/v4/channels/{channel_id}/convert_to_channel", options=__options)
