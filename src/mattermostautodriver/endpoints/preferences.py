from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Preferences"]


class Preferences(Base):

    def get_preferences(self, user_id: str):
        """Get the user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - GetPreferences) <https://developers.mattermost.com/api-documentation/#/operations/GetPreferences>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences")

    def update_preferences(self, user_id: str, options: list[Any]):
        """Save the user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - UpdatePreferences) <https://developers.mattermost.com/api-documentation/#/operations/UpdatePreferences>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/preferences", options=options)

    def delete_preferences(self, user_id: str, options: list[Any]):
        """Delete user's preferences

        user_id: User GUID

        `Read in Mattermost API docs (preferences - DeletePreferences) <https://developers.mattermost.com/api-documentation/#/operations/DeletePreferences>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/preferences/delete", options=options)

    def get_preferences_by_category(self, user_id: str, category: str):
        """List a user's preferences by category

        user_id: User GUID
        category: The category of a group of preferences

        `Read in Mattermost API docs (preferences - GetPreferencesByCategory) <https://developers.mattermost.com/api-documentation/#/operations/GetPreferencesByCategory>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences/{category}")

    def get_preferences_by_category_by_name(self, user_id: str, category: str, preference_name: str):
        """Get a specific user preference

        user_id: User GUID
        category: The category of a group of preferences
        preference_name: The name of the preference

        `Read in Mattermost API docs (preferences - GetPreferencesByCategoryByName) <https://developers.mattermost.com/api-documentation/#/operations/GetPreferencesByCategoryByName>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/preferences/{category}/name/{preference_name}")
