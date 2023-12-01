from .base import Base


class Emoji(Base):
    def create_emoji(self, files, data=None):
        """Create a custom emoji

        image: A file to be uploaded
        emoji: A JSON object containing a ``name`` field with the name of the emoji and a ``creator_id`` field with the id of the authenticated user.

        `Read in Mattermost API docs (emoji - CreateEmoji) <https://api.mattermost.com/#tag/emoji/operation/CreateEmoji>`_
        """
        return self.client.post("""/api/v4/emoji""", files=files, data=data)

    def get_emoji_list(self, params=None):
        """Get a list of custom emoji

        page: The page to select.
        per_page: The number of emojis per page.
        sort: Either blank for no sorting or "name" to sort by emoji names. Minimum server version for sorting is 4.7.

        `Read in Mattermost API docs (emoji - GetEmojiList) <https://api.mattermost.com/#tag/emoji/operation/GetEmojiList>`_
        """
        return self.client.get("""/api/v4/emoji""", params=params)

    def get_emoji(self, emoji_id):
        """Get a custom emoji

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - GetEmoji) <https://api.mattermost.com/#tag/emoji/operation/GetEmoji>`_
        """
        return self.client.get(f"/api/v4/emoji/{emoji_id}")

    def delete_emoji(self, emoji_id):
        """Delete a custom emoji

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - DeleteEmoji) <https://api.mattermost.com/#tag/emoji/operation/DeleteEmoji>`_
        """
        return self.client.delete(f"/api/v4/emoji/{emoji_id}")

    def get_emoji_by_name(self, emoji_name):
        """Get a custom emoji by name

        emoji_name: Emoji name

        `Read in Mattermost API docs (emoji - GetEmojiByName) <https://api.mattermost.com/#tag/emoji/operation/GetEmojiByName>`_
        """
        return self.client.get(f"/api/v4/emoji/name/{emoji_name}")

    def get_emoji_image(self, emoji_id):
        """Get custom emoji image

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - GetEmojiImage) <https://api.mattermost.com/#tag/emoji/operation/GetEmojiImage>`_
        """
        return self.client.get(f"/api/v4/emoji/{emoji_id}/image")

    def search_emoji(self, options):
        """Search custom emoji

        term: The term to match against the emoji name.
        prefix_only: Set to only search for names starting with the search term.

        `Read in Mattermost API docs (emoji - SearchEmoji) <https://api.mattermost.com/#tag/emoji/operation/SearchEmoji>`_
        """
        return self.client.post("""/api/v4/emoji/search""", options=options)

    def autocomplete_emoji(self, params=None):
        """Autocomplete custom emoji

        name: The emoji name to search.

        `Read in Mattermost API docs (emoji - AutocompleteEmoji) <https://api.mattermost.com/#tag/emoji/operation/AutocompleteEmoji>`_
        """
        return self.client.get("""/api/v4/emoji/autocomplete""", params=params)

    def get_emojis_by_names(self, options):
        """Get custom emojis by name
        `Read in Mattermost API docs (emoji - GetEmojisByNames) <https://api.mattermost.com/#tag/emoji/operation/GetEmojisByNames>`_
        """
        return self.client.post("""/api/v4/emoji/names""", options=options)
