from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Conditions"]


class Conditions(Base):

    def get_playbook_conditions(self, id: str, page: int | None = 0, per_page: int | None = 20):
        """List playbook conditions

        id: ID of the playbook to retrieve conditions from.
        page: Zero-based index of the page to request.
        per_page: Number of conditions to return per page.

        `Read in Mattermost API docs (conditions - getPlaybookConditions) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybookConditions>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}/conditions", params=__params)

    def create_playbook_condition(self, id: str, options: Any | None = None):
        """Create a playbook condition

        id: ID of the playbook to create a condition for.

        `Read in Mattermost API docs (conditions - createPlaybookCondition) <https://developers.mattermost.com/api-documentation/#/operations/createPlaybookCondition>`_

        """
        return self.client.post(f"/plugins/playbooks/api/v0/playbooks/{id}/conditions", options=options)

    def update_playbook_condition(self, id: str, conditionID: str, options: Any | None = None):
        """Update a playbook condition

        id: ID of the playbook.
        conditionID: ID of the condition to update.

        `Read in Mattermost API docs (conditions - updatePlaybookCondition) <https://developers.mattermost.com/api-documentation/#/operations/updatePlaybookCondition>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/playbooks/{id}/conditions/{conditionID}", options=options)

    def delete_playbook_condition(self, id: str, conditionID: str):
        """Delete a playbook condition

        id: ID of the playbook.
        conditionID: ID of the condition to delete.

        `Read in Mattermost API docs (conditions - deletePlaybookCondition) <https://developers.mattermost.com/api-documentation/#/operations/deletePlaybookCondition>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/playbooks/{id}/conditions/{conditionID}")

    def get_run_conditions(self, id: str, page: int | None = 0, per_page: int | None = 20):
        """List run conditions

        id: ID of the run to retrieve conditions from.
        page: Zero-based index of the page to request.
        per_page: Number of conditions to return per page.

        `Read in Mattermost API docs (conditions - getRunConditions) <https://developers.mattermost.com/api-documentation/#/operations/getRunConditions>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/plugins/playbooks/api/v0/runs/{id}/conditions", params=__params)
