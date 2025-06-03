from ._base import Base

__all__ = ["Bots"]


class Bots(Base):

    def convert_user_to_bot(self, user_id):
        """Convert a user into a bot

        user_id: User GUID

        `Read in Mattermost API docs (bots - ConvertUserToBot) <https://developers.mattermost.com/api-documentation/#/operations/ConvertUserToBot>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/convert_to_bot")

    def create_bot(self, options):
        """Create a bot

        username:
        display_name:
        description:

        `Read in Mattermost API docs (bots - CreateBot) <https://developers.mattermost.com/api-documentation/#/operations/CreateBot>`_

        """
        return self.client.post("""/api/v4/bots""", options=options)

    def get_bots(self, params=None):
        """Get bots

        page: The page to select.
        per_page: The number of users per page.
        include_deleted: If deleted bots should be returned.
        only_orphaned: When true, only orphaned bots will be returned. A bot is considered orphaned if its owner has been deactivated.

        `Read in Mattermost API docs (bots - GetBots) <https://developers.mattermost.com/api-documentation/#/operations/GetBots>`_

        """
        return self.client.get("""/api/v4/bots""", params=params)

    def patch_bot(self, bot_user_id, options):
        """Patch a bot

        bot_user_id: Bot user ID
        username:
        display_name:
        description:

        `Read in Mattermost API docs (bots - PatchBot) <https://developers.mattermost.com/api-documentation/#/operations/PatchBot>`_

        """
        return self.client.put(f"/api/v4/bots/{bot_user_id}", options=options)

    def get_bot(self, bot_user_id, params=None):
        """Get a bot

        bot_user_id: Bot user ID
        include_deleted: If deleted bots should be returned.

        `Read in Mattermost API docs (bots - GetBot) <https://developers.mattermost.com/api-documentation/#/operations/GetBot>`_

        """
        return self.client.get(f"/api/v4/bots/{bot_user_id}", params=params)

    def disable_bot(self, bot_user_id):
        """Disable a bot

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - DisableBot) <https://developers.mattermost.com/api-documentation/#/operations/DisableBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/disable")

    def enable_bot(self, bot_user_id):
        """Enable a bot

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - EnableBot) <https://developers.mattermost.com/api-documentation/#/operations/EnableBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/enable")

    def assign_bot(self, bot_user_id, user_id):
        """Assign a bot to a user

        bot_user_id: Bot user ID
        user_id: The user ID to assign the bot to.

        `Read in Mattermost API docs (bots - AssignBot) <https://developers.mattermost.com/api-documentation/#/operations/AssignBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/assign/{user_id}")

    def get_bot_icon_image(self, bot_user_id):
        """Get bot's LHS icon

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - GetBotIconImage) <https://developers.mattermost.com/api-documentation/#/operations/GetBotIconImage>`_

        """
        return self.client.get(f"/api/v4/bots/{bot_user_id}/icon")

    def set_bot_icon_image(self, bot_user_id, files, data=None):
        """Set bot's LHS icon image

        bot_user_id: Bot user ID
        image: SVG icon image to be uploaded

        `Read in Mattermost API docs (bots - SetBotIconImage) <https://developers.mattermost.com/api-documentation/#/operations/SetBotIconImage>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/icon", files=files, data=data)

    def delete_bot_icon_image(self, bot_user_id):
        """Delete bot's LHS icon image

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - DeleteBotIconImage) <https://developers.mattermost.com/api-documentation/#/operations/DeleteBotIconImage>`_

        """
        return self.client.delete(f"/api/v4/bots/{bot_user_id}/icon")

    def convert_bot_to_user(self, bot_user_id, options):
        """Convert a bot into a user

        bot_user_id: Bot user ID
        email:
        username:
        password:
        first_name:
        last_name:
        nickname:
        locale:
        position:
        props:
        notify_props:

        `Read in Mattermost API docs (bots - ConvertBotToUser) <https://developers.mattermost.com/api-documentation/#/operations/ConvertBotToUser>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/convert_to_user", options=options)
