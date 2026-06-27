from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Boards"]


class Boards(Base):

    def create_board(
        self,
        team_id: str,
        type: str,
        display_name: str,
        name: str | None = None,
        header: str | None = None,
        purpose: str | None = None,
    ):
        """Create a board channel

        team_id: The team ID the board belongs to
        type: The board channel type.
        * ``BO`` - open board (visible to all team members)
        * ``BP`` - private board (visible to invited members)

        display_name: Human-readable name shown in the UI. Must not be empty.
        name: URL-safe channel name. Auto-generated if omitted.
        header:
        purpose:

        `Read in Mattermost API docs (boards - CreateBoard) <https://developers.mattermost.com/api-documentation/#/operations/CreateBoard>`_

        """
        __options = {
            "team_id": team_id,
            "type": type,
            "display_name": display_name,
            "name": name,
            "header": header,
            "purpose": purpose,
        }
        return self.client.post("""/api/v4/boards""", options=__options)
