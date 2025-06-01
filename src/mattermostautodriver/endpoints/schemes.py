from .base import Base
from typing import Any, BinaryIO


class Schemes(Base):

    def get_schemes(self, scope: str | None = "", page: int | None = 0, per_page: int | None = 60):
        """Get the schemes.

        scope: Limit the results returned to the provided scope, either ``team`` or ``channel``.
        page: The page to select.
        per_page: The number of schemes per page.

        `Read in Mattermost API docs (schemes - GetSchemes) <https://api.mattermost.com/#tag/schemes/operation/GetSchemes>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"scope": scope, "page": page, "per_page": per_page}
        return self.client.get("""/api/v4/schemes""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def create_scheme(self, display_name: str, scope: str, name: str | None = None, description: str | None = None):
        """Create a scheme

        name: The name of the scheme
        display_name: The display name of the scheme
        description: The description of the scheme
        scope: The scope of the scheme ("team" or "channel")

        `Read in Mattermost API docs (schemes - CreateScheme) <https://api.mattermost.com/#tag/schemes/operation/CreateScheme>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "name": name,
            "display_name": display_name,
            "description": description,
            "scope": scope,
        }
        return self.client.post("""/api/v4/schemes""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_scheme(self, scheme_id: str):
        """Get a scheme

        scheme_id: Scheme GUID

        `Read in Mattermost API docs (schemes - GetScheme) <https://api.mattermost.com/#tag/schemes/operation/GetScheme>`_

        """
        return self.client.get(f"/api/v4/schemes/{scheme_id}")

    def delete_scheme(self, scheme_id: str):
        """Delete a scheme

        scheme_id: ID of the scheme to delete

        `Read in Mattermost API docs (schemes - DeleteScheme) <https://api.mattermost.com/#tag/schemes/operation/DeleteScheme>`_

        """
        return self.client.delete(f"/api/v4/schemes/{scheme_id}")

    def patch_scheme(self, scheme_id: str, name: str | None = None, description: str | None = None):
        """Patch a scheme

        scheme_id: Scheme GUID
        name: The human readable name of the scheme
        description: The description of the scheme

        `Read in Mattermost API docs (schemes - PatchScheme) <https://api.mattermost.com/#tag/schemes/operation/PatchScheme>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"name": name, "description": description}
        return self.client.put(f"/api/v4/schemes/{scheme_id}/patch", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_teams_for_scheme(self, scheme_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get a page of teams which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of teams per page.

        `Read in Mattermost API docs (schemes - GetTeamsForScheme) <https://api.mattermost.com/#tag/schemes/operation/GetTeamsForScheme>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/schemes/{scheme_id}/teams", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_channels_for_scheme(self, scheme_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get a page of channels which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of channels per page.

        `Read in Mattermost API docs (schemes - GetChannelsForScheme) <https://api.mattermost.com/#tag/schemes/operation/GetChannelsForScheme>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/schemes/{scheme_id}/channels", params=params_71f8b7431cd64fcfa0dabd300d0636d2)
