from .base import Base


class Bots(Base):
    def convert_user_to_bot(self, user_id):
        """Convert a user into a bot

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/convert_to_bot")

    def create_bot(self, options):
        """Create a bot

        username:
        display_name:
        description:
        """
        return self.client.post("""/bots""", options=options)

    def get_bots(self, params=None):
        """Get bots

        page: The page to select.
        per_page: The number of users per page. There is a maximum limit of 200 users per page.
        include_deleted: If deleted bots should be returned.
        only_orphaned: When true, only orphaned bots will be returned. A bot is consitered orphaned if it's owner has been deactivated.
        """
        return self.client.get("""/bots""", params=params)

    def patch_bot(self, bot_user_id, options):
        """Patch a bot

        bot_user_id: Bot user ID
        username:
        display_name:
        description:
        """
        return self.client.put(f"/bots/{bot_user_id}", options=options)

    def get_bot(self, bot_user_id, params=None):
        """Get a bot

        bot_user_id: Bot user ID
        include_deleted: If deleted bots should be returned.
        """
        return self.client.get(f"/bots/{bot_user_id}", params=params)

    def disable_bot(self, bot_user_id):
        """Disable a bot

        bot_user_id: Bot user ID
        """
        return self.client.post(f"/bots/{bot_user_id}/disable")

    def enable_bot(self, bot_user_id):
        """Enable a bot

        bot_user_id: Bot user ID
        """
        return self.client.post(f"/bots/{bot_user_id}/enable")

    def assign_bot(self, bot_user_id, user_id):
        """Assign a bot to a user

        bot_user_id: Bot user ID
        user_id: The user ID to assign the bot to.
        """
        return self.client.post(f"/bots/{bot_user_id}/assign/{user_id}")

    def get_bot_icon_image(self, bot_user_id):
        """Get bot's LHS icon

        bot_user_id: Bot user ID
        """
        return self.client.get(f"/bots/{bot_user_id}/icon")

    def set_bot_icon_image(self, bot_user_id, data=None):
        """Set bot's LHS icon image

        bot_user_id: Bot user ID
        image: SVG icon image to be uploaded
        """
        return self.client.post(f"/bots/{bot_user_id}/icon", data=data)

    def delete_bot_icon_image(self, bot_user_id):
        """Delete bot's LHS icon image

        bot_user_id: Bot user ID
        """
        return self.client.delete(f"/bots/{bot_user_id}/icon")

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
        """
        return self.client.post(f"/bots/{bot_user_id}/convert_to_user", options=options)
