from ._base import Base
from typing import Any, BinaryIO

__all__ = ["PlaybookRuns"]


class PlaybookRuns(Base):

    def list_playbook_runs(
        self,
        team_id: str,
        page: int | None = 0,
        per_page: int | None = 1000,
        sort: str | None = "create_at",
        direction: str | None = "desc",
        statuses: list[str] | None = ["InProgress"],
        owner_user_id: str | None = None,
        participant_id: str | None = None,
        search_term: str | None = None,
        channel_id: str | None = None,
        omit_ended: bool | None = False,
        since: int | None = None,
    ):
        """List all playbook runs

        team_id: ID of the team to filter by.
        page: Zero-based index of the page to request.
        per_page: Number of playbook runs to return per page.
        sort: Field to sort the returned playbook runs by.
        direction: Direction (ascending or descending) followed by the sorting of the playbook runs.
        statuses: The returned list will contain only the playbook runs with the specified statuses.
        owner_user_id: The returned list will contain only the playbook runs commanded by this user. Specify "me" for current user.
        participant_id: The returned list will contain only the playbook runs for which the given user is a participant. Specify "me" for current user.
        search_term: The returned list will contain only the playbook runs whose name contains the search term.
        channel_id: The returned list will contain only the playbook runs associated with this channel ID.
        omit_ended: When set to true, only active runs (with EndAt = 0) are returned. When false or omitted, both active and ended runs are returned.
        since: Return only PlaybookRuns created/modified since the given timestamp (in milliseconds).

        `Read in Mattermost API docs (playbook_runs - listPlaybookRuns) <https://developers.mattermost.com/api-documentation/#/operations/listPlaybookRuns>`_

        """
        __params = {
            "team_id": team_id,
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "direction": direction,
            "statuses": statuses,
            "owner_user_id": owner_user_id,
            "participant_id": participant_id,
            "search_term": search_term,
            "channel_id": channel_id,
            "omit_ended": omit_ended,
            "since": since,
        }
        return self.client.get("""/plugins/playbooks/api/v0/runs""", params=__params)

    def create_playbook_run_from_post(
        self,
        name: str,
        owner_user_id: str,
        team_id: str,
        playbook_id: str,
        description: str | None = None,
        post_id: str | None = None,
    ):
        """Create a new playbook run

        name: The name of the playbook run.
        description: The description of the playbook run.
        owner_user_id: The identifier of the user who is commanding the playbook run.
        team_id: The identifier of the team where the playbook run's channel is in.
        post_id: If the playbook run was created from a post, this field contains the identifier of such post. If not, this field is empty.
        playbook_id: The identifier of the playbook with from which this playbook run was created.

        `Read in Mattermost API docs (playbook_runs - createPlaybookRunFromPost) <https://developers.mattermost.com/api-documentation/#/operations/createPlaybookRunFromPost>`_

        """
        __options = {
            "name": name,
            "description": description,
            "owner_user_id": owner_user_id,
            "team_id": team_id,
            "post_id": post_id,
            "playbook_id": playbook_id,
        }
        return self.client.post("""/plugins/playbooks/api/v0/runs""", options=__options)

    def get_owners(self, team_id: str):
        """Get all owners

        team_id: ID of the team to filter by.

        `Read in Mattermost API docs (playbook_runs - getOwners) <https://developers.mattermost.com/api-documentation/#/operations/getOwners>`_

        """
        __params = {"team_id": team_id}
        return self.client.get("""/plugins/playbooks/api/v0/runs/owners""", params=__params)

    def get_channels(
        self,
        team_id: str,
        sort: str | None = "create_at",
        direction: str | None = "desc",
        status: str | None = "all",
        owner_user_id: str | None = None,
        search_term: str | None = None,
        participant_id: str | None = None,
    ):
        """Get playbook run channels

        team_id: ID of the team to filter by.
        sort: Field to sort the returned channels by, according to their playbook run.
        direction: Direction (ascending or descending) followed by the sorting of the playbook runs associated to the channels.
        status: The returned list will contain only the channels whose playbook run has this status.
        owner_user_id: The returned list will contain only the channels whose playbook run is commanded by this user.
        search_term: The returned list will contain only the channels associated to a playbook run whose name contains the search term.
        participant_id: The returned list will contain only the channels associated to a playbook run for which the given user is a participant.

        `Read in Mattermost API docs (playbook_runs - getChannels) <https://developers.mattermost.com/api-documentation/#/operations/getChannels>`_

        """
        __params = {
            "team_id": team_id,
            "sort": sort,
            "direction": direction,
            "status": status,
            "owner_user_id": owner_user_id,
            "search_term": search_term,
            "participant_id": participant_id,
        }
        return self.client.get("""/plugins/playbooks/api/v0/runs/channels""", params=__params)

    def get_playbook_run_by_channel_id(self, channel_id: str):
        """Find playbook run by channel ID

        channel_id: ID of the channel associated to the playbook run to retrieve.

        `Read in Mattermost API docs (playbook_runs - getPlaybookRunByChannelId) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybookRunByChannelId>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/runs/channel/{channel_id}")

    def get_playbook_run(self, id: str):
        """Get a playbook run

        id: ID of the playbook run to retrieve.

        `Read in Mattermost API docs (playbook_runs - getPlaybookRun) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybookRun>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/runs/{id}")

    def update_playbook_run(self, id: str, active_stage: int | None = None):
        """Update a playbook run

        id: ID of the playbook run to retrieve.
        active_stage: Zero-based index of the stage that will be made active.

        `Read in Mattermost API docs (playbook_runs - updatePlaybookRun) <https://developers.mattermost.com/api-documentation/#/operations/updatePlaybookRun>`_

        """
        __options = {"active_stage": active_stage}
        return self.client.patch(f"/plugins/playbooks/api/v0/runs/{id}", options=__options)

    def get_playbook_run_metadata(self, id: str):
        """Get playbook run metadata

        id: ID of the playbook run whose metadata will be retrieved.

        `Read in Mattermost API docs (playbook_runs - getPlaybookRunMetadata) <https://developers.mattermost.com/api-documentation/#/operations/getPlaybookRunMetadata>`_

        """
        return self.client.get(f"/plugins/playbooks/api/v0/runs/{id}/metadata")

    def end_playbook_run(self, id: str):
        """End a playbook run

        id: ID of the playbook run to end.

        `Read in Mattermost API docs (playbook_runs - endPlaybookRun) <https://developers.mattermost.com/api-documentation/#/operations/endPlaybookRun>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/end")

    def restart_playbook_run(self, id: str):
        """Restart a playbook run

        id: ID of the playbook run to restart.

        `Read in Mattermost API docs (playbook_runs - restartPlaybookRun) <https://developers.mattermost.com/api-documentation/#/operations/restartPlaybookRun>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/restart")

    def status(self, id: str, message: str, reminder: float | None = None):
        """Update a playbook run's status

        id: ID of the playbook run to update.
        message: The status update message.
        reminder: The number of seconds until the system will send a reminder to the owner to update the status. No reminder will be scheduled if reminder is 0 or omitted.

        `Read in Mattermost API docs (playbook_runs - status) <https://developers.mattermost.com/api-documentation/#/operations/status>`_

        """
        __options = {"message": message, "reminder": reminder}
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/status", options=__options)

    def finish(self, id: str):
        """Finish a playbook

        id: ID of the playbook run to finish.

        `Read in Mattermost API docs (playbook_runs - finish) <https://developers.mattermost.com/api-documentation/#/operations/finish>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/finish")

    def change_owner(self, id: str, owner_id: str):
        """Update playbook run owner

        id: ID of the playbook run whose owner will be changed.
        owner_id: The user ID of the new owner.

        `Read in Mattermost API docs (playbook_runs - changeOwner) <https://developers.mattermost.com/api-documentation/#/operations/changeOwner>`_

        """
        __options = {"owner_id": owner_id}
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/owner", options=__options)

    def add_checklist_item(
        self,
        id: str,
        checklist: int,
        title: str,
        state: str | None = None,
        state_modified: int | None = None,
        assignee_id: str | None = None,
        assignee_modified: int | None = None,
        command: str | None = None,
        command_last_run: int | None = None,
        description: str | None = None,
    ):
        """Add an item to a playbook run's checklist

        id: ID of the playbook run whose checklist will be modified.
        checklist: Zero-based index of the checklist to modify.
        title: The title of the checklist item.
        state: The state of the checklist item. An empty string means that the item is not done.
        state_modified: The timestamp for the latest modification of the item's state, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item was never modified.
        assignee_id: The identifier of the user that has been assigned to complete this item. If the item has no assignee, this is an empty string.
        assignee_modified: The timestamp for the latest modification of the item's assignee, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the item never got an assignee.
        command: The slash command associated with this item. If the item has no slash command associated, this is an empty string
        command_last_run: The timestamp for the latest execution of the item's command, formatted as the number of milliseconds since the Unix epoch. It equals 0 if the command was never executed.
        description: A detailed description of the checklist item, formatted with Markdown.

        `Read in Mattermost API docs (playbook_runs - addChecklistItem) <https://developers.mattermost.com/api-documentation/#/operations/addChecklistItem>`_

        """
        __options = {
            "title": title,
            "state": state,
            "state_modified": state_modified,
            "assignee_id": assignee_id,
            "assignee_modified": assignee_modified,
            "command": command,
            "command_last_run": command_last_run,
            "description": description,
        }
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/add", options=__options)

    def reoder_checklist_item(self, id: str, checklist: int, item_num: int, new_location: int):
        """Reorder an item in a playbook run's checklist

        id: ID of the playbook run whose checklist will be modified.
        checklist: Zero-based index of the checklist to modify.
        item_num: Zero-based index of the item to reorder.
        new_location: Zero-based index of the new place to move the item to.

        `Read in Mattermost API docs (playbook_runs - reoderChecklistItem) <https://developers.mattermost.com/api-documentation/#/operations/reoderChecklistItem>`_

        """
        __options = {"item_num": item_num, "new_location": new_location}
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/reorder", options=__options)

    def item_rename(self, id: str, checklist: int, item: int, title: str, command: str):
        """Update an item of a playbook run's checklist

        id: ID of the playbook run whose checklist will be modified.
        checklist: Zero-based index of the checklist to modify.
        item: Zero-based index of the item to modify.
        title: The new title of the item.
        command: The new slash command of the item.

        `Read in Mattermost API docs (playbook_runs - itemRename) <https://developers.mattermost.com/api-documentation/#/operations/itemRename>`_

        """
        __options = {"title": title, "command": command}
        return self.client.put(
            f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}", options=__options
        )

    def item_delete(self, id: str, checklist: int, item: int):
        """Delete an item of a playbook run's checklist

        id: ID of the playbook run whose checklist will be modified.
        checklist: Zero-based index of the checklist to modify.
        item: Zero-based index of the item to modify.

        `Read in Mattermost API docs (playbook_runs - itemDelete) <https://developers.mattermost.com/api-documentation/#/operations/itemDelete>`_

        """
        return self.client.delete(f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}")

    def item_set_state(self, id: str, checklist: int, item: int, new_state: str = ""):
        """Update the state of an item

        id: ID of the playbook run whose checklist will be modified.
        checklist: Zero-based index of the checklist to modify.
        item: Zero-based index of the item to modify.
        new_state: The new state of the item.

        `Read in Mattermost API docs (playbook_runs - itemSetState) <https://developers.mattermost.com/api-documentation/#/operations/itemSetState>`_

        """
        __options = {"new_state": new_state}
        return self.client.put(
            f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/state", options=__options
        )

    def item_set_assignee(self, id: str, checklist: int, item: int, assignee_id: str):
        """Update the assignee of an item

        id: ID of the playbook run whose item will get a new assignee.
        checklist: Zero-based index of the checklist whose item will get a new assignee.
        item: Zero-based index of the item that will get a new assignee.
        assignee_id: The user ID of the new assignee of the item.

        `Read in Mattermost API docs (playbook_runs - itemSetAssignee) <https://developers.mattermost.com/api-documentation/#/operations/itemSetAssignee>`_

        """
        __options = {"assignee_id": assignee_id}
        return self.client.put(
            f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/assignee", options=__options
        )

    def item_run(self, id: str, checklist: int, item: int):
        """Run an item's slash command

        id: ID of the playbook run whose item will be executed.
        checklist: Zero-based index of the checklist whose item will be executed.
        item: Zero-based index of the item whose slash command will be executed.

        `Read in Mattermost API docs (playbook_runs - itemRun) <https://developers.mattermost.com/api-documentation/#/operations/itemRun>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/checklists/{checklist}/item/{item}/run")

    def get_run_property_fields(self, id: str, updated_since: int | None = None):
        """Get property fields for a playbook run

        id: ID of the playbook run to retrieve property fields from.
        updated_since: Filter results to only include property fields updated after this timestamp (Unix time in milliseconds).

        `Read in Mattermost API docs (playbook_runs - getRunPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/getRunPropertyFields>`_

        """
        __params = {"updated_since": updated_since}
        return self.client.get(f"/plugins/playbooks/api/v0/runs/{id}/property_fields", params=__params)

    def get_run_property_values(self, id: str, updated_since: int | None = None):
        """Get property values for a playbook run

        id: ID of the playbook run to retrieve property values from.
        updated_since: Filter results to only include property values updated after this timestamp (Unix time in milliseconds).

        `Read in Mattermost API docs (playbook_runs - getRunPropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/getRunPropertyValues>`_

        """
        __params = {"updated_since": updated_since}
        return self.client.get(f"/plugins/playbooks/api/v0/runs/{id}/property_values", params=__params)

    def set_run_property_value(self, id: str, field_id: str, options: Any | None = None):
        """Set a property value for a playbook run

        id: ID of the playbook run to set property value for.
        field_id: ID of the property field to set value for.

        `Read in Mattermost API docs (playbook_runs - setRunPropertyValue) <https://developers.mattermost.com/api-documentation/#/operations/setRunPropertyValue>`_

        """
        return self.client.put(f"/plugins/playbooks/api/v0/runs/{id}/property_fields/{field_id}/value", options=options)
