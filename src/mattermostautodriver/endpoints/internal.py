from .base import Base
from typing import Any


class Internal(Base):

    def create_playbook_run_from_dialog(
        self,
        type: str | None = None,
        url: str | None = None,
        callback_id: str | None = None,
        state: str | None = None,
        user_id: str | None = None,
        channel_id: str | None = None,
        team_id: str | None = None,
        submission: dict[str, Any] | None = None,
        cancelled: bool | None = None,
    ):
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

        `Read in Mattermost API docs (Internal - createPlaybookRunFromDialog) <https://api.mattermost.com/#tag/Internal/operation/createPlaybookRunFromDialog>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "type": type,
            "url": url,
            "callback_id": callback_id,
            "state": state,
            "user_id": user_id,
            "channel_id": channel_id,
            "team_id": team_id,
            "submission": submission,
            "cancelled": cancelled,
        }
        return self.client.post(
            """/plugins/playbooks/api/v0/runs/dialog""", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def get_checklist_autocomplete(self, channel_ID: str):
        """Get autocomplete data for /playbook check

        channel_ID: ID of the channel the user is in.

        `Read in Mattermost API docs (Internal - getChecklistAutocomplete) <https://api.mattermost.com/#tag/Internal/operation/getChecklistAutocomplete>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"channel_ID": channel_ID}
        return self.client.get(
            """/plugins/playbooks/api/v0/runs/checklist-autocomplete""", params=params_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def end_playbook_run_dialog(self, id: str):
        """End a playbook run from dialog

        id: ID of the playbook run to end.

        `Read in Mattermost API docs (Internal - endPlaybookRunDialog) <https://api.mattermost.com/#tag/Internal/operation/endPlaybookRunDialog>`_

        """
        return self.client.post(f"/plugins/playbooks/api/v0/runs/{id}/end")

    def next_stage_dialog(self, id: str, state: str | None = None):
        """Go to next stage from dialog

        id: The PlaybookRun ID
        state: String representation of the zero-based index of the stage to go to.

        `Read in Mattermost API docs (Internal - nextStageDialog) <https://api.mattermost.com/#tag/Internal/operation/nextStageDialog>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"state": state}
        return self.client.post(
            f"/plugins/playbooks/api/v0/runs/{id}/next-stage-dialog", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )
