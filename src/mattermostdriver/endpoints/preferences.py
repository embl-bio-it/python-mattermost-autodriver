from .base import Base


class Preferences(Base):
    def get_preferences(self, user_id):
        """Get the user's preferences

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/preferences")

    def update_preferences(self, user_id, options):
        """Save the user's preferences

        user_id: User GUID
        """
        return self.client.put(f"/users/{user_id}/preferences", options=options)

    def delete_preferences(self, user_id, options):
        """Delete user's preferences

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/preferences/delete", options=options)

    def get_preferences_by_category(self, user_id, category):
        """List a user's preferences by category

        user_id: User GUID
        category: The category of a group of preferences
        """
        return self.client.get(f"/users/{user_id}/preferences/{category}")

    def get_preferences_by_category_by_name(self, user_id, category, preference_name):
        """Get a specific user preference

        user_id: User GUID
        category: The category of a group of preferences
        preference_name: The name of the preference
        """
        return self.client.get(f"/users/{user_id}/preferences/{category}/name/{preference_name}")
