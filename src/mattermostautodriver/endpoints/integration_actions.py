from ._base import Base, FileType
from typing import Any

__all__ = ["IntegrationActions"]


class IntegrationActions(Base):

    def open_interactive_dialog(self, trigger_id: str, url: str, dialog: dict[str, Any]):
        """Open a dialog

        trigger_id: Trigger ID provided by other action
        url: The URL to send the submitted dialog payload to
        dialog: Post object to create

        `Read in Mattermost API docs (integration_actions - OpenInteractiveDialog) <https://developers.mattermost.com/api-documentation/#/operations/OpenInteractiveDialog>`_

        """
        __options = {"trigger_id": trigger_id, "url": url, "dialog": dialog}
        return self.client.post("""/api/v4/actions/dialogs/open""", options=__options)

    def submit_interactive_dialog(
        self,
        url: str,
        channel_id: str,
        submission: dict[str, Any],
        team_id: str | None = None,
        callback_id: str | None = None,
        state: str | None = None,
        cancelled: bool | None = None,
        file_ids: list[str] | None = None,
    ):
        """Submit a dialog

        url: The URL to send the submitted dialog payload to
        channel_id: Channel ID the user submitted the dialog from
        team_id: Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team).

        submission: String map where keys are element names and values are the element input values
        callback_id: Callback ID sent when the dialog was opened
        state: State sent when the dialog was opened
        cancelled: Set to true if the dialog was cancelled
        file_ids: List of file IDs uploaded as part of the dialog submission. Each file must have been uploaded by the submitting user. A maximum of 10 file IDs may be submitted.


        `Read in Mattermost API docs (integration_actions - SubmitInteractiveDialog) <https://developers.mattermost.com/api-documentation/#/operations/SubmitInteractiveDialog>`_

        """
        __options = {
            "url": url,
            "channel_id": channel_id,
            "team_id": team_id,
            "submission": submission,
            "callback_id": callback_id,
            "state": state,
            "cancelled": cancelled,
            "file_ids": file_ids,
        }
        return self.client.post("""/api/v4/actions/dialogs/submit""", options=__options)

    def lookup_interactive_dialog(
        self,
        url: str,
        channel_id: str,
        submission: dict[str, Any],
        team_id: str | None = None,
        callback_id: str | None = None,
        state: str | None = None,
    ):
        """Lookup dialog elements

        url: The URL to send the lookup request to
        channel_id: Channel ID the user is performing the lookup from
        team_id: Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team).

        submission: String map where keys are element names and values are the element input values
        callback_id: Callback ID sent when the dialog was opened
        state: State sent when the dialog was opened

        `Read in Mattermost API docs (integration_actions - LookupInteractiveDialog) <https://developers.mattermost.com/api-documentation/#/operations/LookupInteractiveDialog>`_

        """
        __options = {
            "url": url,
            "channel_id": channel_id,
            "team_id": team_id,
            "submission": submission,
            "callback_id": callback_id,
            "state": state,
        }
        return self.client.post("""/api/v4/actions/dialogs/lookup""", options=__options)

    def execute_dialog_action(
        self, url: str, channel_id: str, context: dict[str, Any] | None = None, team_id: str | None = None
    ):
        """Execute a dialog action button

        url: The action button URL to send the action payload to. Must be a valid lookup URL.
        context: String map of context values configured on the action button, forwarded to the integration
        channel_id: Channel ID the user clicked the action button from
        team_id: Optional. The server resolves the authoritative team from the channel, so a client-supplied value is ignored. Empty for DM/GM channels (which have no team).


        `Read in Mattermost API docs (integration_actions - ExecuteDialogAction) <https://developers.mattermost.com/api-documentation/#/operations/ExecuteDialogAction>`_

        """
        __options = {"url": url, "context": context, "channel_id": channel_id, "team_id": team_id}
        return self.client.post("""/api/v4/actions/dialogs/execute""", options=__options)
