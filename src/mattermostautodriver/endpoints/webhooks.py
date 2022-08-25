from .base import Base


class Webhooks(Base):
    def create_incoming_webhook(self, options):
        """Create an incoming webhook

        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        user_id: The ID of the owner of the webhook if different than the requester. Required for [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook
        username: The username this incoming webhook will post as.
        icon_url: The profile picture this incoming webhook will use when posting.
        """
        return self.client.post("""/hooks/incoming""", options=options)

    def get_incoming_webhooks(self, params=None):
        """List incoming webhooks

        page: The page to select.
        per_page: The number of hooks per page.
        team_id: The ID of the team to get hooks for.
        """
        return self.client.get("""/hooks/incoming""", params=params)

    def get_incoming_webhook(self, hook_id):
        """Get an incoming webhook

        hook_id: Incoming Webhook GUID
        """
        return self.client.get(f"/hooks/incoming/{hook_id}")

    def delete_incoming_webhook(self, hook_id):
        """Delete an incoming webhook

        hook_id: Incoming webhook GUID
        """
        return self.client.delete(f"/hooks/incoming/{hook_id}")

    def update_incoming_webhook(self, hook_id, options):
        """Update an incoming webhook

        hook_id: Incoming Webhook GUID
        id: Incoming webhook GUID
        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook
        username: The username this incoming webhook will post as.
        icon_url: The profile picture this incoming webhook will use when posting.
        """
        return self.client.put(f"/hooks/incoming/{hook_id}", options=options)

    def create_outgoing_webhook(self, options):
        """Create an outgoing webhook

        team_id: The ID of the team that the webhook watchs
        channel_id: The ID of a public channel that the webhook watchs
        creator_id: The ID of the owner of the webhook if different than the requester. Required in [local mode](https://docs.mattermost.com/administration/mmctl-cli-tool.html#local-mode).
        description: The description for this outgoing webhook
        display_name: The display name for this outgoing webhook
        trigger_words: List of words for the webhook to trigger on
        trigger_when: When to trigger the webhook, `0` when a trigger word is present at all and `1` if the message starts with a trigger word
        callback_urls: The URLs to POST the payloads to when the webhook is triggered
        content_type: The format to POST the data in, either `application/json` or `application/x-www-form-urlencoded`
        """
        return self.client.post("""/hooks/outgoing""", options=options)

    def get_outgoing_webhooks(self, params=None):
        """List outgoing webhooks

        page: The page to select.
        per_page: The number of hooks per page.
        team_id: The ID of the team to get hooks for.
        channel_id: The ID of the channel to get hooks for.
        """
        return self.client.get("""/hooks/outgoing""", params=params)

    def get_outgoing_webhook(self, hook_id):
        """Get an outgoing webhook

        hook_id: Outgoing webhook GUID
        """
        return self.client.get(f"/hooks/outgoing/{hook_id}")

    def delete_outgoing_webhook(self, hook_id):
        """Delete an outgoing webhook

        hook_id: Outgoing webhook GUID
        """
        return self.client.delete(f"/hooks/outgoing/{hook_id}")

    def update_outgoing_webhook(self, hook_id, options):
        """Update an outgoing webhook

        hook_id: outgoing Webhook GUID
        id: Outgoing webhook GUID
        channel_id: The ID of a public channel or private group that receives the webhook payloads.
        display_name: The display name for this incoming webhook
        description: The description for this incoming webhook
        """
        return self.client.put(f"/hooks/outgoing/{hook_id}", options=options)

    def regen_outgoing_hook_token(self, hook_id):
        """Regenerate the token for the outgoing webhook.

        hook_id: Outgoing webhook GUID
        """
        return self.client.post(f"/hooks/outgoing/{hook_id}/regen_token")
