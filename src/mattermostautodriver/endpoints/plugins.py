from .base import Base


class Plugins(Base):
    def upload_plugin(self, files, data=None):
        """Upload plugin

        plugin: The plugin image to be uploaded
        force: Set to 'true' to overwrite a previously installed plugin with the same ID, if any
        """
        return self.client.post("""/plugins""", files=files, data=data)

    def get_plugins(self):
        """Get plugins"""
        return self.client.get("""/plugins""")

    def install_plugin_from_url(self):
        """Install plugin from url"""
        return self.client.post("""/plugins/install_from_url""")

    def remove_plugin(self, plugin_id):
        """Remove plugin

        plugin_id: Id of the plugin to be removed
        """
        return self.client.delete(f"/plugins/{plugin_id}")

    def enable_plugin(self, plugin_id):
        """Enable plugin

        plugin_id: Id of the plugin to be enabled
        """
        return self.client.post(f"/plugins/{plugin_id}/enable")

    def disable_plugin(self, plugin_id):
        """Disable plugin

        plugin_id: Id of the plugin to be disabled
        """
        return self.client.post(f"/plugins/{plugin_id}/disable")

    def get_webapp_plugins(self):
        """Get webapp plugins"""
        return self.client.get("""/plugins/webapp""")

    def get_plugin_statuses(self):
        """Get plugins status"""
        return self.client.get("""/plugins/statuses""")

    def install_marketplace_plugin(self, options):
        """Installs a marketplace plugin

        id: The ID of the plugin to install.
        version: The version of the plugin to install.
        """
        return self.client.post("""/plugins/marketplace""", options=options)

    def get_marketplace_plugins(self, params=None):
        """Gets all the marketplace plugins

        page: Page number to be fetched. (not yet implemented)
        per_page: Number of item per page. (not yet implemented)
        filter: Set to filter plugins by ID, name, or description.
        server_version: Set to filter minimum plugin server version. (not yet implemented)
        local_only: Set true to only retrieve local plugins.
        """
        return self.client.get("""/plugins/marketplace""", params=params)

    def get_marketplace_visited_by_admin(self):
        """Get if the Plugin Marketplace has been visited by at least an admin."""
        return self.client.get("""/plugins/marketplace/first_admin_visit""")
