from ._base import Base
from typing import Any, BinaryIO

__all__ = ["ContentFlagging"]


class ContentFlagging(Base):

    def get_cf_flag_config(self):
        """Get content flagging configuration
        `Read in Mattermost API docs (content_flagging - GetCFFlagConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetCFFlagConfig>`_

        """
        return self.client.get("""/api/v4/content_flagging/flag/config""")

    def get_cf_team_status(self, team_id: str):
        """Get content flagging status for a team

        team_id: The ID of the team to retrieve the content flagging status for

        `Read in Mattermost API docs (content_flagging - GetCFTeamStatus) <https://developers.mattermost.com/api-documentation/#/operations/GetCFTeamStatus>`_

        """
        return self.client.get(f"/api/v4/content_flagging/team/{team_id}/status")

    def post_cf_post_flag(self, post_id: str, reason: str | None = None, comment: str | None = None):
        """Flag a post

        post_id: The ID of the post to be flagged
        reason: The reason for flagging the post. This must be one of the configured reasons available for selection.
        comment: Comment from the user flagging the post.

        `Read in Mattermost API docs (content_flagging - PostCFPostFlag) <https://developers.mattermost.com/api-documentation/#/operations/PostCFPostFlag>`_

        """
        __options = {"reason": reason, "comment": comment}
        return self.client.post(f"/api/v4/content_flagging/post/{post_id}/flag", options=__options)

    def get_cf_fields(self):
        """Get content flagging property fields
        `Read in Mattermost API docs (content_flagging - GetCFFields) <https://developers.mattermost.com/api-documentation/#/operations/GetCFFields>`_

        """
        return self.client.get("""/api/v4/content_flagging/fields""")

    def get_cf_post_field_values(self, post_id: str):
        """Get content flagging property field values for a post

        post_id: The ID of the post to retrieve property field values for

        `Read in Mattermost API docs (content_flagging - GetCFPostFieldValues) <https://developers.mattermost.com/api-documentation/#/operations/GetCFPostFieldValues>`_

        """
        return self.client.get(f"/api/v4/content_flagging/post/{post_id}/field_values")

    def get_cf_post(self, post_id: str):
        """Get a flagged post with all its content.

        post_id: The ID of the post to retrieve

        `Read in Mattermost API docs (content_flagging - GetCFPost) <https://developers.mattermost.com/api-documentation/#/operations/GetCFPost>`_

        """
        return self.client.get(f"/api/v4/content_flagging/post/{post_id}")

    def remove_cf_post(self, post_id: str):
        """Remove a flagged post

        post_id: The ID of the post to be removed

        `Read in Mattermost API docs (content_flagging - RemoveCFPost) <https://developers.mattermost.com/api-documentation/#/operations/RemoveCFPost>`_

        """
        return self.client.put(f"/api/v4/content_flagging/post/{post_id}/remove")

    def keep_cf_post(self, post_id: str):
        """Keep a flagged post

        post_id: The ID of the post to be kept

        `Read in Mattermost API docs (content_flagging - KeepCFPost) <https://developers.mattermost.com/api-documentation/#/operations/KeepCFPost>`_

        """
        return self.client.put(f"/api/v4/content_flagging/post/{post_id}/keep")

    def get_cf_config(self):
        """Get the system content flagging configuration
        `Read in Mattermost API docs (content_flagging - GetCFConfig) <https://developers.mattermost.com/api-documentation/#/operations/GetCFConfig>`_

        """
        return self.client.get("""/api/v4/content_flagging/config""")

    def update_cf_config(self, options: Any):
        """Update the system content flagging configuration
        `Read in Mattermost API docs (content_flagging - UpdateCFConfig) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCFConfig>`_

        """
        return self.client.put("""/api/v4/content_flagging/config""", options=options)

    def search_cf_team_reviewers(self, team_id: str, term: str):
        """Search content reviewers in a team

        team_id: The ID of the team to search for content reviewers for
        term: The search term to filter content reviewers by

        `Read in Mattermost API docs (content_flagging - SearchCFTeamReviewers) <https://developers.mattermost.com/api-documentation/#/operations/SearchCFTeamReviewers>`_

        """
        __params = {"term": term}
        return self.client.get(f"/api/v4/content_flagging/team/{team_id}/reviewers/search", params=__params)

    def post_cf_post_reviewer(self, post_id: str, content_reviewer_id: str):
        """Assign a content reviewer to a flagged post

        post_id: The ID of the post to assign a content reviewer to
        content_reviewer_id: The ID of the user to be assigned as the content reviewer for the post

        `Read in Mattermost API docs (content_flagging - PostCFPostReviewer) <https://developers.mattermost.com/api-documentation/#/operations/PostCFPostReviewer>`_

        """
        return self.client.post(f"/api/v4/content_flagging/post/{post_id}/assign/{content_reviewer_id}")
