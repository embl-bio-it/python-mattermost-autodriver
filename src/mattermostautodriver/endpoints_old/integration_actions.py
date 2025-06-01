from ._base import Base

__all__ = ["IntegrationActions"]


class IntegrationActions(Base):

    def open_interactive_dialog(self, options):
        """Open a dialog

        trigger_id: Trigger ID provided by other action
        url: The URL to send the submitted dialog payload to
        dialog: Post object to create

        `Read in Mattermost API docs (integration_actions - OpenInteractiveDialog) <https://api.mattermost.com/#tag/integration_actions/operation/OpenInteractiveDialog>`_

        """
        return self.client.post("""/api/v4/actions/dialogs/open""", options=options)

    def submit_interactive_dialog(self, options):
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
        return self.client.post("""/api/v4/actions/dialogs/submit""", options=options)
