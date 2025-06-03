from ._base import Base

__all__ = ["PlaybookAutofollows"]


class PlaybookAutofollows(Base):

    def get_auto_follows(self, id):
        """Get the list of followers' user IDs of a playbook

        id: ID of the playbook to retrieve followers from.

        `Read in Mattermost API docs (playbook_autofollows - getAutoFollows) <https://developers.mattermost.com/api-documentation/#/operations/getAutoFollows>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}/autofollows")
