from .base import Base


class Users(Base):
    def login(self, options):
        """Login to Mattermost server

        id:
        login_id:
        token:
        device_id:
        ldap_only:
        password: The password used for email authentication.
        """
        return self.client.post("""/users/login""", options=options)

    def login_by_cws_token(self, options):
        """Auto-Login to Mattermost server using CWS token

        login_id:
        cws_token:
        """
        return self.client.post("""/users/login/cws""", options=options)

    def logout(self):
        """Logout from the Mattermost server"""
        return self.client.post("""/users/logout""")

    def create_user(self, options):
        """Create a user

        email:
        username:
        first_name:
        last_name:
        nickname:
        auth_data: Service-specific authentication data, such as email address.
        auth_service: The authentication service, one of "email", "gitlab", "ldap", "saml", "office365", "google", and "".
        password: The password used for email authentication.
        locale:
        props:
        notify_props:
        """
        return self.client.post("""/users""", options=options)

    def get_users(self, params=None):
        """Get users

        page: The page to select.
        per_page: The number of users per page. There is a maximum limit of 200 users per page.
        in_team: The ID of the team to get users for.
        not_in_team: The ID of the team to exclude users for. Must not be used with "in_team" query parameter.
        in_channel: The ID of the channel to get users for.
        not_in_channel: The ID of the channel to exclude users for. Must be used with "in_channel" query parameter.
        in_group: The ID of the group to get users for. Must have `manage_system` permission.
        group_constrained: When used with `not_in_channel` or `not_in_team`, returns only the users that are allowed to join the channel or team based on its group constrains.
        without_team: Whether or not to list users that are not on any team. This option takes precendence over `in_team`, `in_channel`, and `not_in_channel`.
        active: Whether or not to list only users that are active. This option cannot be used along with the `inactive` option.
        inactive: Whether or not to list only users that are deactivated. This option cannot be used along with the `active` option.
        role: Returns users that have this role.
        sort: Sort is only available in conjunction with certain options below. The paging parameter is also always available.

          ##### `in_team`
          Can be "", "last_activity_at" or "create_at".
          When left blank, sorting is done by username.
          __Minimum server version__: 4.0
          ##### `in_channel`
          Can be "", "status".
          When left blank, sorting is done by username. `status` will sort by User's current status (Online, Away, DND, Offline), then by Username.
          __Minimum server version__: 4.7

        roles: Comma separated string used to filter users based on any of the specified system roles

          Example: `?roles=system_admin,system_user` will return users that are either system admins or system users

          __Minimum server version__: 5.26

        channel_roles: Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with `in_channel`

          Example: `?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user` will return users that are only channel users and not admins or guests

          __Minimum server version__: 5.26

        team_roles: Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with `in_team`

          Example: `?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user` will return users that are only team users and not admins or guests

          __Minimum server version__: 5.26

        """
        return self.client.get("""/users""", params=params)

    def permanent_delete_all_users(self):
        """Permanent delete all users"""
        return self.client.delete("""/users""")

    def get_users_by_ids(self, options):
        """Get users by ids"""
        return self.client.post("""/users/ids""", options=options)

    def get_users_by_group_channel_ids(self, options):
        """Get users by group channels ids"""
        return self.client.post("""/users/group_channels""", options=options)

    def get_users_by_usernames(self, options):
        """Get users by usernames"""
        return self.client.post("""/users/usernames""", options=options)

    def search_users(self, options):
        """Search users

        term: The term to match against username, full name, nickname and email
        team_id: If provided, only search users on this team
        not_in_team_id: If provided, only search users not on this team
        in_channel_id: If provided, only search users in this channel
        not_in_channel_id: If provided, only search users not in this channel. Must specifiy `team_id` when using this option
        in_group_id: If provided, only search users in this group. Must have `manage_system` permission.
        group_constrained: When used with `not_in_channel_id` or `not_in_team_id`, returns only the users that are allowed to join the channel or team based on its group constrains.
        allow_inactive: When `true`, include deactivated users in the results
        without_team: Set this to `true` if you would like to search for users that are not on a team. This option takes precendence over `team_id`, `in_channel_id`, and `not_in_channel_id`.
        limit: The maximum number of users to return in the results

          __Available as of server version 5.6. Defaults to `100` if not provided or on an earlier server version.__

        """
        return self.client.post("""/users/search""", options=options)

    def autocomplete_users(self, params=None):
        """Autocomplete users

        team_id: Team ID
        channel_id: Channel ID
        name: Username, nickname first name or last name
        limit: The maximum number of users to return in each subresult

          __Available as of server version 5.6. Defaults to `100` if not provided or on an earlier server version.__

        """
        return self.client.get("""/users/autocomplete""", params=params)

    def get_known_users(self):
        """Get user IDs of known users"""
        return self.client.get("""/users/known""")

    def get_total_users_stats(self):
        """Get total count of users in the system"""
        return self.client.get("""/users/stats""")

    def get_total_users_stats_filtered(self, params=None):
        """Get total count of users in the system matching the specified filters

        in_team: The ID of the team to get user stats for.
        in_channel: The ID of the channel to get user stats for.
        include_deleted: If deleted accounts should be included in the count.
        include_bots: If bot accounts should be included in the count.
        roles: Comma separated string used to filter users based on any of the specified system roles

          Example: `?roles=system_admin,system_user` will include users that are either system admins or system users

        channel_roles: Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with `in_channel`

          Example: `?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user` will include users that are only channel users and not admins or guests

        team_roles: Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with `in_team`

          Example: `?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user` will include users that are only team users and not admins or guests

        """
        return self.client.get("""/users/stats/filtered""", params=params)

    def get_user(self, user_id):
        """Get a user

        user_id: User GUID. This can also be "me" which will point to the current user.
        """
        return self.client.get(f"/users/{user_id}")

    def update_user(self, user_id, options):
        """Update a user

        user_id: User GUID
        id:
        email:
        username:
        first_name:
        last_name:
        nickname:
        locale:
        position:
        timezone:
        props:
        notify_props:
        """
        return self.client.put(f"/users/{user_id}", options=options)

    def delete_user(self, user_id):
        """Deactivate a user account.

        user_id: User GUID
        """
        return self.client.delete(f"/users/{user_id}")

    def patch_user(self, user_id, options):
        """Patch a user

        user_id: User GUID
        email:
        username:
        first_name:
        last_name:
        nickname:
        locale:
        position:
        props:
        notify_props:
        """
        return self.client.put(f"/users/{user_id}/patch", options=options)

    def update_user_roles(self, user_id, options):
        """Update a user's roles

        user_id: User GUID
        roles:
        """
        return self.client.put(f"/users/{user_id}/roles", options=options)

    def update_user_active(self, user_id, options):
        """Update user active status

        user_id: User GUID
        active:
        """
        return self.client.put(f"/users/{user_id}/active", options=options)

    def get_profile_image(self, user_id, params=None):
        """Get user's profile image

        user_id: User GUID
        _: Not used by the server. Clients can pass in the last picture update time of the user to potentially take advantage of caching
        """
        return self.client.get(f"/users/{user_id}/image", params=params)

    def set_profile_image(self, user_id, files, data=None):
        """Set user's profile image

        user_id: User GUID
        image: The image to be uploaded
        """
        return self.client.post(f"/users/{user_id}/image", files=files, data=data)

    def set_default_profile_image(self, user_id):
        """Delete user's profile image

        user_id: User GUID
        """
        return self.client.delete(f"/users/{user_id}/image")

    def get_default_profile_image(self, user_id):
        """Return user's default (generated) profile image

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/image/default")

    def get_user_by_username(self, username):
        """Get a user by username

        username: Username
        """
        return self.client.get(f"/users/username/{username}")

    def reset_password(self, options):
        """Reset password

        code: The recovery code
        new_password: The new password for the user
        """
        return self.client.post("""/users/password/reset""", options=options)

    def update_user_mfa(self, user_id, options):
        """Update a user's MFA

        user_id: User GUID
        activate: Use `true` to activate, `false` to deactivate
        code: The code produced by your MFA client. Required if `activate` is true
        """
        return self.client.put(f"/users/{user_id}/mfa", options=options)

    def generate_mfa_secret(self, user_id):
        """Generate MFA secret

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/mfa/generate")

    def demote_user_to_guest(self, user_id):
        """Demote a user to a guest

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/demote")

    def promote_guest_to_user(self, user_id):
        """Promote a guest to user

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/promote")

    def convert_user_to_bot(self, user_id):
        """Convert a user into a bot

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/convert_to_bot")

    def check_user_mfa(self, options):
        """Check MFA

        login_id: The email or username used to login
        """
        return self.client.post("""/users/mfa""", options=options)

    def update_user_password(self, user_id, options):
        """Update a user's password

        user_id: User GUID
        current_password: The current password for the user
        new_password: The new password for the user
        """
        return self.client.put(f"/users/{user_id}/password", options=options)

    def send_password_reset_email(self, options):
        """Send password reset email

        email: The email of the user
        """
        return self.client.post("""/users/password/reset/send""", options=options)

    def get_user_by_email(self, email):
        """Get a user by email

        email: User Email
        """
        return self.client.get(f"/users/email/{email}")

    def get_sessions(self, user_id):
        """Get user's sessions

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/sessions")

    def revoke_session(self, user_id, options):
        """Revoke a user session

        user_id: User GUID
        session_id: The session GUID to revoke.
        """
        return self.client.post(f"/users/{user_id}/sessions/revoke", options=options)

    def revoke_all_sessions(self, user_id):
        """Revoke all active sessions for a user

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/sessions/revoke/all")

    def attach_device_id(self, options):
        """Attach mobile device

        device_id: Mobile device id. For Android prefix the id with `android:` and Apple with `apple:`
        """
        return self.client.put("""/users/sessions/device""", options=options)

    def get_user_audits(self, user_id):
        """Get user's audits

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/audits")

    def verify_user_email_without_token(self, user_id):
        """Verify user email by ID

        user_id: User GUID
        """
        return self.client.post(f"/users/{user_id}/email/verify/member")

    def verify_user_email(self, options):
        """Verify user email

        token: The token given to validate the email
        """
        return self.client.post("""/users/email/verify""", options=options)

    def send_verification_email(self, options):
        """Send verification email

        email: Email of a user
        """
        return self.client.post("""/users/email/verify/send""", options=options)

    def switch_account_type(self, options):
        """Switch login method

        current_service: The service the user currently uses to login
        new_service: The service the user will use to login
        email: The email of the user
        password: The password used with the current service
        mfa_code: The MFA code of the current service
        ldap_id: The LDAP/AD id of the user
        """
        return self.client.post("""/users/login/switch""", options=options)

    def create_user_access_token(self, user_id, options):
        """Create a user access token

        user_id: User GUID
        description: A description of the token usage
        """
        return self.client.post(f"/users/{user_id}/tokens", options=options)

    def get_user_access_tokens_for_user(self, user_id, params=None):
        """Get user access tokens

        user_id: User GUID
        page: The page to select.
        per_page: The number of tokens per page.
        """
        return self.client.get(f"/users/{user_id}/tokens", params=params)

    def get_user_access_tokens(self, params=None):
        """Get user access tokens

        page: The page to select.
        per_page: The number of tokens per page.
        """
        return self.client.get("""/users/tokens""", params=params)

    def revoke_user_access_token(self, options):
        """Revoke a user access token

        token_id: The user access token GUID to revoke
        """
        return self.client.post("""/users/tokens/revoke""", options=options)

    def get_user_access_token(self, token_id):
        """Get a user access token

        token_id: User access token GUID
        """
        return self.client.get(f"/users/tokens/{token_id}")

    def disable_user_access_token(self, options):
        """Disable personal access token

        token_id: The personal access token GUID to disable
        """
        return self.client.post("""/users/tokens/disable""", options=options)

    def enable_user_access_token(self, options):
        """Enable personal access token

        token_id: The personal access token GUID to enable
        """
        return self.client.post("""/users/tokens/enable""", options=options)

    def search_user_access_tokens(self, options):
        """Search tokens

        term: The search term to match against the token id, user id or username.
        """
        return self.client.post("""/users/tokens/search""", options=options)

    def update_user_auth(self, user_id, options):
        """Update a user's authentication method

        user_id: User GUID
        """
        return self.client.put(f"/users/{user_id}/auth", options=options)

    def register_terms_of_service_action(self, user_id, options):
        """Records user action when they accept or decline custom terms of service

        user_id: User GUID
        serviceTermsId: terms of service ID on which the user is acting on
        accepted: true or false, indicates whether the user accepted or rejected the terms of service.
        """
        return self.client.post(f"/users/{user_id}/terms_of_service", options=options)

    def get_user_terms_of_service(self, user_id):
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        user_id: User GUID
        """
        return self.client.get(f"/users/{user_id}/terms_of_service")

    def revoke_sessions_from_all_users(self):
        """Revoke all sessions from all users."""
        return self.client.post("""/users/sessions/revoke/all""")

    def publish_user_typing(self, user_id, options=None):
        """Publish a user typing websocket event.

        user_id: User GUID
        channel_id: The id of the channel to which to direct the typing event.
        parent_id: The optional id of the root post of the thread to which the user is replying. If unset, the typing event is directed at the entire channel.
        """
        return self.client.post(f"/users/{user_id}/typing", options=options)

    def get_uploads_for_user(self, user_id):
        """Get uploads for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        """
        return self.client.get(f"/users/{user_id}/uploads")

    def get_channel_members_with_team_data_for_user(self, user_id, params=None):
        """Get all channel members from all teams for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        page: Page specifies which part of the results to return, by PageSize.
        pageSize: PageSize specifies the size of the returned chunk of results.
        """
        return self.client.get(f"/users/{user_id}/channel_members", params=params)

    def migrate_auth_to_ldap(self, options=None):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:
        """
        return self.client.post("""/users/migrate_auth/ldap""", options=options)

    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:
        """
        return self.client.post("""/users/migrate_auth/saml""", options=options)

    def convert_bot_to_user(self, bot_user_id, options):
        """Convert a bot into a user

        bot_user_id: Bot user ID
        email:
        username:
        password:
        first_name:
        last_name:
        nickname:
        locale:
        position:
        props:
        notify_props:
        """
        return self.client.post(f"/bots/{bot_user_id}/convert_to_user", options=options)
