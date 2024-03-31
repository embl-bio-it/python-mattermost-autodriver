from .base import Base


class OutgoingConnections(Base):

    def list_outgoing_o_auth_connections(self, params=None):
        """List all connections

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_connections - ListOutgoingOAuthConnections) <https://api.mattermost.com/#tag/outgoing_connections/operation/ListOutgoingOAuthConnections>`_

        """
        return self.client.get("""/api/v4/oauth/outgoing_connections""", params=params)

    def create_outgoing_o_auth_connection(self, options=None):
        """Create a connection
        `Read in Mattermost API docs (outgoing_connections - CreateOutgoingOAuthConnection) <https://api.mattermost.com/#tag/outgoing_connections/operation/CreateOutgoingOAuthConnection>`_

        """
        return self.client.post("""/api/v4/oauth/outgoing_connections""", options=options)

    def get_outgoing_o_auth_connection(self, params=None):
        """Get a connection

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_connections - GetOutgoingOAuthConnection) <https://api.mattermost.com/#tag/outgoing_connections/operation/GetOutgoingOAuthConnection>`_

        """
        return self.client.get(f"/api/v4/oauth/outgoing_connections/{connection_id}", params=params)

    def update_outgoing_o_auth_connection(self, options=None):
        """Update a connection
        `Read in Mattermost API docs (outgoing_connections - UpdateOutgoingOAuthConnection) <https://api.mattermost.com/#tag/outgoing_connections/operation/UpdateOutgoingOAuthConnection>`_

        """
        return self.client.put(f"/api/v4/oauth/outgoing_connections/{connection_id}", options=options)

    def delete_outgoing_o_auth_connection(self):
        """Delete a connection
        `Read in Mattermost API docs (outgoing_connections - DeleteOutgoingOAuthConnection) <https://api.mattermost.com/#tag/outgoing_connections/operation/DeleteOutgoingOAuthConnection>`_

        """
        return self.client.delete(f"/api/v4/oauth/outgoing_connections/{connection_id}")

    def validate_outgoing_o_auth_connection(self, options=None):
        """Validate a connection configuration
        `Read in Mattermost API docs (outgoing_connections - ValidateOutgoingOAuthConnection) <https://api.mattermost.com/#tag/outgoing_connections/operation/ValidateOutgoingOAuthConnection>`_

        """
        return self.client.post("""/api/v4/oauth/outgoing_connections/validate""", options=options)
