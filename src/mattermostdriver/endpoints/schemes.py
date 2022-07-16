from .base import Base


class Schemes(Base):
    def get_schemes(self, params=None):
        """Get the schemes.

        scope: Limit the results returned to the provided scope, either `team` or `channel`.
        page: The page to select.
        per_page: The number of schemes per page.
        """
        return self.client.get("""/schemes""", params=params)

    def create_scheme(self, options):
        """Create a scheme

        name: The name of the scheme
        description: The description of the scheme
        scope: The scope of the scheme ("team" or "channel")
        """
        return self.client.post("""/schemes""", options=options)

    def get_scheme(self, scheme_id):
        """Get a scheme

        scheme_id: Scheme GUID
        """
        return self.client.get(f"/schemes/{scheme_id}")

    def delete_scheme(self, scheme_id):
        """Delete a scheme

        scheme_id: ID of the scheme to delete
        """
        return self.client.delete(f"/schemes/{scheme_id}")

    def patch_scheme(self, scheme_id, options):
        """Patch a scheme

        scheme_id: Scheme GUID
        name: The human readable name of the scheme
        description: The description of the scheme
        """
        return self.client.put(f"/schemes/{scheme_id}/patch", options=options)

    def get_teams_for_scheme(self, scheme_id, params=None):
        """Get a page of teams which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of teams per page.
        """
        return self.client.get(f"/schemes/{scheme_id}/teams", params=params)

    def get_channels_for_scheme(self, scheme_id, params=None):
        """Get a page of channels which use this scheme.

        scheme_id: Scheme GUID
        page: The page to select.
        per_page: The number of channels per page.
        """
        return self.client.get(f"/schemes/{scheme_id}/channels", params=params)
