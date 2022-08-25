from .base import Base


class Commands(Base):
    def create_command(self, options):
        """Create a command

        team_id: Team ID to where the command should be created
        method: ``'P'`` for post request, ``'G'`` for get request
        trigger: Activation word to trigger the command
        url: The URL that the command will make the request
        """
        return self.client.post("""/commands""", options=options)

    def list_commands(self, params=None):
        """List commands for a team

        team_id: The team id.
        custom_only: To get only the custom commands. If set to false will get the custom
        if the user have access plus the system commands, otherwise just the system commands.

        """
        return self.client.get("""/commands""", params=params)

    def list_autocomplete_commands(self, team_id):
        """List autocomplete commands

        team_id: Team GUID
        """
        return self.client.get(f"/teams/{team_id}/commands/autocomplete")

    def list_command_autocomplete_suggestions(self, team_id, params=None):
        """List commands' autocomplete data

        team_id: Team GUID
        user_input: String inputted by the user.
        """
        return self.client.get(f"/teams/{team_id}/commands/autocomplete_suggestions", params=params)

    def get_command_by_id(self, command_id):
        """Get a command

        command_id: ID of the command to get
        """
        return self.client.get(f"/commands/{command_id}")

    def update_command(self, command_id, options):
        """Update a command

        command_id: ID of the command to update
        """
        return self.client.put(f"/commands/{command_id}", options=options)

    def delete_command(self, command_id):
        """Delete a command

        command_id: ID of the command to delete
        """
        return self.client.delete(f"/commands/{command_id}")

    def move_command(self, command_id, options):
        """Move a command

        command_id: ID of the command to move
        team_id: Destination teamId
        """
        return self.client.put(f"/commands/{command_id}/move", options=options)

    def regen_command_token(self, command_id):
        """Generate a new token

        command_id: ID of the command to generate the new token
        """
        return self.client.put(f"/commands/{command_id}/regen_token")

    def execute_command(self, options):
        """Execute a command

        channel_id: Channel Id where the command will execute
        command: The slash command to execute
        """
        return self.client.post("""/commands/execute""", options=options)
