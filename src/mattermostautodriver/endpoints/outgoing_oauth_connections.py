from ._base import Base, FileType
from typing import Any

__all__ = ["OutgoingOauthConnections"]


class OutgoingOauthConnections(Base):

    def list_outgoing_o_auth_connections(self, team_id: str):
        """List all connections

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - ListOutgoingOAuthConnections) <https://developers.mattermost.com/api-documentation/#/operations/ListOutgoingOAuthConnections>`_

        """
        __params = {"team_id": team_id}
        return self.client.get("""/api/v4/oauth/outgoing_connections""", params=__params)

    def create_outgoing_o_auth_connection(self, team_id: str, options: Any | None = None):
        """Create a connection

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - CreateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/CreateOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.post("""/api/v4/oauth/outgoing_connections""", params=__params, options=options)

    def get_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, team_id: str):
        """Get a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID
        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - GetOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/GetOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.get(f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}", params=__params)

    def update_outgoing_o_auth_connection(
        self, outgoing_oauth_connection_id: str, team_id: str, options: Any | None = None
    ):
        """Update a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID
        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - UpdateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/UpdateOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.put(
            f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}", params=__params, options=options
        )

    def delete_outgoing_o_auth_connection(self, outgoing_oauth_connection_id: str, team_id: str):
        """Delete a connection

        outgoing_oauth_connection_id: Outgoing OAuth connection ID
        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - DeleteOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/DeleteOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.delete(f"/api/v4/oauth/outgoing_connections/{outgoing_oauth_connection_id}", params=__params)

    def validate_outgoing_o_auth_connection(self, team_id: str, options: Any | None = None):
        """Validate a connection configuration

        team_id: Current Team ID in integrations backstage

        `Read in Mattermost API docs (outgoing_oauth_connections - ValidateOutgoingOAuthConnection) <https://developers.mattermost.com/api-documentation/#/operations/ValidateOutgoingOAuthConnection>`_

        """
        __params = {"team_id": team_id}
        return self.client.post("""/api/v4/oauth/outgoing_connections/validate""", params=__params, options=options)
