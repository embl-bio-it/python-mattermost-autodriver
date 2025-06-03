from ._base import Base

__all__ = ["Reactions"]


class Reactions(Base):

    def save_reaction(self, options):
        """Create a reaction
        `Read in Mattermost API docs (reactions - SaveReaction) <https://developers.mattermost.com/api-documentation/#/operations/SaveReaction>`_

        """
        return self.client.post("""/api/v4/reactions""", options=options)

    def get_reactions(self, post_id):
        """Get a list of reactions to a post

        post_id: ID of a post

        `Read in Mattermost API docs (reactions - GetReactions) <https://developers.mattermost.com/api-documentation/#/operations/GetReactions>`_

        """
        return self.client.get(f"/api/v4/posts/{post_id}/reactions")

    def delete_reaction(self, user_id, post_id, emoji_name):
        """Remove a reaction from a post

        user_id: ID of the user
        post_id: ID of the post
        emoji_name: emoji name

        `Read in Mattermost API docs (reactions - DeleteReaction) <https://developers.mattermost.com/api-documentation/#/operations/DeleteReaction>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/posts/{post_id}/reactions/{emoji_name}")

    def get_bulk_reactions(self, options):
        """Bulk get the reaction for posts
        `Read in Mattermost API docs (reactions - GetBulkReactions) <https://developers.mattermost.com/api-documentation/#/operations/GetBulkReactions>`_

        """
        return self.client.post("""/api/v4/posts/ids/reactions""", options=options)
