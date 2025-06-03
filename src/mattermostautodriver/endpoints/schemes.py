from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Schemes"]


class Schemes(Base):

    def get_schemes(self, scope: str | None = "", page: int | None = 0, per_page: int | None = 60):
        """Get the schemes.

        scope: Limit the results returned to the provided scope, either ``team`` or ``channel``.
        page: The page to select.
        per_page: The number of schemes per page.

        `Read in Mattermost API docs (schemes - GetSchemes) <https://developers.mattermost.com/api-documentation/#/operations/GetSchemes>`_

        """
        __params = {"scope": scope, "page": page, "per_page": per_page}
        return self.client.get("""/api/v4/schemes""", params=__params)

    def create_scheme(self, display_name: str, scope: str, name: str | None = None, description: str | None = None):
        """Create a scheme

        name: The name of the scheme
        display_name: The display name of the scheme
        description: The description of the scheme
        scope: The scope of the scheme ("team" or "channel")

        `Read in Mattermost API docs (schemes - CreateScheme) <https://developers.mattermost.com/api-documentation/#/operations/CreateScheme>`_

        """
        __options = {"name": name, "display_name": display_name, "description": description, "scope": scope}
        return self.client.post("""/api/v4/schemes""", options=__options)

    def get_scheme(self, scheme_id: str):
        """Get a scheme

        scheme_id: Scheme GUID

        `Read in Mattermost API docs (schemes - GetScheme) <https://developers.mattermost.com/api-documentation/#/operations/GetScheme>`_

        """
        return self.client.get(f"/api/v4/schemes/{scheme_id}")

    def delete_scheme(self, scheme_id: str):
        """Delete a scheme

        scheme_id: ID of the scheme to delete

        `Read in Mattermost API docs (schemes - DeleteScheme) <https://developers.mattermost.com/api-documentation/#/operations/DeleteScheme>`_

        """
        return self.client.delete(f"/api/v4/schemes/{scheme_id}")

    def patch_scheme(self, scheme_id: str, name: str | None = None, description: str | None = None):
        """Patch a scheme

        scheme_id: Scheme GUID
        name: The human readable name of the scheme
        description: The description of the scheme

        `Read in Mattermost API docs (schemes - PatchScheme) <https://developers.mattermost.com/api-documentation/#/operations/PatchScheme>`_

        """
        __options = {"name": name, "description": description}
        return self.client.put(f"/api/v4/schemes/{scheme_id}/patch", options=__options)

    def get_teams_for_scheme(self, scheme_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get a page of teams which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of teams per page.

        `Read in Mattermost API docs (schemes - GetTeamsForScheme) <https://developers.mattermost.com/api-documentation/#/operations/GetTeamsForScheme>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/schemes/{scheme_id}/teams", params=__params)

    def get_channels_for_scheme(self, scheme_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get a page of channels which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of channels per page.

        `Read in Mattermost API docs (schemes - GetChannelsForScheme) <https://developers.mattermost.com/api-documentation/#/operations/GetChannelsForScheme>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/schemes/{scheme_id}/channels", params=__params)
