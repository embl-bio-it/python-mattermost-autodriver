from .base import Base
from typing import Any


class IntegrationActions(Base):

    def open_interactive_dialog(self, trigger_id: str, url: str, dialog: dict[str, Any]):
        """Open a dialog

        trigger_id: Trigger ID provided by other action
        url: The URL to send the submitted dialog payload to
        dialog: Post object to create

        `Read in Mattermost API docs (integration_actions - OpenInteractiveDialog) <https://api.mattermost.com/#tag/integration_actions/operation/OpenInteractiveDialog>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"trigger_id": trigger_id, "url": url, "dialog": dialog}
        return self.client.post("""/api/v4/actions/dialogs/open""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def submit_interactive_dialog(
        self,
        url: str,
        channel_id: str,
        team_id: str,
        submission: dict[str, Any],
        callback_id: str | None = None,
        state: str | None = None,
        cancelled: bool | None = None,
    ):
        """Submit a dialog

        url: The URL to send the submitted dialog payload to
        channel_id: Channel ID the user submitted the dialog from
        team_id: Team ID the user submitted the dialog from
        submission: String map where keys are element names and values are the element input values
        callback_id: Callback ID sent when the dialog was opened
        state: State sent when the dialog was opened
        cancelled: Set to true if the dialog was cancelled

        `Read in Mattermost API docs (integration_actions - SubmitInteractiveDialog) <https://api.mattermost.com/#tag/integration_actions/operation/SubmitInteractiveDialog>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "url": url,
            "channel_id": channel_id,
            "team_id": team_id,
            "submission": submission,
            "callback_id": callback_id,
            "state": state,
            "cancelled": cancelled,
        }
        return self.client.post("""/api/v4/actions/dialogs/submit""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)
