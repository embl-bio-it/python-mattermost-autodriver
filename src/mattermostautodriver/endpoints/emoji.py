from .base import Base


class Emoji(Base):
    def create_emoji(self, files, data=None):
        """Create a custom emoji

        image: A file to be uploaded
        emoji: A JSON object containing a `name` field with the name of the emoji and a `creator_id` field with the id of the authenticated user.
        """
        return self.client.post("""/emoji""", files=files, data=data)

    def get_emoji_list(self, params=None):
        """Get a list of custom emoji

        page: The page to select.
        per_page: The number of emojis per page.
        sort: Either blank for no sorting or "name" to sort by emoji names. Minimum server version for sorting is 4.7.
        """
        return self.client.get("""/emoji""", params=params)

    def get_emoji(self, emoji_id):
        """Get a custom emoji

        emoji_id: Emoji GUID
        """
        return self.client.get(f"/emoji/{emoji_id}")

    def delete_emoji(self, emoji_id):
        """Delete a custom emoji

        emoji_id: Emoji GUID
        """
        return self.client.delete(f"/emoji/{emoji_id}")

    def get_emoji_by_name(self, emoji_name):
        """Get a custom emoji by name

        emoji_name: Emoji name
        """
        return self.client.get(f"/emoji/name/{emoji_name}")

    def get_emoji_image(self, emoji_id):
        """Get custom emoji image

        emoji_id: Emoji GUID
        """
        return self.client.get(f"/emoji/{emoji_id}/image")

    def search_emoji(self, options):
        """Search custom emoji

        term: The term to match against the emoji name.
        prefix_only: Set to only search for names starting with the search term.
        """
        return self.client.post("""/emoji/search""", options=options)

    def autocomplete_emoji(self, params=None):
        """Autocomplete custom emoji

        name: The emoji name to search.
        """
        return self.client.get("""/emoji/autocomplete""", params=params)
