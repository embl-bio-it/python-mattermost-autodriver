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

        `Read in Mattermost API docs (users - Login) <https://api.mattermost.com/#tag/users/operation/Login>`_
        """
        return self.client.post("""/api/v4/users/login""", options=options)

    def login_by_cws_token(self, options):
        """Auto-Login to Mattermost server using CWS token

        login_id:
        cws_token:

        `Read in Mattermost API docs (users - LoginByCwsToken) <https://api.mattermost.com/#tag/users/operation/LoginByCwsToken>`_
        """
        return self.client.post("""/api/v4/users/login/cws""", options=options)

    def logout(self):
        """Logout from the Mattermost server
        `Read in Mattermost API docs (users - Logout) <https://api.mattermost.com/#tag/users/operation/Logout>`_
        """
        return self.client.post("""/api/v4/users/logout""")

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

        `Read in Mattermost API docs (users - CreateUser) <https://api.mattermost.com/#tag/users/operation/CreateUser>`_
        """
        return self.client.post("""/api/v4/users""", options=options)

    def get_users(self, params=None):
        """Get users

        page: The page to select.
        per_page: The number of users per page. There is a maximum limit of 200 users per page.
        in_team: The ID of the team to get users for.
        not_in_team: The ID of the team to exclude users for. Must not be used with "in_team" query parameter.
        in_channel: The ID of the channel to get users for.
        not_in_channel: The ID of the channel to exclude users for. Must be used with "in_channel" query parameter.
        in_group: The ID of the group to get users for. Must have ``manage_system`` permission.
        group_constrained: When used with ``not_in_channel`` or ``not_in_team``, returns only the users that are allowed to join the channel or team based on its group constrains.
        without_team: Whether or not to list users that are not on any team. This option takes precendence over ``in_team``, ``in_channel``, and ``not_in_channel``.
        active: Whether or not to list only users that are active. This option cannot be used along with the ``inactive`` option.
        inactive: Whether or not to list only users that are deactivated. This option cannot be used along with the ``active`` option.
        role: Returns users that have this role.
        sort: Sort is only available in conjunction with certain options below. The paging parameter is also always available.

        ##### ``in_team``
        Can be "", "last_activity_at" or "create_at".
        When left blank, sorting is done by username.
        *Minimum server version*: 4.0
        ##### ``in_channel``
        Can be "", "status".
        When left blank, sorting is done by username. ``status`` will sort by User's current status (Online, Away, DND, Offline), then by Username.
        *Minimum server version*: 4.7
        ##### ``in_group``
        Can be "", "display_name".
        When left blank, sorting is done by username. ``display_name`` will sort alphabetically by user's display name.
        *Minimum server version*: 7.7

        roles: Comma separated string used to filter users based on any of the specified system roles

        Example: ``?roles=system_admin,system_user`` will return users that are either system admins or system users

        *Minimum server version*: 5.26

        channel_roles: Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with ``in_channel``

        Example: ``?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user`` will return users that are only channel users and not admins or guests

        *Minimum server version*: 5.26

        team_roles: Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with ``in_team``

        Example: ``?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user`` will return users that are only team users and not admins or guests

        *Minimum server version*: 5.26


        `Read in Mattermost API docs (users - GetUsers) <https://api.mattermost.com/#tag/users/operation/GetUsers>`_
        """
        return self.client.get("""/api/v4/users""", params=params)

    def permanent_delete_all_users(self):
        """Permanent delete all users
        `Read in Mattermost API docs (users - PermanentDeleteAllUsers) <https://api.mattermost.com/#tag/users/operation/PermanentDeleteAllUsers>`_
        """
        return self.client.delete("""/api/v4/users""")

    def get_users_by_ids(self, options):
        """Get users by ids
        `Read in Mattermost API docs (users - GetUsersByIds) <https://api.mattermost.com/#tag/users/operation/GetUsersByIds>`_
        """
        return self.client.post("""/api/v4/users/ids""", options=options)

    def get_users_by_group_channel_ids(self, options):
        """Get users by group channels ids
        `Read in Mattermost API docs (users - GetUsersByGroupChannelIds) <https://api.mattermost.com/#tag/users/operation/GetUsersByGroupChannelIds>`_
        """
        return self.client.post("""/api/v4/users/group_channels""", options=options)

    def get_users_by_usernames(self, options):
        """Get users by usernames
        `Read in Mattermost API docs (users - GetUsersByUsernames) <https://api.mattermost.com/#tag/users/operation/GetUsersByUsernames>`_
        """
        return self.client.post("""/api/v4/users/usernames""", options=options)

    def search_users(self, options):
        """Search users

        term: The term to match against username, full name, nickname and email
        team_id: If provided, only search users on this team
        not_in_team_id: If provided, only search users not on this team
        in_channel_id: If provided, only search users in this channel
        not_in_channel_id: If provided, only search users not in this channel. Must specifiy ``team_id`` when using this option
        in_group_id: If provided, only search users in this group. Must have ``manage_system`` permission.
        group_constrained: When used with ``not_in_channel_id`` or ``not_in_team_id``, returns only the users that are allowed to join the channel or team based on its group constrains.
        allow_inactive: When ``true``, include deactivated users in the results
        without_team: Set this to ``true`` if you would like to search for users that are not on a team. This option takes precendence over ``team_id``, ``in_channel_id``, and ``not_in_channel_id``.
        limit: The maximum number of users to return in the results

        *Available as of server version 5.6. Defaults to ``100`` if not provided or on an earlier server version.*


        `Read in Mattermost API docs (users - SearchUsers) <https://api.mattermost.com/#tag/users/operation/SearchUsers>`_
        """
        return self.client.post("""/api/v4/users/search""", options=options)

    def autocomplete_users(self, params=None):
        """Autocomplete users

        team_id: Team ID
        channel_id: Channel ID
        name: Username, nickname first name or last name
        limit: The maximum number of users to return in each subresult

        *Available as of server version 5.6. Defaults to ``100`` if not provided or on an earlier server version.*


        `Read in Mattermost API docs (users - AutocompleteUsers) <https://api.mattermost.com/#tag/users/operation/AutocompleteUsers>`_
        """
        return self.client.get("""/api/v4/users/autocomplete""", params=params)

    def get_known_users(self):
        """Get user IDs of known users
        `Read in Mattermost API docs (users - GetKnownUsers) <https://api.mattermost.com/#tag/users/operation/GetKnownUsers>`_
        """
        return self.client.get("""/api/v4/users/known""")

    def get_total_users_stats(self):
        """Get total count of users in the system
        `Read in Mattermost API docs (users - GetTotalUsersStats) <https://api.mattermost.com/#tag/users/operation/GetTotalUsersStats>`_
        """
        return self.client.get("""/api/v4/users/stats""")

    def get_total_users_stats_filtered(self, params=None):
        """Get total count of users in the system matching the specified filters

        in_team: The ID of the team to get user stats for.
        in_channel: The ID of the channel to get user stats for.
        include_deleted: If deleted accounts should be included in the count.
        include_bots: If bot accounts should be included in the count.
        roles: Comma separated string used to filter users based on any of the specified system roles

        Example: ``?roles=system_admin,system_user`` will include users that are either system admins or system users

        channel_roles: Comma separated string used to filter users based on any of the specified channel roles, can only be used in conjunction with ``in_channel``

        Example: ``?in_channel=4eb6axxw7fg3je5iyasnfudc5y&channel_roles=channel_user`` will include users that are only channel users and not admins or guests

        team_roles: Comma separated string used to filter users based on any of the specified team roles, can only be used in conjunction with ``in_team``

        Example: ``?in_team=4eb6axxw7fg3je5iyasnfudc5y&team_roles=team_user`` will include users that are only team users and not admins or guests


        `Read in Mattermost API docs (users - GetTotalUsersStatsFiltered) <https://api.mattermost.com/#tag/users/operation/GetTotalUsersStatsFiltered>`_
        """
        return self.client.get("""/api/v4/users/stats/filtered""", params=params)

    def get_user(self, user_id):
        """Get a user

        user_id: User GUID. This can also be "me" which will point to the current user.

        `Read in Mattermost API docs (users - GetUser) <https://api.mattermost.com/#tag/users/operation/GetUser>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}")

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

        `Read in Mattermost API docs (users - UpdateUser) <https://api.mattermost.com/#tag/users/operation/UpdateUser>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}", options=options)

    def delete_user(self, user_id):
        """Deactivate a user account.

        user_id: User GUID

        `Read in Mattermost API docs (users - DeleteUser) <https://api.mattermost.com/#tag/users/operation/DeleteUser>`_
        """
        return self.client.delete(f"/api/v4/users/{user_id}")

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

        `Read in Mattermost API docs (users - PatchUser) <https://api.mattermost.com/#tag/users/operation/PatchUser>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/patch", options=options)

    def update_user_roles(self, user_id, options):
        """Update a user's roles

        user_id: User GUID
        roles:

        `Read in Mattermost API docs (users - UpdateUserRoles) <https://api.mattermost.com/#tag/users/operation/UpdateUserRoles>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/roles", options=options)

    def update_user_active(self, user_id, options):
        """Update user active status

        user_id: User GUID
        active:

        `Read in Mattermost API docs (users - UpdateUserActive) <https://api.mattermost.com/#tag/users/operation/UpdateUserActive>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/active", options=options)

    def get_profile_image(self, user_id, params=None):
        """Get user's profile image

        user_id: User GUID
        _: Not used by the server. Clients can pass in the last picture update time of the user to potentially take advantage of caching

        `Read in Mattermost API docs (users - GetProfileImage) <https://api.mattermost.com/#tag/users/operation/GetProfileImage>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/image", params=params)

    def set_profile_image(self, user_id, files, data=None):
        """Set user's profile image

        user_id: User GUID
        image: The image to be uploaded

        `Read in Mattermost API docs (users - SetProfileImage) <https://api.mattermost.com/#tag/users/operation/SetProfileImage>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/image", files=files, data=data)

    def set_default_profile_image(self, user_id):
        """Delete user's profile image

        user_id: User GUID

        `Read in Mattermost API docs (users - SetDefaultProfileImage) <https://api.mattermost.com/#tag/users/operation/SetDefaultProfileImage>`_
        """
        return self.client.delete(f"/api/v4/users/{user_id}/image")

    def get_default_profile_image(self, user_id):
        """Return user's default (generated) profile image

        user_id: User GUID

        `Read in Mattermost API docs (users - GetDefaultProfileImage) <https://api.mattermost.com/#tag/users/operation/GetDefaultProfileImage>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/image/default")

    def get_user_by_username(self, username):
        """Get a user by username

        username: Username

        `Read in Mattermost API docs (users - GetUserByUsername) <https://api.mattermost.com/#tag/users/operation/GetUserByUsername>`_
        """
        return self.client.get(f"/api/v4/users/username/{username}")

    def reset_password(self, options):
        """Reset password

        code: The recovery code
        new_password: The new password for the user

        `Read in Mattermost API docs (users - ResetPassword) <https://api.mattermost.com/#tag/users/operation/ResetPassword>`_
        """
        return self.client.post("""/api/v4/users/password/reset""", options=options)

    def update_user_mfa(self, user_id, options):
        """Update a user's MFA

        user_id: User GUID
        activate: Use ``true`` to activate, ``false`` to deactivate
        code: The code produced by your MFA client. Required if ``activate`` is true

        `Read in Mattermost API docs (users - UpdateUserMfa) <https://api.mattermost.com/#tag/users/operation/UpdateUserMfa>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/mfa", options=options)

    def generate_mfa_secret(self, user_id):
        """Generate MFA secret

        user_id: User GUID

        `Read in Mattermost API docs (users - GenerateMfaSecret) <https://api.mattermost.com/#tag/users/operation/GenerateMfaSecret>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/mfa/generate")

    def demote_user_to_guest(self, user_id):
        """Demote a user to a guest

        user_id: User GUID

        `Read in Mattermost API docs (users - DemoteUserToGuest) <https://api.mattermost.com/#tag/users/operation/DemoteUserToGuest>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/demote")

    def promote_guest_to_user(self, user_id):
        """Promote a guest to user

        user_id: User GUID

        `Read in Mattermost API docs (users - PromoteGuestToUser) <https://api.mattermost.com/#tag/users/operation/PromoteGuestToUser>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/promote")

    def convert_user_to_bot(self, user_id):
        """Convert a user into a bot

        user_id: User GUID

        `Read in Mattermost API docs (users - ConvertUserToBot) <https://api.mattermost.com/#tag/users/operation/ConvertUserToBot>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/convert_to_bot")

    def check_user_mfa(self, options):
        """Check MFA

        login_id: The email or username used to login

        `Read in Mattermost API docs (users - CheckUserMfa) <https://api.mattermost.com/#tag/users/operation/CheckUserMfa>`_
        """
        return self.client.post("""/api/v4/users/mfa""", options=options)

    def update_user_password(self, user_id, options):
        """Update a user's password

        user_id: User GUID
        current_password: The current password for the user
        new_password: The new password for the user

        `Read in Mattermost API docs (users - UpdateUserPassword) <https://api.mattermost.com/#tag/users/operation/UpdateUserPassword>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/password", options=options)

    def send_password_reset_email(self, options):
        """Send password reset email

        email: The email of the user

        `Read in Mattermost API docs (users - SendPasswordResetEmail) <https://api.mattermost.com/#tag/users/operation/SendPasswordResetEmail>`_
        """
        return self.client.post("""/api/v4/users/password/reset/send""", options=options)

    def get_user_by_email(self, email):
        """Get a user by email

        email: User Email

        `Read in Mattermost API docs (users - GetUserByEmail) <https://api.mattermost.com/#tag/users/operation/GetUserByEmail>`_
        """
        return self.client.get(f"/api/v4/users/email/{email}")

    def get_sessions(self, user_id):
        """Get user's sessions

        user_id: User GUID

        `Read in Mattermost API docs (users - GetSessions) <https://api.mattermost.com/#tag/users/operation/GetSessions>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/sessions")

    def revoke_session(self, user_id, options):
        """Revoke a user session

        user_id: User GUID
        session_id: The session GUID to revoke.

        `Read in Mattermost API docs (users - RevokeSession) <https://api.mattermost.com/#tag/users/operation/RevokeSession>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/sessions/revoke", options=options)

    def revoke_all_sessions(self, user_id):
        """Revoke all active sessions for a user

        user_id: User GUID

        `Read in Mattermost API docs (users - RevokeAllSessions) <https://api.mattermost.com/#tag/users/operation/RevokeAllSessions>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/sessions/revoke/all")

    def attach_device_id(self, options):
        """Attach mobile device

        device_id: Mobile device id. For Android prefix the id with ``android:`` and Apple with ``apple:``

        `Read in Mattermost API docs (users - AttachDeviceId) <https://api.mattermost.com/#tag/users/operation/AttachDeviceId>`_
        """
        return self.client.put("""/api/v4/users/sessions/device""", options=options)

    def get_user_audits(self, user_id):
        """Get user's audits

        user_id: User GUID

        `Read in Mattermost API docs (users - GetUserAudits) <https://api.mattermost.com/#tag/users/operation/GetUserAudits>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/audits")

    def verify_user_email_without_token(self, user_id):
        """Verify user email by ID

        user_id: User GUID

        `Read in Mattermost API docs (users - VerifyUserEmailWithoutToken) <https://api.mattermost.com/#tag/users/operation/VerifyUserEmailWithoutToken>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/email/verify/member")

    def verify_user_email(self, options):
        """Verify user email

        token: The token given to validate the email

        `Read in Mattermost API docs (users - VerifyUserEmail) <https://api.mattermost.com/#tag/users/operation/VerifyUserEmail>`_
        """
        return self.client.post("""/api/v4/users/email/verify""", options=options)

    def send_verification_email(self, options):
        """Send verification email

        email: Email of a user

        `Read in Mattermost API docs (users - SendVerificationEmail) <https://api.mattermost.com/#tag/users/operation/SendVerificationEmail>`_
        """
        return self.client.post("""/api/v4/users/email/verify/send""", options=options)

    def switch_account_type(self, options):
        """Switch login method

        current_service: The service the user currently uses to login
        new_service: The service the user will use to login
        email: The email of the user
        password: The password used with the current service
        mfa_code: The MFA code of the current service
        ldap_id: The LDAP/AD id of the user

        `Read in Mattermost API docs (users - SwitchAccountType) <https://api.mattermost.com/#tag/users/operation/SwitchAccountType>`_
        """
        return self.client.post("""/api/v4/users/login/switch""", options=options)

    def create_user_access_token(self, user_id, options):
        """Create a user access token

        user_id: User GUID
        description: A description of the token usage

        `Read in Mattermost API docs (users - CreateUserAccessToken) <https://api.mattermost.com/#tag/users/operation/CreateUserAccessToken>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/tokens", options=options)

    def get_user_access_tokens_for_user(self, user_id, params=None):
        """Get user access tokens

        user_id: User GUID
        page: The page to select.
        per_page: The number of tokens per page.

        `Read in Mattermost API docs (users - GetUserAccessTokensForUser) <https://api.mattermost.com/#tag/users/operation/GetUserAccessTokensForUser>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/tokens", params=params)

    def get_user_access_tokens(self, params=None):
        """Get user access tokens

        page: The page to select.
        per_page: The number of tokens per page.

        `Read in Mattermost API docs (users - GetUserAccessTokens) <https://api.mattermost.com/#tag/users/operation/GetUserAccessTokens>`_
        """
        return self.client.get("""/api/v4/users/tokens""", params=params)

    def revoke_user_access_token(self, options):
        """Revoke a user access token

        token_id: The user access token GUID to revoke

        `Read in Mattermost API docs (users - RevokeUserAccessToken) <https://api.mattermost.com/#tag/users/operation/RevokeUserAccessToken>`_
        """
        return self.client.post("""/api/v4/users/tokens/revoke""", options=options)

    def get_user_access_token(self, token_id):
        """Get a user access token

        token_id: User access token GUID

        `Read in Mattermost API docs (users - GetUserAccessToken) <https://api.mattermost.com/#tag/users/operation/GetUserAccessToken>`_
        """
        return self.client.get(f"/api/v4/users/tokens/{token_id}")

    def disable_user_access_token(self, options):
        """Disable personal access token

        token_id: The personal access token GUID to disable

        `Read in Mattermost API docs (users - DisableUserAccessToken) <https://api.mattermost.com/#tag/users/operation/DisableUserAccessToken>`_
        """
        return self.client.post("""/api/v4/users/tokens/disable""", options=options)

    def enable_user_access_token(self, options):
        """Enable personal access token

        token_id: The personal access token GUID to enable

        `Read in Mattermost API docs (users - EnableUserAccessToken) <https://api.mattermost.com/#tag/users/operation/EnableUserAccessToken>`_
        """
        return self.client.post("""/api/v4/users/tokens/enable""", options=options)

    def search_user_access_tokens(self, options):
        """Search tokens

        term: The search term to match against the token id, user id or username.

        `Read in Mattermost API docs (users - SearchUserAccessTokens) <https://api.mattermost.com/#tag/users/operation/SearchUserAccessTokens>`_
        """
        return self.client.post("""/api/v4/users/tokens/search""", options=options)

    def update_user_auth(self, user_id, options):
        """Update a user's authentication method

        user_id: User GUID

        `Read in Mattermost API docs (users - UpdateUserAuth) <https://api.mattermost.com/#tag/users/operation/UpdateUserAuth>`_
        """
        return self.client.put(f"/api/v4/users/{user_id}/auth", options=options)

    def register_terms_of_service_action(self, user_id, options):
        """Records user action when they accept or decline custom terms of service

        user_id: User GUID
        serviceTermsId: terms of service ID on which the user is acting on
        accepted: true or false, indicates whether the user accepted or rejected the terms of service.

        `Read in Mattermost API docs (users - RegisterTermsOfServiceAction) <https://api.mattermost.com/#tag/users/operation/RegisterTermsOfServiceAction>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/terms_of_service", options=options)

    def get_user_terms_of_service(self, user_id):
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        user_id: User GUID

        `Read in Mattermost API docs (users - GetUserTermsOfService) <https://api.mattermost.com/#tag/users/operation/GetUserTermsOfService>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/terms_of_service")

    def revoke_sessions_from_all_users(self):
        """Revoke all sessions from all users.
        `Read in Mattermost API docs (users - RevokeSessionsFromAllUsers) <https://api.mattermost.com/#tag/users/operation/RevokeSessionsFromAllUsers>`_
        """
        return self.client.post("""/api/v4/users/sessions/revoke/all""")

    def publish_user_typing(self, user_id, options=None):
        """Publish a user typing websocket event.

        user_id: User GUID
        channel_id: The id of the channel to which to direct the typing event.
        parent_id: The optional id of the root post of the thread to which the user is replying. If unset, the typing event is directed at the entire channel.

        `Read in Mattermost API docs (users - PublishUserTyping) <https://api.mattermost.com/#tag/users/operation/PublishUserTyping>`_
        """
        return self.client.post(f"/api/v4/users/{user_id}/typing", options=options)

    def get_uploads_for_user(self, user_id):
        """Get uploads for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.

        `Read in Mattermost API docs (users - GetUploadsForUser) <https://api.mattermost.com/#tag/users/operation/GetUploadsForUser>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/uploads")

    def get_channel_members_with_team_data_for_user(self, user_id, params=None):
        """Get all channel members from all teams for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        page: Page specifies which part of the results to return, by PageSize.
        pageSize: PageSize specifies the size of the returned chunk of results.

        `Read in Mattermost API docs (users - GetChannelMembersWithTeamDataForUser) <https://api.mattermost.com/#tag/users/operation/GetChannelMembersWithTeamDataForUser>`_
        """
        return self.client.get(f"/api/v4/users/{user_id}/channel_members", params=params)

    def migrate_auth_to_ldap(self, options=None):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (users - MigrateAuthToLdap) <https://api.mattermost.com/#tag/users/operation/MigrateAuthToLdap>`_
        """
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=options)

    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (users - MigrateAuthToSaml) <https://api.mattermost.com/#tag/users/operation/MigrateAuthToSaml>`_
        """
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=options)

    def get_users_with_invalid_emails(self, params=None):
        """Get users with invalid emails

        page: The page to select.
        per_page: The number of users per page. There is a maximum limit of 200 users per page.

        `Read in Mattermost API docs (users - GetUsersWithInvalidEmails) <https://api.mattermost.com/#tag/users/operation/GetUsersWithInvalidEmails>`_
        """
        return self.client.get("""/api/v4/users/invalid_emails""", params=params)

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

        `Read in Mattermost API docs (users - ConvertBotToUser) <https://api.mattermost.com/#tag/users/operation/ConvertBotToUser>`_
        """
        return self.client.post(f"/api/v4/bots/{bot_user_id}/convert_to_user", options=options)
