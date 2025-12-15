from ._base import Base

__all__ = ["OAuth"]


class OAuth(Base):

    def create_o_auth_app(self, options):
        """Register OAuth app

        name: The name of the client application
        description: A short description of the application
        icon_url: A URL to an icon to display with the application
        callback_urls: A list of callback URLs for the appliation
        homepage: A link to the website of the application
        is_trusted: Set this to ``true`` to skip asking users for permission
        is_public: Set this to ``true`` to create a public client (no client secret). Public clients must use PKCE for authorization.

        `Read in Mattermost API docs (o_auth - CreateOAuthApp) <https://developers.mattermost.com/api-documentation/#/operations/CreateOAuthApp>`_

        """
        return self.client.post("""/api/v4/oauth/apps""", options=options)

    def get_o_auth_apps(self, params=None):
        """Get OAuth apps

        page: The page to select.
        per_page: The number of apps per page.

        `Read in Mattermost API docs (o_auth - GetOAuthApps) <https://developers.mattermost.com/api-documentation/#/operations/GetOAuthApps>`_

        """
        return self.client.get("""/api/v4/oauth/apps""", params=params)

    def get_o_auth_app(self, app_id):
        """Get an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (o_auth - GetOAuthApp) <https://developers.mattermost.com/api-documentation/#/operations/GetOAuthApp>`_

        """
        return self.client.get(f"/api/v4/oauth/apps/{app_id}")

    def update_o_auth_app(self, app_id, options):
        """Update an OAuth app

        app_id: Application client id
        id: The id of the client application
        name: The name of the client application
        description: A short description of the application
        icon_url: A URL to an icon to display with the application
        callback_urls: A list of callback URLs for the appliation
        homepage: A link to the website of the application
        is_trusted: Set this to ``true`` to skip asking users for permission. It will be set to false if value is not provided.

        `Read in Mattermost API docs (o_auth - UpdateOAuthApp) <https://developers.mattermost.com/api-documentation/#/operations/UpdateOAuthApp>`_

        """
        return self.client.put(f"/api/v4/oauth/apps/{app_id}", options=options)

    def delete_o_auth_app(self, app_id):
        """Delete an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (o_auth - DeleteOAuthApp) <https://developers.mattermost.com/api-documentation/#/operations/DeleteOAuthApp>`_

        """
        return self.client.delete(f"/api/v4/oauth/apps/{app_id}")

    def regenerate_o_auth_app_secret(self, app_id):
        """Regenerate OAuth app secret

        app_id: Application client id

        `Read in Mattermost API docs (o_auth - RegenerateOAuthAppSecret) <https://developers.mattermost.com/api-documentation/#/operations/RegenerateOAuthAppSecret>`_

        """
        return self.client.post(f"/api/v4/oauth/apps/{app_id}/regen_secret")

    def get_o_auth_app_info(self, app_id):
        """Get info on an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (o_auth - GetOAuthAppInfo) <https://developers.mattermost.com/api-documentation/#/operations/GetOAuthAppInfo>`_

        """
        return self.client.get(f"/api/v4/oauth/apps/{app_id}/info")

    def get_authorization_server_metadata(self):
        """Get OAuth 2.0 Authorization Server Metadata
        `Read in Mattermost API docs (o_auth - GetAuthorizationServerMetadata) <https://developers.mattermost.com/api-documentation/#/operations/GetAuthorizationServerMetadata>`_

        """
        return self.client.get("""/.well-known/oauth-authorization-server""")

    def register_o_auth_client(self, options):
        """Register OAuth client using Dynamic Client Registration
        `Read in Mattermost API docs (o_auth - RegisterOAuthClient) <https://developers.mattermost.com/api-documentation/#/operations/RegisterOAuthClient>`_

        """
        return self.client.post("""/api/v4/oauth/apps/register""", options=options)

    def get_authorized_o_auth_apps_for_user(self, user_id, params=None):
        """Get authorized OAuth apps

        user_id: User GUID
        page: The page to select.
        per_page: The number of apps per page.

        `Read in Mattermost API docs (o_auth - GetAuthorizedOAuthAppsForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetAuthorizedOAuthAppsForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/oauth/apps/authorized", params=params)
