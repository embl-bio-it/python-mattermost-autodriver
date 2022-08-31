from .base import Base


class OAuth(Base):
    def create_o_auth_app(self, options):
        """Register OAuth app

        name: The name of the client application
        description: A short description of the application
        icon_url: A URL to an icon to display with the application
        callback_urls: A list of callback URLs for the appliation
        homepage: A link to the website of the application
        is_trusted: Set this to ``true`` to skip asking users for permission

        `Read in Mattermost API docs (OAuth - CreateOAuthApp) <https://api.mattermost.com/#tag/OAuth/operation/CreateOAuthApp>`_
        """
        return self.client.post("""/oauth/apps""", options=options)

    def get_o_auth_apps(self, params=None):
        """Get OAuth apps

        page: The page to select.
        per_page: The number of apps per page.

        `Read in Mattermost API docs (OAuth - GetOAuthApps) <https://api.mattermost.com/#tag/OAuth/operation/GetOAuthApps>`_
        """
        return self.client.get("""/oauth/apps""", params=params)

    def get_o_auth_app(self, app_id):
        """Get an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (OAuth - GetOAuthApp) <https://api.mattermost.com/#tag/OAuth/operation/GetOAuthApp>`_
        """
        return self.client.get(f"/oauth/apps/{app_id}")

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

        `Read in Mattermost API docs (OAuth - UpdateOAuthApp) <https://api.mattermost.com/#tag/OAuth/operation/UpdateOAuthApp>`_
        """
        return self.client.put(f"/oauth/apps/{app_id}", options=options)

    def delete_o_auth_app(self, app_id):
        """Delete an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (OAuth - DeleteOAuthApp) <https://api.mattermost.com/#tag/OAuth/operation/DeleteOAuthApp>`_
        """
        return self.client.delete(f"/oauth/apps/{app_id}")

    def regenerate_o_auth_app_secret(self, app_id):
        """Regenerate OAuth app secret

        app_id: Application client id

        `Read in Mattermost API docs (OAuth - RegenerateOAuthAppSecret) <https://api.mattermost.com/#tag/OAuth/operation/RegenerateOAuthAppSecret>`_
        """
        return self.client.post(f"/oauth/apps/{app_id}/regen_secret")

    def get_o_auth_app_info(self, app_id):
        """Get info on an OAuth app

        app_id: Application client id

        `Read in Mattermost API docs (OAuth - GetOAuthAppInfo) <https://api.mattermost.com/#tag/OAuth/operation/GetOAuthAppInfo>`_
        """
        return self.client.get(f"/oauth/apps/{app_id}/info")

    def get_authorized_o_auth_apps_for_user(self, user_id, params=None):
        """Get authorized OAuth apps

        user_id: User GUID
        page: The page to select.
        per_page: The number of apps per page.

        `Read in Mattermost API docs (OAuth - GetAuthorizedOAuthAppsForUser) <https://api.mattermost.com/#tag/OAuth/operation/GetAuthorizedOAuthAppsForUser>`_
        """
        return self.client.get(f"/users/{user_id}/oauth/apps/authorized", params=params)
