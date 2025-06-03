from ._base import Base

__all__ = ["Status"]


class Status(Base):

    def get_user_status(self, user_id):
        """Get user status

        user_id: User ID

        `Read in Mattermost API docs (status - GetUserStatus) <https://developers.mattermost.com/api-documentation/#/operations/GetUserStatus>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/status")

    def update_user_status(self, user_id, options):
        """Update user status

        user_id: User ID
        user_id: User ID
        status: User status, can be ``online``, ``away``, ``offline`` and ``dnd``
        dnd_end_time: Time in epoch seconds at which a dnd status would be unset.

        `Read in Mattermost API docs (status - UpdateUserStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserStatus>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/status", options=options)

    def get_users_statuses_by_ids(self, options):
        """Get user statuses by id
        `Read in Mattermost API docs (status - GetUsersStatusesByIds) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersStatusesByIds>`_

        """
        return self.client.post("""/api/v4/users/status/ids""", options=options)

    def update_user_custom_status(self, user_id, options):
        """Update user custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - UpdateUserCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserCustomStatus>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/status/custom", options=options)

    def unset_user_custom_status(self, user_id):
        """Unsets user custom status

        user_id: User ID

        `Read in Mattermost API docs (status - UnsetUserCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/UnsetUserCustomStatus>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/status/custom")

    def remove_recent_custom_status(self, user_id, params):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - RemoveRecentCustomStatus) <https://developers.mattermost.com/api-documentation/#/operations/RemoveRecentCustomStatus>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/status/custom/recent", params=params)

    def post_user_recent_custom_status_delete(self, user_id, options):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.

        `Read in Mattermost API docs (status - PostUserRecentCustomStatusDelete) <https://developers.mattermost.com/api-documentation/#/operations/PostUserRecentCustomStatusDelete>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/status/custom/recent/delete", options=options)
