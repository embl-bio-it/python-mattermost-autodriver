from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Playbooks"]


class Playbooks(Base):

    def get_playbooks(
        self,
        team_id: str,
        page: int | None = 0,
        per_page: int | None = 1000,
        sort: str | None = "title",
        direction: str | None = "asc",
        with_archived: bool | None = False,
    ):
        """List all playbooks

        team_id: ID of the team to filter by.
        page: Zero-based index of the page to request.
        per_page: Number of playbooks to return per page.
        sort: Field to sort the returned playbooks by title, number of stages or total number of steps.
        direction: Direction (ascending or descending) followed by the sorting of the playbooks.
        with_archived: Includes archived playbooks in the result.

        `Read in Mattermost API docs (playbooks - getPlaybooks) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybooks>`_

        """
        __params = {
            "team_id": team_id,
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "direction": direction,
            "with_archived": with_archived,
        }
        return self.client.get("""/plugins/playbooks/api/v0/playbooks""", params=__params)

    def create_playbook(
        self,
        title: str,
        team_id: str,
        create_public_playbook_run: bool,
        checklists: list[dict[str, Any]],
        member_ids: list[str],
        description: str | None = None,
        public: bool | None = None,
        broadcast_channel_ids: list[str] | None = None,
        invited_user_ids: list[str] | None = None,
        invite_users_enabled: bool | None = None,
        default_owner_id: str | None = None,
        default_owner_enabled: str | None = None,
        announcement_channel_id: str | None = None,
        announcement_channel_enabled: bool | None = None,
        webhook_on_creation_url: str | None = None,
        webhook_on_creation_enabled: bool | None = None,
        webhook_on_status_update_url: str | None = None,
        webhook_on_status_update_enabled: bool | None = None,
    ):
        """Create a playbook

        title: The title of the playbook.
        description: The description of the playbook.
        team_id: The identifier of the team where the playbook is in.
        create_public_playbook_run: A boolean indicating whether the playbook runs created from this playbook should be public or private.
        public: A boolean indicating whether the playbook is licensed as public or private. Required 'true' for free tier.
        checklists: The stages defined by this playbook.
        member_ids: The identifiers of all the users that are members of this playbook.
        broadcast_channel_ids: The IDs of the channels where all the status updates will be broadcasted. The team of the broadcast channel must be the same as the playbook's team.
        invited_user_ids: A list with the IDs of the members to be automatically invited to the playbook run's channel as soon as the playbook run is created.
        invite_users_enabled: Boolean that indicates whether the members declared in invited_user_ids will be automatically invited.
        default_owner_id: User ID of the member that will be automatically assigned as owner as soon as the playbook run is created. If the member is not part of the playbook run's channel or is not included in the invited_user_ids list, they will be automatically invited to the channel.
        default_owner_enabled: Boolean that indicates whether the member declared in default_owner_id will be automatically assigned as owner.
        announcement_channel_id: ID of the channel where the playbook run will be automatically announced as soon as the playbook run is created.
        announcement_channel_enabled: Boolean that indicates whether the playbook run creation will be announced in the channel declared in announcement_channel_id.
        webhook_on_creation_url: An absolute URL where a POST request will be sent as soon as the playbook run is created. The allowed protocols are HTTP and HTTPS.
        webhook_on_creation_enabled: Boolean that indicates whether the webhook declared in webhook_on_creation_url will be automatically sent.
        webhook_on_status_update_url: An absolute URL where a POST request will be sent as soon as the playbook run's status is updated. The allowed protocols are HTTP and HTTPS.
        webhook_on_status_update_enabled: Boolean that indicates whether the webhook declared in webhook_on_status_update_url will be automatically sent.

        `Read in Mattermost API docs (playbooks - createPlaybook) <https://developers.mattermost.com/api-documentation/#/operations/createPlaybook>`_

        """
        __options = {
            "title": title,
            "description": description,
            "team_id": team_id,
            "create_public_playbook_run": create_public_playbook_run,
            "public": public,
            "checklists": checklists,
            "member_ids": member_ids,
            "broadcast_channel_ids": broadcast_channel_ids,
            "invited_user_ids": invited_user_ids,
            "invite_users_enabled": invite_users_enabled,
            "default_owner_id": default_owner_id,
            "default_owner_enabled": default_owner_enabled,
            "announcement_channel_id": announcement_channel_id,
            "announcement_channel_enabled": announcement_channel_enabled,
            "webhook_on_creation_url": webhook_on_creation_url,
            "webhook_on_creation_enabled": webhook_on_creation_enabled,
            "webhook_on_status_update_url": webhook_on_status_update_url,
            "webhook_on_status_update_enabled": webhook_on_status_update_enabled,
        }
        return self.client.post("""/plugins/playbooks/api/v0/playbooks""", options=__options)

    def get_playbook(self, id: str):
        """Get a playbook

        id: ID of the playbook to retrieve.

        `Read in Mattermost API docs (playbooks - getPlaybook) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybook>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}")

    def update_playbook(self, id: str, options: Any | None = None):
        """Update a playbook

        id: ID of the playbook to update.

        `Read in Mattermost API docs (playbooks - updatePlaybook) <https://developers.mattermost.com/api-documentation/#/operations/updatePlaybook>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/playbooks/{id}", options=options)

    def delete_playbook(self, id: str):
        """Delete a playbook

        id: ID of the playbook to delete.

        `Read in Mattermost API docs (playbooks - deletePlaybook) <https://developers.mattermost.com/api-documentation/#/operations/deletePlaybook>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/playbooks/{id}")

    def get_playbook_property_fields(self, id: str, updated_since: int | None = None):
        """Get property fields for a playbook

        id: ID of the playbook to retrieve property fields from.
        updated_since: Filter results to only include property fields updated after this timestamp (Unix time in milliseconds).

        `Read in Mattermost API docs (playbooks - getPlaybookPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybookPropertyFields>`_

        """
        __params = {"updated_since": updated_since}
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}/property_fields", params=__params)

    def create_playbook_property_field(self, id: str, options: Any | None = None):
        """Create a property field for a playbook

        id: ID of the playbook to create a property field for.

        `Read in Mattermost API docs (playbooks - createPlaybookPropertyField) <https://developers.mattermost.com/api-documentation/#/operations/createPlaybookPropertyField>`_

        """
        return self.client.post(f"/plugins/playbooks/api/v0/playbooks/{id}/property_fields", options=options)

    def update_playbook_property_field(self, id: str, field_id: str, options: Any | None = None):
        """Update a property field for a playbook

        id: ID of the playbook containing the property field.
        field_id: ID of the property field to update.

        `Read in Mattermost API docs (playbooks - updatePlaybookPropertyField) <https://developers.mattermost.com/api-documentation/#/operations/updatePlaybookPropertyField>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}", options=options)

    def delete_playbook_property_field(self, id: str, field_id: str):
        """Delete a property field for a playbook

        id: ID of the playbook containing the property field.
        field_id: ID of the property field to delete.

        `Read in Mattermost API docs (playbooks - deletePlaybookPropertyField) <https://developers.mattermost.com/api-documentation/#/operations/deletePlaybookPropertyField>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/playbooks/{id}/property_fields/{field_id}")

    def reorder_playbook_property_fields(self, id: str, field_id: str, target_position: int):
        """Reorder property fields for a playbook

        id: ID of the playbook.
        field_id: ID of the property field to move.
        target_position: Target position index (zero-based) where the field should be moved.

        `Read in Mattermost API docs (playbooks - reorderPlaybookPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/reorderPlaybookPropertyFields>`_

        """
        __options = {"field_id": field_id, "target_position": target_position}
        return self.client.post(f"/plugins/playbooks/api/v0/playbooks/{id}/property_fields/reorder", options=__options)
