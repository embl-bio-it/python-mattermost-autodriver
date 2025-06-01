from .base import Base
from typing import Any


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

        `Read in Mattermost API docs (Playbooks - getPlaybooks) <https://api.mattermost.com/#tag/Playbooks/operation/getPlaybooks>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "team_id": team_id,
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "direction": direction,
            "with_archived": with_archived,
        }
        return self.client.get(
            """/plugins/playbooks/api/v0/playbooks""", params=params_71f8b7431cd64fcfa0dabd300d0636d2
        )

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

        `Read in Mattermost API docs (Playbooks - createPlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/createPlaybook>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
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
        return self.client.post(
            """/plugins/playbooks/api/v0/playbooks""", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def get_playbook(self, id: str):
        """Get a playbook

        id: ID of the playbook to retrieve.

        `Read in Mattermost API docs (Playbooks - getPlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/getPlaybook>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}")

    def update_playbook(self, id: str, options: Any | None = None):
        """Update a playbook

        id: ID of the playbook to update.

        `Read in Mattermost API docs (Playbooks - updatePlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/updatePlaybook>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/playbooks/{id}", options=options)

    def delete_playbook(self, id: str):
        """Delete a playbook

        id: ID of the playbook to delete.

        `Read in Mattermost API docs (Playbooks - deletePlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/deletePlaybook>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/playbooks/{id}")
