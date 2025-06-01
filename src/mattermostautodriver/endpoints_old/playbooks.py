from ._base import Base

__all__ = ["Playbooks"]


class Playbooks(Base):

    def get_playbooks(self, params=None):
        """List all playbooks

        team_id: ID of the team to filter by.
        page: Zero-based index of the page to request.
        per_page: Number of playbooks to return per page.
        sort: Field to sort the returned playbooks by title, number of stages or total number of steps.
        direction: Direction (ascending or descending) followed by the sorting of the playbooks.
        with_archived: Includes archived playbooks in the result.

        `Read in Mattermost API docs (Playbooks - getPlaybooks) <https://api.mattermost.com/#tag/Playbooks/operation/getPlaybooks>`_

        """
        return self.client.get("""/plugins/playbooks/api/v0/playbooks""", params=params)

    def create_playbook(self, options=None):
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
        return self.client.post("""/plugins/playbooks/api/v0/playbooks""", options=options)

    def get_playbook(self, id):
        """Get a playbook

        id: ID of the playbook to retrieve.

        `Read in Mattermost API docs (Playbooks - getPlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/getPlaybook>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/playbooks/{id}")

    def update_playbook(self, id, options=None):
        """Update a playbook

        id: ID of the playbook to update.

        `Read in Mattermost API docs (Playbooks - updatePlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/updatePlaybook>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/playbooks/{id}", options=options)

    def delete_playbook(self, id):
        """Delete a playbook

        id: ID of the playbook to delete.

        `Read in Mattermost API docs (Playbooks - deletePlaybook) <https://api.mattermost.com/#tag/Playbooks/operation/deletePlaybook>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/playbooks/{id}")
