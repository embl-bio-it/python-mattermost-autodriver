from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Emoji"]


class Emoji(Base):

    def create_emoji(self, image: BinaryIO, emoji: str):
        """Create a custom emoji

        image: A file to be uploaded
        emoji: A JSON object containing a ``name`` field with the name of the emoji and a ``creator_id`` field with the id of the authenticated user.

        `Read in Mattermost API docs (emoji - CreateEmoji) <https://developers.mattermost.com/api-documentation/#/operations/CreateEmoji>`_

        """
        __files = {"image": image}
        __data = {"emoji": emoji}
        return self.client.post("""/api/v4/emoji""", files=__files, data=__data)

    def get_emoji_list(self, page: int | None = 0, per_page: int | None = 60, sort: str | None = ""):
        """Get a list of custom emoji

        page: The page to select.
        per_page: The number of emojis per page.
        sort: Either blank for no sorting or "name" to sort by emoji names. Minimum server version for sorting is 4.7.

        `Read in Mattermost API docs (emoji - GetEmojiList) <https://developers.mattermost.com/api-documentation/#/operations/GetEmojiList>`_

        """
        __params = {"page": page, "per_page": per_page, "sort": sort}
        return self.client.get("""/api/v4/emoji""", params=__params)

    def get_emoji(self, emoji_id: str):
        """Get a custom emoji

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - GetEmoji) <https://developers.mattermost.com/api-documentation/#/operations/GetEmoji>`_

        """
        return self.client.get(f"/api/v4/emoji/{emoji_id}")

    def delete_emoji(self, emoji_id: str):
        """Delete a custom emoji

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - DeleteEmoji) <https://developers.mattermost.com/api-documentation/#/operations/DeleteEmoji>`_

        """
        return self.client.delete(f"/api/v4/emoji/{emoji_id}")

    def get_emoji_by_name(self, emoji_name: str):
        """Get a custom emoji by name

        emoji_name: Emoji name

        `Read in Mattermost API docs (emoji - GetEmojiByName) <https://developers.mattermost.com/api-documentation/#/operations/GetEmojiByName>`_

        """
        return self.client.get(f"/api/v4/emoji/name/{emoji_name}")

    def get_emoji_image(self, emoji_id: str):
        """Get custom emoji image

        emoji_id: Emoji GUID

        `Read in Mattermost API docs (emoji - GetEmojiImage) <https://developers.mattermost.com/api-documentation/#/operations/GetEmojiImage>`_

        """
        return self.client.get(f"/api/v4/emoji/{emoji_id}/image")

    def search_emoji(self, term: str, prefix_only: str | None = None):
        """Search custom emoji

        term: The term to match against the emoji name.
        prefix_only: Set to only search for names starting with the search term.

        `Read in Mattermost API docs (emoji - SearchEmoji) <https://developers.mattermost.com/api-documentation/#/operations/SearchEmoji>`_

        """
        __options = {"term": term, "prefix_only": prefix_only}
        return self.client.post("""/api/v4/emoji/search""", options=__options)

    def autocomplete_emoji(self, name: str):
        """Autocomplete custom emoji

        name: The emoji name to search.

        `Read in Mattermost API docs (emoji - AutocompleteEmoji) <https://developers.mattermost.com/api-documentation/#/operations/AutocompleteEmoji>`_

        """
        __params = {"name": name}
        return self.client.get("""/api/v4/emoji/autocomplete""", params=__params)

    def get_emojis_by_names(self, options: list[str]):
        """Get custom emojis by name
        `Read in Mattermost API docs (emoji - GetEmojisByNames) <https://developers.mattermost.com/api-documentation/#/operations/GetEmojisByNames>`_

        """
        return self.client.post("""/api/v4/emoji/names""", options=options)
