from .base import Base
from typing import Any, BinaryIO


class Bots(Base):

    def convert_user_to_bot(self, user_id: str):
        """Convert a user into a bot

        user_id: User GUID

        `Read in Mattermost API docs (bots - ConvertUserToBot) <https://api.mattermost.com/#tag/bots/operation/ConvertUserToBot>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/convert_to_bot")

    def create_bot(self, username: str, display_name: str | None = None, description: str | None = None):
        """Create a bot

        username:
        display_name:
        description:

        `Read in Mattermost API docs (bots - CreateBot) <https://api.mattermost.com/#tag/bots/operation/CreateBot>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "username": username,
            "display_name": display_name,
            "description": description,
        }
        return self.client.post("""/api/v4/bots""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_bots(
        self,
        page: int | None = 0,
        per_page: int | None = 60,
        include_deleted: bool | None = None,
        only_orphaned: bool | None = None,
    ):
        """Get bots

        page: The page to select.
        per_page: The number of users per page.
        include_deleted: If deleted bots should be returned.
        only_orphaned: When true, only orphaned bots will be returned. A bot is considered orphaned if its owner has been deactivated.

        `Read in Mattermost API docs (bots - GetBots) <https://api.mattermost.com/#tag/bots/operation/GetBots>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "page": page,
            "per_page": per_page,
            "include_deleted": include_deleted,
            "only_orphaned": only_orphaned,
        }
        return self.client.get("""/api/v4/bots""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def patch_bot(
        self, bot_user_id: str, username: str, display_name: str | None = None, description: str | None = None
    ):
        """Patch a bot

        bot_user_id: Bot user ID
        username:
        display_name:
        description:

        `Read in Mattermost API docs (bots - PatchBot) <https://api.mattermost.com/#tag/bots/operation/PatchBot>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "username": username,
            "display_name": display_name,
            "description": description,
        }
        return self.client.put(f"/api/v4/bots/{bot_user_id}", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_bot(self, bot_user_id: str, include_deleted: bool | None = None):
        """Get a bot

        bot_user_id: Bot user ID
        include_deleted: If deleted bots should be returned.

        `Read in Mattermost API docs (bots - GetBot) <https://api.mattermost.com/#tag/bots/operation/GetBot>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"include_deleted": include_deleted}
        return self.client.get(f"/api/v4/bots/{bot_user_id}", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def disable_bot(self, bot_user_id: str):
        """Disable a bot

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - DisableBot) <https://api.mattermost.com/#tag/bots/operation/DisableBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/disable")

    def enable_bot(self, bot_user_id: str):
        """Enable a bot

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - EnableBot) <https://api.mattermost.com/#tag/bots/operation/EnableBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/enable")

    def assign_bot(self, bot_user_id: str, user_id: str):
        """Assign a bot to a user

        bot_user_id: Bot user ID
        user_id: The user ID to assign the bot to.

        `Read in Mattermost API docs (bots - AssignBot) <https://api.mattermost.com/#tag/bots/operation/AssignBot>`_

        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/assign/{user_id}")

    def get_bot_icon_image(self, bot_user_id: str):
        """Get bot's LHS icon

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - GetBotIconImage) <https://api.mattermost.com/#tag/bots/operation/GetBotIconImage>`_

        """
        return self.client.get(f"/api/v4/bots/{bot_user_id}/icon")

    def set_bot_icon_image(self, bot_user_id: str, image: BinaryIO):
        """Set bot's LHS icon image

        bot_user_id: Bot user ID
        image: SVG icon image to be uploaded

        `Read in Mattermost API docs (bots - SetBotIconImage) <https://api.mattermost.com/#tag/bots/operation/SetBotIconImage>`_

        """
        files_71f8b7431cd64fcfa0dabd300d0636d2 = {"image": image}
        return self.client.post(f"/api/v4/bots/{bot_user_id}/icon", files=files_71f8b7431cd64fcfa0dabd300d0636d2)

    def delete_bot_icon_image(self, bot_user_id: str):
        """Delete bot's LHS icon image

        bot_user_id: Bot user ID

        `Read in Mattermost API docs (bots - DeleteBotIconImage) <https://api.mattermost.com/#tag/bots/operation/DeleteBotIconImage>`_

        """
        return self.client.delete(f"/api/v4/bots/{bot_user_id}/icon")

    def convert_bot_to_user(
        self,
        bot_user_id: str,
        email: str | None = None,
        username: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        nickname: str | None = None,
        locale: str | None = None,
        position: str | None = None,
        props: dict[str, Any] | None = None,
        notify_props: Any | None = None,
    ):
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

        `Read in Mattermost API docs (bots - ConvertBotToUser) <https://api.mattermost.com/#tag/bots/operation/ConvertBotToUser>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "email": email,
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "locale": locale,
            "position": position,
            "props": props,
            "notify_props": notify_props,
        }
        return self.client.post(
            f"/api/v4/bots/{bot_user_id}/convert_to_user", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )
