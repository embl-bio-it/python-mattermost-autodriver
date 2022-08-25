from .base import Base


class Status(Base):
    def get_user_status(self, user_id):
        """Get user status

        user_id: User ID
        """
        return self.client.get(f"/users/{user_id}/status")

    def update_user_status(self, user_id, options):
        """Update user status

        user_id: User ID
        user_id: User ID
        status: User status, can be ``online``, ``away``, ``offline`` and ``dnd``
        dnd_end_time: Time in epoch seconds at which a dnd status would be unset.
        """
        return self.client.put(f"/users/{user_id}/status", options=options)

    def get_users_statuses_by_ids(self, options):
        """Get user statuses by id"""
        return self.client.post("""/users/status/ids""", options=options)

    def update_user_custom_status(self, user_id, options):
        """Update user custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.
        """
        return self.client.put(f"/users/{user_id}/status/custom", options=options)

    def unset_user_custom_status(self, user_id):
        """Unsets user custom status

        user_id: User ID
        """
        return self.client.delete(f"/users/{user_id}/status/custom")

    def remove_recent_custom_status(self, user_id, params):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.
        """
        return self.client.delete(f"/users/{user_id}/status/custom/recent", params=params)

    def post_user_recent_custom_status_delete(self, user_id, options):
        """Delete user's recent custom status

        user_id: User ID
        emoji: Any emoji
        text: Any custom status text
        duration: Duration of custom status, can be ``thirty_minutes``, ``one_hour``, ``four_hours``, ``today``, ``this_week`` or ``date_and_time``
        expires_at: The time at which custom status should be expired. It should be in ISO format.
        """
        return self.client.post(f"/users/{user_id}/status/custom/recent/delete", options=options)
