from .base import Base
from typing import Any, BinaryIO


class Commands(Base):

    def create_command(self, team_id: str, method: str, trigger: str, url: str):
        """Create a command

        team_id: Team ID to where the command should be created
        method: ``'P'`` for post request, ``'G'`` for get request
        trigger: Activation word to trigger the command
        url: The URL that the command will make the request

        `Read in Mattermost API docs (commands - CreateCommand) <https://api.mattermost.com/#tag/commands/operation/CreateCommand>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {
            "team_id": team_id,
            "method": method,
            "trigger": trigger,
            "url": url,
        }
        return self.client.post("""/api/v4/commands""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def list_commands(self, team_id: str | None = None, custom_only: bool | None = False):
        """List commands for a team

        team_id: The team id.
        custom_only: To get only the custom commands. If set to false will get the custom
        if the user have access plus the system commands, otherwise just the system commands.


        `Read in Mattermost API docs (commands - ListCommands) <https://api.mattermost.com/#tag/commands/operation/ListCommands>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"team_id": team_id, "custom_only": custom_only}
        return self.client.get("""/api/v4/commands""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def list_autocomplete_commands(self, team_id: str):
        """List autocomplete commands

        team_id: Team GUID

        `Read in Mattermost API docs (commands - ListAutocompleteCommands) <https://api.mattermost.com/#tag/commands/operation/ListAutocompleteCommands>`_

        """
        return self.client.get(f"/api/v4/teams/{team_id}/commands/autocomplete")

    def list_command_autocomplete_suggestions(self, team_id: str, user_input: str):
        """List commands' autocomplete data

        team_id: Team GUID
        user_input: String inputted by the user.

        `Read in Mattermost API docs (commands - ListCommandAutocompleteSuggestions) <https://api.mattermost.com/#tag/commands/operation/ListCommandAutocompleteSuggestions>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"user_input": user_input}
        return self.client.get(
            f"/api/v4/teams/{team_id}/commands/autocomplete_suggestions", params=params_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def get_command_by_id(self, command_id: str):
        """Get a command

        command_id: ID of the command to get

        `Read in Mattermost API docs (commands - GetCommandById) <https://api.mattermost.com/#tag/commands/operation/GetCommandById>`_

        """
        return self.client.get(f"/api/v4/commands/{command_id}")

    def update_command(self, command_id: str, options: Any):
        """Update a command

        command_id: ID of the command to update

        `Read in Mattermost API docs (commands - UpdateCommand) <https://api.mattermost.com/#tag/commands/operation/UpdateCommand>`_

        """
        return self.client.put(f"/api/v4/commands/{command_id}", options=options)

    def delete_command(self, command_id: str):
        """Delete a command

        command_id: ID of the command to delete

        `Read in Mattermost API docs (commands - DeleteCommand) <https://api.mattermost.com/#tag/commands/operation/DeleteCommand>`_

        """
        return self.client.delete(f"/api/v4/commands/{command_id}")

    def move_command(self, command_id: str, team_id: str | None = None):
        """Move a command

        command_id: ID of the command to move
        team_id: Destination teamId

        `Read in Mattermost API docs (commands - MoveCommand) <https://api.mattermost.com/#tag/commands/operation/MoveCommand>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"team_id": team_id}
        return self.client.put(f"/api/v4/commands/{command_id}/move", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def regen_command_token(self, command_id: str):
        """Generate a new token

        command_id: ID of the command to generate the new token

        `Read in Mattermost API docs (commands - RegenCommandToken) <https://api.mattermost.com/#tag/commands/operation/RegenCommandToken>`_

        """
        return self.client.put(f"/api/v4/commands/{command_id}/regen_token")

    def execute_command(self, channel_id: str, command: str):
        """Execute a command

        channel_id: Channel Id where the command will execute
        command: The slash command to execute, including parameters. Eg, ``'/echo bounces around the room'``

        `Read in Mattermost API docs (commands - ExecuteCommand) <https://api.mattermost.com/#tag/commands/operation/ExecuteCommand>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"channel_id": channel_id, "command": command}
        return self.client.post("""/api/v4/commands/execute""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)
