from ._base import Base

__all__ = ["Internal"]


class Internal(Base):

    def create_playbook_run_from_dialog(self, options=None):
        """Create a new playbook run from dialog

        type:
        url:
        callback_id: Callback ID provided by the integration.
        state: Stringified JSON with the post_id and the client_id.
        user_id: ID of the user who submitted the dialog.
        channel_id: ID of the channel the user was in when submitting the dialog.
        team_id: ID of the team the user was on when submitting the dialog.
        submission: Map of the dialog fields to their values
        cancelled: If the dialog was cancelled.

        `Read in Mattermost API docs (internal - createPlaybookRunFromDialog) <https://developers.mattermost.com/api-documentation/#/operations/createPlaybookRunFromDialog>`_

        """
        return self.client.post("""/plugins/playbooks/api/v0/runs/dialog""", options=options)

    def get_checklist_autocomplete(self, params=None):
        """Get autocomplete data for /playbook check

        channel_ID: ID of the channel the user is in.

        `Read in Mattermost API docs (internal - getChecklistAutocomplete) <https://developers.mattermost.com/api-documentation/#/operations/getChecklistAutocomplete>`_

        """
        return self.client.get("""/plugins/playbooks/api/v0/runs/checklist-autocomplete""", params=params)

    def end_playbook_run_dialog(self, id):
        """End a playbook run from dialog

        id: ID of the playbook run to end.

        `Read in Mattermost API docs (internal - endPlaybookRunDialog) <https://developers.mattermost.com/api-documentation/#/operations/endPlaybookRunDialog>`_

        """
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/end")

    def next_stage_dialog(self, id, options=None):
        """Go to next stage from dialog

        id: The PlaybookRun ID
        state: String representation of the zero-based index of the stage to go to.

        `Read in Mattermost API docs (internal - nextStageDialog) <https://developers.mattermost.com/api-documentation/#/operations/nextStageDialog>`_

        """
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/next-stage-dialog", options=options)
