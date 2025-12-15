from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Webhooks"]


class Webhooks(Base):

    def create_incoming_webhook(
        self,
        channel_id: str,
        user_id: str | None = None,
        display_name: str | None = None,
        description: str | None = None,
        username: str | None = None,
        icon_url: str | None = None,
        channel_locked: bool | None = None,
    ):
        """Create an incoming webhook

        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        user_id: The ID of the owner of the webhook if different than the requester. Required for [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook
        username: The username this incoming webhook will post as.
        icon_url: The profile picture this incoming webhook will use when posting.
        channel_locked: Whether the webhook is locked to the channel.

        `Read in Mattermost API docs (webhooks - CreateIncomingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/CreateIncomingWebhook>`_

        """
        __options = {
            "channel_id": channel_id,
            "user_id": user_id,
            "display_name": display_name,
            "description": description,
            "username": username,
            "icon_url": icon_url,
            "channel_locked": channel_locked,
        }
        return self.client.post("""/api/v4/hooks/incoming""", options=__options)

    def get_incoming_webhooks(
        self,
        page: int | None = 0,
        per_page: int | None = 60,
        team_id: str | None = None,
        include_total_count: bool | None = False,
    ):
        """List incoming webhooks

        page: The page to select.
        per_page: The number of hooks per page.
        team_id: The ID of the team to get hooks for.
        include_total_count: Appends a total count of returned hooks inside the response object - ex: ``{ "incoming_webhooks": [], "total_count": 0 }``.

        `Read in Mattermost API docs (webhooks - GetIncomingWebhooks) <https://developers.mattermost.com/api-documentation/#/operations/GetIncomingWebhooks>`_

        """
        __params = {"page": page, "per_page": per_page, "team_id": team_id, "include_total_count": include_total_count}
        return self.client.get("""/api/v4/hooks/incoming""", params=__params)

    def get_incoming_webhook(self, hook_id: str):
        """Get an incoming webhook

        hook_id: Incoming Webhook GUID

        `Read in Mattermost API docs (webhooks - GetIncomingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/GetIncomingWebhook>`_

        """
        return self.client.get(f"/api/v4/hooks/incoming/{hook_id}")

    def delete_incoming_webhook(self, hook_id: str):
        """Delete an incoming webhook

        hook_id: Incoming webhook GUID

        `Read in Mattermost API docs (webhooks - DeleteIncomingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/DeleteIncomingWebhook>`_

        """
        return self.client.delete(f"/api/v4/hooks/incoming/{hook_id}")

    def update_incoming_webhook(
        self,
        hook_id: str,
        id: str,
        channel_id: str,
        display_name: str,
        description: str,
        username: str | None = None,
        icon_url: str | None = None,
        channel_locked: bool | None = None,
    ):
        """Update an incoming webhook

        hook_id: Incoming Webhook GUID
        id: Incoming webhook GUID
        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook
        username: The username this incoming webhook will post as.
        icon_url: The profile picture this incoming webhook will use when posting.
        channel_locked: Whether the webhook is locked to the channel.

        `Read in Mattermost API docs (webhooks - UpdateIncomingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/UpdateIncomingWebhook>`_

        """
        __options = {
            "id": id,
            "channel_id": channel_id,
            "display_name": display_name,
            "description": description,
            "username": username,
            "icon_url": icon_url,
            "channel_locked": channel_locked,
        }
        return self.client.put(f"/api/v4/hooks/incoming/{hook_id}", options=__options)

    def create_outgoing_webhook(
        self,
        team_id: str,
        display_name: str,
        trigger_words: list[str],
        callback_urls: list[str],
        channel_id: str | None = None,
        creator_id: str | None = None,
        description: str | None = None,
        trigger_when: int | None = None,
        content_type: str | None = "application/x-www-form-urlencoded",
    ):
        """Create an outgoing webhook

        team_id: The ID of the team that the webhook watchs
        channel_id: The ID of a public channel that the webhook watchs
        creator_id: The ID of the owner of the webhook if different than the requester. Required in [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
        description: The description for this outgoing webhook
        display_name: The display name for this outgoing webhook
        trigger_words: List of words for the webhook to trigger on
        trigger_when: When to trigger the webhook, ``0`` when a trigger word is present at all and ``1`` if the message starts with a trigger word
        callback_urls: The URLs to POST the payloads to when the webhook is triggered
        content_type: The format to POST the data in, either ``application/json`` or ``application/x-www-form-urlencoded``

        `Read in Mattermost API docs (webhooks - CreateOutgoingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/CreateOutgoingWebhook>`_

        """
        __options = {
            "team_id": team_id,
            "channel_id": channel_id,
            "creator_id": creator_id,
            "description": description,
            "display_name": display_name,
            "trigger_words": trigger_words,
            "trigger_when": trigger_when,
            "callback_urls": callback_urls,
            "content_type": content_type,
        }
        return self.client.post("""/api/v4/hooks/outgoing""", options=__options)

    def get_outgoing_webhooks(
        self, page: int | None = 0, per_page: int | None = 60, team_id: str | None = None, channel_id: str | None = None
    ):
        """List outgoing webhooks

        page: The page to select.
        per_page: The number of hooks per page.
        team_id: The ID of the team to get hooks for.
        channel_id: The ID of the channel to get hooks for.

        `Read in Mattermost API docs (webhooks - GetOutgoingWebhooks) <https://developers.mattermost.com/api-documentation/#/operations/GetOutgoingWebhooks>`_

        """
        __params = {"page": page, "per_page": per_page, "team_id": team_id, "channel_id": channel_id}
        return self.client.get("""/api/v4/hooks/outgoing""", params=__params)

    def get_outgoing_webhook(self, hook_id: str):
        """Get an outgoing webhook

        hook_id: Outgoing webhook GUID

        `Read in Mattermost API docs (webhooks - GetOutgoingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/GetOutgoingWebhook>`_

        """
        return self.client.get(f"/api/v4/hooks/outgoing/{hook_id}")

    def delete_outgoing_webhook(self, hook_id: str):
        """Delete an outgoing webhook

        hook_id: Outgoing webhook GUID

        `Read in Mattermost API docs (webhooks - DeleteOutgoingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/DeleteOutgoingWebhook>`_

        """
        return self.client.delete(f"/api/v4/hooks/outgoing/{hook_id}")

    def update_outgoing_webhook(self, hook_id: str, id: str, channel_id: str, display_name: str, description: str):
        """Update an outgoing webhook

        hook_id: outgoing Webhook GUID
        id: Outgoing webhook GUID
        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook

        `Read in Mattermost API docs (webhooks - UpdateOutgoingWebhook) <https://developers.mattermost.com/api-documentation/#/operations/UpdateOutgoingWebhook>`_

        """
        __options = {"id": id, "channel_id": channel_id, "display_name": display_name, "description": description}
        return self.client.put(f"/api/v4/hooks/outgoing/{hook_id}", options=__options)

    def regen_outgoing_hook_token(self, hook_id: str):
        """Regenerate the token for the outgoing webhook.

        hook_id: Outgoing webhook GUID

        `Read in Mattermost API docs (webhooks - RegenOutgoingHookToken) <https://developers.mattermost.com/api-documentation/#/operations/RegenOutgoingHookToken>`_

        """
        return self.client.post(f"/api/v4/hooks/outgoing/{hook_id}/regen_token")
