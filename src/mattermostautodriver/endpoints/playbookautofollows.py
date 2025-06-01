from .base import Base
from typing import Any


class PlaybookAutofollows(Base):

    def get_auto_follows(self, id: str):
        """Get the list of followers' user IDs of a playbook

        id: ID of the playbook to retrieve followers from.

        `Read in Mattermost API docs (PlaybookAutofollows - getAutoFollows) <https://api.mattermost.com/#tag/PlaybookAutofollows/operation/getAutoFollows>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}/autofollows")
