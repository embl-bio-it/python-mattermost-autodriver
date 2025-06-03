from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Status"]


class Status(Base):

    def get_user_status(self, user_id: str):
        """Get user status

        user_id: User ID

        `Read in Mattermost API docs (status - GetUserStatus) <https://developers.mattermost.com/api-documentation/#/operations/GetUserStatus>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/status")

    def update_user_status(self, user_id: str, status: str, dnd_end_time: int | None = None):
        """Update user status

        user_id: User ID
        user_id: User ID
        status: User status, can be ``online``, ``away``, ``offline`` and ``dnd``
        dnd_end_time: Time in epoch seconds at which a dnd status would be unset.

        `Read in Mattermost API docs (status - UpdateUserStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserStatus>`_

        """
        __options = {"user_id": user_id, "status": status, "dnd_end_time": dnd_end_time}
        return self.client.put(f"/api/v4/users/{user_id}/status", options=__options)

    def get_users_statuses_by_ids(self, options: list[str]):
        """Get user statuses by id
        `Read in Mattermost API docs (status - GetUsersStatusesByIds) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersStatusesByIds>`_

        """
        return self.client.post("""/api/v4/users/status/ids""", options=options)

    def update_user_custom_status(
        self, user_id: str, emoji: str, text: str, duration: str | None = None, expires_at: str | None = None
    ):
        """Update user custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - UpdateUserCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserCustomStatus>`_

        """
        __options = {"emoji": emoji, "text": text, "duration": duration, "expires_at": expires_at}
        return self.client.put(f"/api/v4/users/{user_id}/status/custom", options=__options)

    def unset_user_custom_status(self, user_id: str):
        """Unsets user custom status

        user_id: User ID

        `Read in Mattermost API docs (status - UnsetUserCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/UnsetUserCustomStatus>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/status/custom")

    def remove_recent_custom_status(self, user_id: str, emoji: str, text: str, duration: str, expires_at: str):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - RemoveRecentCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/RemoveRecentCustomStatus>`_

        """
        __params = {"emoji": emoji, "text": text, "duration": duration, "expires_at": expires_at}
        return self.client.delete(f"/api/v4/users/{user_id}/status/custom/recent", params=__params)

    def post_user_recent_custom_status_delete(
        self, user_id: str, emoji: str, text: str, duration: str, expires_at: str
    ):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - PostUserRecentCustomStatusDelete) <https://developers.mattermost.com/api-documentation/#/operations/PostUserRecentCustomStatusDelete>`_

        """
        __options = {"emoji": emoji, "text": text, "duration": duration, "expires_at": expires_at}
        return self.client.post(f"/api/v4/users/{user_id}/status/custom/recent/delete", options=__options)
