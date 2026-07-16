from ._base import Base, FileType
from typing import Any

__all__ = ["Oauth"]


class Oauth(Base):

    def list_outgoing_o_auth_connections(self, team_id: str):
        """List all connections

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (oauth - ListOutgoingOAuthConnections) <https://developers.mattermost.com/api-documentation/#/operations/ListOutgoingOAuthConnections>`_

        """
        __params = {"team_id": team_id}
        return self.client.get("""/api/v4/oauth/outgoing_connections""", params=__params)

    def create_outgoing_o_auth_connection(self, options: Any | None = None):
        """Create a connection
        `Read in Mattermost API docs (oauth - CreateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/CreateOutgoingOAuthConnection>`_

        """
        return self.client.post("""/api/v4/oauth/outgoing_connections""", options=options)

    def get_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, team_id: str):
        """Get a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID
        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (oauth - GetOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/GetOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.get(f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}", params=__params)

    def update_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, options: Any | None = None):
        """Update a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID

        `Read in Mattermost API docs (oauth - UpdateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/UpdateOutgoingOAuthConnection>`_

        """
        return self.client.put(f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}", options=options)

    def delete_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str):
        """Delete a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID

        `Read in Mattermost API docs (oauth - DeleteOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/DeleteOutgoingOAuthConnection>`_

        """
        return self.client.delete(f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}")

    def validate_outgoing_o_auth_connection(self, options: Any | None = None):
        """Validate a connection configuration
        `Read in Mattermost API docs (oauth - ValidateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/ValidateOutgoingOAuthConnection>`_

        """
        return self.client.post("""/api/v4/oauth/outgoing_connections/validate""", options=options)
