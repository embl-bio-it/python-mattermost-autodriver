from .base import Base
from typing import Any, BinaryIO


class Plugins(Base):

    def upload_plugin(self, plugin: BinaryIO, force: str | None = None):
        """Upload plugin

        plugin: The plugin image to be uploaded
        force: Set to 'true' to overwrite a previously installed plugin with the same ID, if any

        `Read in Mattermost API docs (plugins - UploadPlugin) <https://api.mattermost.com/#tag/plugins/operation/UploadPlugin>`_

        """
        files_71f8b7431cd64fcfa0dabd300d0636d2 = {"plugin": plugin}
        data_71f8b7431cd64fcfa0dabd300d0636d2 = {"force": force}
        return self.client.post(
            """/api/v4/plugins""",
            files=files_71f8b7431cd64fcfa0dabd300d0636d2,
            data=data_71f8b7431cd64fcfa0dabd300d0636d2,
        )

    def get_plugins(self):
        """Get plugins
        `Read in Mattermost API docs (plugins - GetPlugins) <https://api.mattermost.com/#tag/plugins/operation/GetPlugins>`_

        """
        return self.client.get("""/api/v4/plugins""")

    def install_plugin_from_url(self):
        """Install plugin from url
        `Read in Mattermost API docs (plugins - InstallPluginFromUrl) <https://api.mattermost.com/#tag/plugins/operation/InstallPluginFromUrl>`_

        """
        return self.client.post("""/api/v4/plugins/install_from_url""")

    def remove_plugin(self, plugin_id: str):
        """Remove plugin

        plugin_id: Id of the plugin to be removed

        `Read in Mattermost API docs (plugins - RemovePlugin) <https://api.mattermost.com/#tag/plugins/operation/RemovePlugin>`_

        """
        return self.client.delete(f"/api/v4/plugins/{plugin_id}")

    def enable_plugin(self, plugin_id: str):
        """Enable plugin

        plugin_id: Id of the plugin to be enabled

        `Read in Mattermost API docs (plugins - EnablePlugin) <https://api.mattermost.com/#tag/plugins/operation/EnablePlugin>`_

        """
        return self.client.post(f"/api/v4/plugins/{plugin_id}/enable")

    def disable_plugin(self, plugin_id: str):
        """Disable plugin

        plugin_id: Id of the plugin to be disabled

        `Read in Mattermost API docs (plugins - DisablePlugin) <https://api.mattermost.com/#tag/plugins/operation/DisablePlugin>`_

        """
        return self.client.post(f"/api/v4/plugins/{plugin_id}/disable")

    def get_webapp_plugins(self):
        """Get webapp plugins
        `Read in Mattermost API docs (plugins - GetWebappPlugins) <https://api.mattermost.com/#tag/plugins/operation/GetWebappPlugins>`_

        """
        return self.client.get("""/api/v4/plugins/webapp""")

    def get_plugin_statuses(self):
        """Get plugins status
        `Read in Mattermost API docs (plugins - GetPluginStatuses) <https://api.mattermost.com/#tag/plugins/operation/GetPluginStatuses>`_

        """
        return self.client.get("""/api/v4/plugins/statuses""")

    def install_marketplace_plugin(self, id: str, version: str):
        """Installs a marketplace plugin

        id: The ID of the plugin to install.
        version: The version of the plugin to install.

        `Read in Mattermost API docs (plugins - InstallMarketplacePlugin) <https://api.mattermost.com/#tag/plugins/operation/InstallMarketplacePlugin>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"id": id, "version": version}
        return self.client.post("""/api/v4/plugins/marketplace""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_marketplace_plugins(
        self,
        page: int | None = None,
        per_page: int | None = None,
        filter: str | None = None,
        server_version: str | None = None,
        local_only: bool | None = None,
    ):
        """Gets all the marketplace plugins

        page: Page number to be fetched. (not yet implemented)
        per_page: Number of item per page. (not yet implemented)
        filter: Set to filter plugins by ID, name, or description.
        server_version: Set to filter minimum plugin server version. (not yet implemented)
        local_only: Set true to only retrieve local plugins.

        `Read in Mattermost API docs (plugins - GetMarketplacePlugins) <https://api.mattermost.com/#tag/plugins/operation/GetMarketplacePlugins>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "page": page,
            "per_page": per_page,
            "filter": filter,
            "server_version": server_version,
            "local_only": local_only,
        }
        return self.client.get("""/api/v4/plugins/marketplace""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_marketplace_visited_by_admin(self):
        """Get if the Plugin Marketplace has been visited by at least an admin.
        `Read in Mattermost API docs (plugins - GetMarketplaceVisitedByAdmin) <https://api.mattermost.com/#tag/plugins/operation/GetMarketplaceVisitedByAdmin>`_

        """
        return self.client.get("""/api/v4/plugins/marketplace/first_admin_visit""")
