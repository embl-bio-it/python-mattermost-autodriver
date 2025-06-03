from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Commands"]


class Commands(Base):

    def create_command(self, team_id: str, method: str, trigger: str, url: str):
        """Create a command

        team_id: Team ID to where the command should be created
        method: ``'P'`` for post request, ``'G'`` for get request
        trigger: Activation word to trigger the command
        url: The URL that the command will make the request

        `Read in Mattermost API docs (commands - CreateCommand) <https://developers.mattermost.com/api-documentation/#/operations/CreateCommand>`_

        """
        __options = {"team_id": team_id, "method": method, "trigger": trigger, "url": url}
        return self.client.post("""/api/v4/commands""", options=__options)

    def list_commands(self, team_id: str | None = None, custom_only: bool | None = False):
        """List commands for a team

        team_id: The team id.
        custom_only: To get only the custom commands. If set to false will get the custom
        if the user have access plus the system commands, otherwise just the system commands.


        `Read in Mattermost API docs (commands - ListCommands) <https://developers.mattermost.com/api-documentation/#/operations/ListCommands>`_

        """
        __params = {"team_id": team_id, "custom_only": custom_only}
        return self.client.get("""/api/v4/commands""", params=__params)

    def list_autocomplete_commands(self, team_id: str):
        """List autocomplete commands

        team_id: Team GUID

        `Read in Mattermost API docs (commands - ListAutocompleteCommands) <https://developers.mattermost.com/api-documentation/#/operations/ListAutocompleteCommands>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/commands/autocomplete")

    def list_command_autocomplete_suggestions(self, team_id: str, user_input: str):
        """List commands' autocomplete data

        team_id: Team GUID
        user_input: String inputted by the user.

        `Read in Mattermost API docs (commands - ListCommandAutocompleteSuggestions) <https://developers.mattermost.com/api-documentation/#/operations/ListCommandAutocompleteSuggestions>`_

        """
        __params = {"user_input": user_input}
        return self.client.get(f"/api/v4/teams/{team_id}/commands/autocomplete_suggestions", params=__params)

    def get_command_by_id(self, command_id: str):
        """Get a command

        command_id: ID of the command to get

        `Read in Mattermost API docs (commands - GetCommandById) <https://developers.mattermost.com/api-documentation/#/operations/GetCommandById>`_

        """
        return self.client.get(f"/api/v4/commands/{command_id}")

    def update_command(self, command_id: str, options: Any):
        """Update a command

        command_id: ID of the command to update

        `Read in Mattermost API docs (commands - UpdateCommand) <https://developers.mattermost.com/api-documentation/#/operations/UpdateCommand>`_

        """
        return self.client.put(f"/api/v4/commands/{command_id}", options=options)

    def delete_command(self, command_id: str):
        """Delete a command

        command_id: ID of the command to delete

        `Read in Mattermost API docs (commands - DeleteCommand) <https://developers.mattermost.com/api-documentation/#/operations/DeleteCommand>`_

        """
        return self.client.delete(f"/api/v4/commands/{command_id}")

    def move_command(self, command_id: str, team_id: str | None = None):
        """Move a command

        command_id: ID of the command to move
        team_id: Destination teamId

        `Read in Mattermost API docs (commands - MoveCommand) <https://developers.mattermost.com/api-documentation/#/operations/MoveCommand>`_

        """
        __options = {"team_id": team_id}
        return self.client.put(f"/api/v4/commands/{command_id}/move", options=__options)

    def regen_command_token(self, command_id: str):
        """Generate a new token

        command_id: ID of the command to generate the new token

        `Read in Mattermost API docs (commands - RegenCommandToken) <https://developers.mattermost.com/api-documentation/#/operations/RegenCommandToken>`_

        """
        return self.client.put(f"/api/v4/commands/{command_id}/regen_token")

    def execute_command(self, channel_id: str, command: str):
        """Execute a command

        channel_id: Channel Id where the command will execute
        command: The slash command to execute, including parameters. Eg, ``'/echo bounces around the room'``

        `Read in Mattermost API docs (commands - ExecuteCommand) <https://developers.mattermost.com/api-documentation/#/operations/ExecuteCommand>`_

        """
        __options = {"channel_id": channel_id, "command": command}
        return self.client.post("""/api/v4/commands/execute""", options=__options)
