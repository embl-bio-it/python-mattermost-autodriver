from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Users"]


class Users(Base):

    def login(
        self,
        id: str | None = None,
        login_id: str | None = None,
        token: str | None = None,
        device_id: str | None = None,
        ldap_only: bool | None = None,
        password: str | None = None,
    ):
        """Login to Mattermost server

        id:
        login_id:
        token:
        device_id:
        ldap_only:
        password: The password used for email authentication.

        `Read in Mattermost API docs (users - Login) <https://developers.mattermost.com/api-documentation/#/operations/Login>`_

        """
        __options = {
            "id": id,
            "login_id": login_id,
            "token": token,
            "device_id": device_id,
            "ldap_only": ldap_only,
            "password": password,
        }
        return self.client.post("""/api/v4/users/login""", options=__options)

    def login_by_cws_token(self, login_id: str | None = None, cws_token: str | None = None):
        """Auto-Login to Mattermost server using CWS token

        login_id:
        cws_token:

        `Read in Mattermost API docs (users - LoginByCwsToken) <https://developers.mattermost.com/api-documentation/#/operations/LoginByCwsToken>`_

        """
        __options = {"login_id": login_id, "cws_token": cws_token}
        return self.client.post("""/api/v4/users/login/cws""", options=__options)

    def login_sso_code_exchange(self, login_code: str, code_verifier: str, state: str):
        """Exchange SSO login code for session tokens

        login_code: Short-lived one-time code from SSO callback
        code_verifier: SAML verifier to prove code possession
        state: State parameter to prevent CSRF attacks

        `Read in Mattermost API docs (users - LoginSSOCodeExchange) <https://developers.mattermost.com/api-documentation/#/operations/LoginSSOCodeExchange>`_

        """
        __options = {"login_code": login_code, "code_verifier": code_verifier, "state": state}
        return self.client.post("""/api/v4/users/login/sso/code-exchange""", options=__options)

    def logout(self):
        """Logout from the Mattermost server
        `Read in Mattermost API docs (users - Logout) <https://developers.mattermost.com/api-documentation/#/operations/Logout>`_

        """
        return self.client.post("""/api/v4/users/logout""")

    def create_user(
        self,
        email: str,
        username: str,
        first_name: str | None = None,
        last_name: str | None = None,
        nickname: str | None = None,
        position: str | None = None,
        timezone: Any | None = None,
        auth_data: str | None = None,
        auth_service: str | None = None,
        password: str | None = None,
        locale: str | None = None,
        props: dict[str, Any] | None = None,
        notify_props: Any | None = None,
    ):
        """Create a user

        email:
        username:
        first_name:
        last_name:
        nickname:
        position:
        timezone:
        auth_data: Service-specific authentication data, such as email address.
        auth_service: The authentication service, one of "email", "gitlab", "ldap", "saml", "office365", "google", and "".
        password: The password used for email authentication.
        locale:
        props:
        notify_props:

        `Read in Mattermost API docs (users - CreateUser) <https://developers.mattermost.com/api-documentation/#/operations/CreateUser>`_

        """
        __options = {
            "email": email,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "position": position,
            "timezone": timezone,
            "auth_data": auth_data,
            "auth_service": auth_service,
            "password": password,
            "locale": locale,
            "props": props,
            "notify_props": notify_props,
        }
        return self.client.post("""/api/v4/users""", options=__options)

    def get_users(
        self,
        page: int | None = 0,
        per_page: int | None = 60,
        in_team: str | None = None,
        not_in_team: str | None = None,
        in_channel: str | None = None,
        not_in_channel: str | None = None,
        in_group: str | None = None,
        group_constrained: bool | None = None,
        without_team: bool | None = None,
        active: bool | None = None,
        inactive: bool | None = None,
        role: str | None = None,
        sort: str | None = None,
        roles: str | None = None,
        channel_roles: str | None = None,
        team_roles: str | None = None,
    ):
        """Get users

        page: The page to select.
        per_page: The number of users per page.
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
        Note that when "last_activity_at" is specified, an additional "last_activity_at" field will be returned in the response packet.
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


        `Read in Mattermost API docs (users - GetUsers) <https://developers.mattermost.com/api-documentation/#/operations/GetUsers>`_

        """
        __params = {
            "page": page,
            "per_page": per_page,
            "in_team": in_team,
            "not_in_team": not_in_team,
            "in_channel": in_channel,
            "not_in_channel": not_in_channel,
            "in_group": in_group,
            "group_constrained": group_constrained,
            "without_team": without_team,
            "active": active,
            "inactive": inactive,
            "role": role,
            "sort": sort,
            "roles": roles,
            "channel_roles": channel_roles,
            "team_roles": team_roles,
        }
        return self.client.get("""/api/v4/users""", params=__params)

    def permanent_delete_all_users(self):
        """Permanent delete all users
        `Read in Mattermost API docs (users - PermanentDeleteAllUsers) <https://developers.mattermost.com/api-documentation/#/operations/PermanentDeleteAllUsers>`_

        """
        return self.client.delete("""/api/v4/users""")

    def get_users_by_ids(self, options: list[str]):
        """Get users by ids
        `Read in Mattermost API docs (users - GetUsersByIds) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersByIds>`_

        """
        return self.client.post("""/api/v4/users/ids""", options=options)

    def get_users_by_group_channel_ids(self, options: list[str]):
        """Get users by group channels ids
        `Read in Mattermost API docs (users - GetUsersByGroupChannelIds) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersByGroupChannelIds>`_

        """
        return self.client.post("""/api/v4/users/group_channels""", options=options)

    def get_users_by_usernames(self, options: list[str]):
        """Get users by usernames
        `Read in Mattermost API docs (users - GetUsersByUsernames) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersByUsernames>`_

        """
        return self.client.post("""/api/v4/users/usernames""", options=options)

    def search_users(
        self,
        term: str,
        team_id: str | None = None,
        not_in_team_id: str | None = None,
        in_channel_id: str | None = None,
        not_in_channel_id: str | None = None,
        in_group_id: str | None = None,
        group_constrained: bool | None = None,
        allow_inactive: bool | None = None,
        without_team: bool | None = None,
        limit: int | None = 100,
    ):
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


        `Read in Mattermost API docs (users - SearchUsers) <https://developers.mattermost.com/api-documentation/#/operations/SearchUsers>`_

        """
        __options = {
            "term": term,
            "team_id": team_id,
            "not_in_team_id": not_in_team_id,
            "in_channel_id": in_channel_id,
            "not_in_channel_id": not_in_channel_id,
            "in_group_id": in_group_id,
            "group_constrained": group_constrained,
            "allow_inactive": allow_inactive,
            "without_team": without_team,
            "limit": limit,
        }
        return self.client.post("""/api/v4/users/search""", options=__options)

    def autocomplete_users(
        self, name: str, team_id: str | None = None, channel_id: str | None = None, limit: int | None = 100
    ):
        """Autocomplete users

        team_id: Team ID
        channel_id: Channel ID
        name: Username, nickname first name or last name
        limit: The maximum number of users to return in each subresult

        *Available as of server version 5.6. Defaults to ``100`` if not provided or on an earlier server version.*


        `Read in Mattermost API docs (users - AutocompleteUsers) <https://developers.mattermost.com/api-documentation/#/operations/AutocompleteUsers>`_

        """
        __params = {"team_id": team_id, "channel_id": channel_id, "name": name, "limit": limit}
        return self.client.get("""/api/v4/users/autocomplete""", params=__params)

    def get_known_users(self):
        """Get user IDs of known users
        `Read in Mattermost API docs (users - GetKnownUsers) <https://developers.mattermost.com/api-documentation/#/operations/GetKnownUsers>`_

        """
        return self.client.get("""/api/v4/users/known""")

    def get_total_users_stats(self):
        """Get total count of users in the system
        `Read in Mattermost API docs (users - GetTotalUsersStats) <https://developers.mattermost.com/api-documentation/#/operations/GetTotalUsersStats>`_

        """
        return self.client.get("""/api/v4/users/stats""")

    def get_total_users_stats_filtered(
        self,
        in_team: str | None = None,
        in_channel: str | None = None,
        include_deleted: bool | None = None,
        include_bots: bool | None = None,
        roles: str | None = None,
        channel_roles: str | None = None,
        team_roles: str | None = None,
    ):
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


        `Read in Mattermost API docs (users - GetTotalUsersStatsFiltered) <https://developers.mattermost.com/api-documentation/#/operations/GetTotalUsersStatsFiltered>`_

        """
        __params = {
            "in_team": in_team,
            "in_channel": in_channel,
            "include_deleted": include_deleted,
            "include_bots": include_bots,
            "roles": roles,
            "channel_roles": channel_roles,
            "team_roles": team_roles,
        }
        return self.client.get("""/api/v4/users/stats/filtered""", params=__params)

    def get_user(self, user_id: str):
        """Get a user

        user_id: User GUID. This can also be "me" which will point to the current user.

        `Read in Mattermost API docs (users - GetUser) <https://developers.mattermost.com/api-documentation/#/operations/GetUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}")

    def update_user(
        self,
        user_id: str,
        id: str,
        email: str,
        username: str,
        first_name: str | None = None,
        last_name: str | None = None,
        nickname: str | None = None,
        locale: str | None = None,
        position: str | None = None,
        timezone: Any | None = None,
        props: dict[str, Any] | None = None,
        notify_props: Any | None = None,
    ):
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

        `Read in Mattermost API docs (users - UpdateUser) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUser>`_

        """
        __options = {
            "id": id,
            "email": email,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "locale": locale,
            "position": position,
            "timezone": timezone,
            "props": props,
            "notify_props": notify_props,
        }
        return self.client.put(f"/api/v4/users/{user_id}", options=__options)

    def delete_user(self, user_id: str):
        """Deactivate a user account.

        user_id: User GUID

        `Read in Mattermost API docs (users - DeleteUser) <https://developers.mattermost.com/api-documentation/#/operations/DeleteUser>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}")

    def patch_user(
        self,
        user_id: str,
        email: str | None = None,
        username: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        nickname: str | None = None,
        locale: str | None = None,
        position: str | None = None,
        timezone: Any | None = None,
        props: dict[str, Any] | None = None,
        notify_props: Any | None = None,
    ):
        """Patch a user

        user_id: User GUID
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

        `Read in Mattermost API docs (users - PatchUser) <https://developers.mattermost.com/api-documentation/#/operations/PatchUser>`_

        """
        __options = {
            "email": email,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "locale": locale,
            "position": position,
            "timezone": timezone,
            "props": props,
            "notify_props": notify_props,
        }
        return self.client.put(f"/api/v4/users/{user_id}/patch", options=__options)

    def update_user_roles(self, user_id: str, roles: str):
        """Update a user's roles

        user_id: User GUID
        roles:

        `Read in Mattermost API docs (users - UpdateUserRoles) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserRoles>`_

        """
        __options = {"roles": roles}
        return self.client.put(f"/api/v4/users/{user_id}/roles", options=__options)

    def update_user_active(self, user_id: str, active: bool):
        """Update user active status

        user_id: User GUID
        active:

        `Read in Mattermost API docs (users - UpdateUserActive) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserActive>`_

        """
        __options = {"active": active}
        return self.client.put(f"/api/v4/users/{user_id}/active", options=__options)

    def get_profile_image(self, user_id: str, _: float | None = None):
        """Get user's profile image

        user_id: User GUID
        _: Not used by the server. Clients can pass in the last picture update time of the user to potentially take advantage of caching

        `Read in Mattermost API docs (users - GetProfileImage) <https://developers.mattermost.com/api-documentation/#/operations/GetProfileImage>`_

        """
        __params = {"_": _}
        return self.client.get(f"/api/v4/users/{user_id}/image", params=__params)

    def set_profile_image(self, user_id: str, image: BinaryIO):
        """Set user's profile image

        user_id: User GUID
        image: The image to be uploaded

        `Read in Mattermost API docs (users - SetProfileImage) <https://developers.mattermost.com/api-documentation/#/operations/SetProfileImage>`_

        """
        __files = {"image": image}
        return self.client.post(f"/api/v4/users/{user_id}/image", files=__files)

    def set_default_profile_image(self, user_id: str):
        """Delete user's profile image

        user_id: User GUID

        `Read in Mattermost API docs (users - SetDefaultProfileImage) <https://developers.mattermost.com/api-documentation/#/operations/SetDefaultProfileImage>`_

        """
        return self.client.delete(f"/api/v4/users/{user_id}/image")

    def get_default_profile_image(self, user_id: str):
        """Return user's default (generated) profile image

        user_id: User GUID

        `Read in Mattermost API docs (users - GetDefaultProfileImage) <https://developers.mattermost.com/api-documentation/#/operations/GetDefaultProfileImage>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/image/default")

    def get_user_by_username(self, username: str):
        """Get a user by username

        username: Username

        `Read in Mattermost API docs (users - GetUserByUsername) <https://developers.mattermost.com/api-documentation/#/operations/GetUserByUsername>`_

        """
        return self.client.get(f"/api/v4/users/username/{username}")

    def reset_password(self, code: str, new_password: str):
        """Reset password

        code: The recovery code
        new_password: The new password for the user

        `Read in Mattermost API docs (users - ResetPassword) <https://developers.mattermost.com/api-documentation/#/operations/ResetPassword>`_

        """
        __options = {"code": code, "new_password": new_password}
        return self.client.post("""/api/v4/users/password/reset""", options=__options)

    def update_user_mfa(self, user_id: str, activate: bool, code: str | None = None):
        """Update a user's MFA

        user_id: User GUID
        activate: Use ``true`` to activate, ``false`` to deactivate
        code: The code produced by your MFA client. Required if ``activate`` is true

        `Read in Mattermost API docs (users - UpdateUserMfa) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserMfa>`_

        """
        __options = {"activate": activate, "code": code}
        return self.client.put(f"/api/v4/users/{user_id}/mfa", options=__options)

    def generate_mfa_secret(self, user_id: str):
        """Generate MFA secret

        user_id: User GUID

        `Read in Mattermost API docs (users - GenerateMfaSecret) <https://developers.mattermost.com/api-documentation/#/operations/GenerateMfaSecret>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/mfa/generate")

    def demote_user_to_guest(self, user_id: str):
        """Demote a user to a guest

        user_id: User GUID

        `Read in Mattermost API docs (users - DemoteUserToGuest) <https://developers.mattermost.com/api-documentation/#/operations/DemoteUserToGuest>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/demote")

    def promote_guest_to_user(self, user_id: str):
        """Promote a guest to user

        user_id: User GUID

        `Read in Mattermost API docs (users - PromoteGuestToUser) <https://developers.mattermost.com/api-documentation/#/operations/PromoteGuestToUser>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/promote")

    def convert_user_to_bot(self, user_id: str):
        """Convert a user into a bot

        user_id: User GUID

        `Read in Mattermost API docs (users - ConvertUserToBot) <https://developers.mattermost.com/api-documentation/#/operations/ConvertUserToBot>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/convert_to_bot")

    def check_user_mfa(self, login_id: str):
        """Check MFA

        login_id: The email or username used to login

        `Read in Mattermost API docs (users - CheckUserMfa) <https://developers.mattermost.com/api-documentation/#/operations/CheckUserMfa>`_

        """
        __options = {"login_id": login_id}
        return self.client.post("""/api/v4/users/mfa""", options=__options)

    def update_user_password(self, user_id: str, new_password: str, current_password: str | None = None):
        """Update a user's password

        user_id: User GUID
        current_password: The current password for the user
        new_password: The new password for the user

        `Read in Mattermost API docs (users - UpdateUserPassword) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserPassword>`_

        """
        __options = {"current_password": current_password, "new_password": new_password}
        return self.client.put(f"/api/v4/users/{user_id}/password", options=__options)

    def send_password_reset_email(self, email: str):
        """Send password reset email

        email: The email of the user

        `Read in Mattermost API docs (users - SendPasswordResetEmail) <https://developers.mattermost.com/api-documentation/#/operations/SendPasswordResetEmail>`_

        """
        __options = {"email": email}
        return self.client.post("""/api/v4/users/password/reset/send""", options=__options)

    def get_user_by_email(self, email: str):
        """Get a user by email

        email: User Email

        `Read in Mattermost API docs (users - GetUserByEmail) <https://developers.mattermost.com/api-documentation/#/operations/GetUserByEmail>`_

        """
        return self.client.get(f"/api/v4/users/email/{email}")

    def get_sessions(self, user_id: str):
        """Get user's sessions

        user_id: User GUID

        `Read in Mattermost API docs (users - GetSessions) <https://developers.mattermost.com/api-documentation/#/operations/GetSessions>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/sessions")

    def revoke_session(self, user_id: str, session_id: str):
        """Revoke a user session

        user_id: User GUID
        session_id: The session GUID to revoke.

        `Read in Mattermost API docs (users - RevokeSession) <https://developers.mattermost.com/api-documentation/#/operations/RevokeSession>`_

        """
        __options = {"session_id": session_id}
        return self.client.post(f"/api/v4/users/{user_id}/sessions/revoke", options=__options)

    def revoke_all_sessions(self, user_id: str):
        """Revoke all active sessions for a user

        user_id: User GUID

        `Read in Mattermost API docs (users - RevokeAllSessions) <https://developers.mattermost.com/api-documentation/#/operations/RevokeAllSessions>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/sessions/revoke/all")

    def attach_device_extra_props(
        self,
        device_id: str | None = None,
        deviceNotificationDisabled: str | None = None,
        mobileVersion: str | None = None,
    ):
        """Attach mobile device and extra props to the session object

        device_id: Mobile device id. For Android prefix the id with ``android:`` and Apple with ``apple:``
        deviceNotificationDisabled: Whether the mobile device has notifications disabled. Accepted values are "true" or "false".
        mobileVersion: Mobile app version. The version must be parseable as a semver.

        `Read in Mattermost API docs (users - AttachDeviceExtraProps) <https://developers.mattermost.com/api-documentation/#/operations/AttachDeviceExtraProps>`_

        """
        __options = {
            "device_id": device_id,
            "deviceNotificationDisabled": deviceNotificationDisabled,
            "mobileVersion": mobileVersion,
        }
        return self.client.put("""/api/v4/users/sessions/device""", options=__options)

    def get_user_audits(self, user_id: str):
        """Get user's audits

        user_id: User GUID

        `Read in Mattermost API docs (users - GetUserAudits) <https://developers.mattermost.com/api-documentation/#/operations/GetUserAudits>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/audits")

    def verify_user_email_without_token(self, user_id: str):
        """Verify user email by ID

        user_id: User GUID

        `Read in Mattermost API docs (users - VerifyUserEmailWithoutToken) <https://developers.mattermost.com/api-documentation/#/operations/VerifyUserEmailWithoutToken>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/email/verify/member")

    def verify_user_email(self, token: str):
        """Verify user email

        token: The token given to validate the email

        `Read in Mattermost API docs (users - VerifyUserEmail) <https://developers.mattermost.com/api-documentation/#/operations/VerifyUserEmail>`_

        """
        __options = {"token": token}
        return self.client.post("""/api/v4/users/email/verify""", options=__options)

    def send_verification_email(self, email: str):
        """Send verification email

        email: Email of a user

        `Read in Mattermost API docs (users - SendVerificationEmail) <https://developers.mattermost.com/api-documentation/#/operations/SendVerificationEmail>`_

        """
        __options = {"email": email}
        return self.client.post("""/api/v4/users/email/verify/send""", options=__options)

    def switch_account_type(
        self,
        current_service: str,
        new_service: str,
        email: str | None = None,
        password: str | None = None,
        mfa_code: str | None = None,
        ldap_id: str | None = None,
    ):
        """Switch login method

        current_service: The service the user currently uses to login
        new_service: The service the user will use to login
        email: The email of the user
        password: The password used with the current service
        mfa_code: The MFA code of the current service
        ldap_id: The LDAP/AD id of the user

        `Read in Mattermost API docs (users - SwitchAccountType) <https://developers.mattermost.com/api-documentation/#/operations/SwitchAccountType>`_

        """
        __options = {
            "current_service": current_service,
            "new_service": new_service,
            "email": email,
            "password": password,
            "mfa_code": mfa_code,
            "ldap_id": ldap_id,
        }
        return self.client.post("""/api/v4/users/login/switch""", options=__options)

    def create_user_access_token(self, user_id: str, description: str):
        """Create a user access token

        user_id: User GUID
        description: A description of the token usage

        `Read in Mattermost API docs (users - CreateUserAccessToken) <https://developers.mattermost.com/api-documentation/#/operations/CreateUserAccessToken>`_

        """
        __options = {"description": description}
        return self.client.post(f"/api/v4/users/{user_id}/tokens", options=__options)

    def get_user_access_tokens_for_user(self, user_id: str, page: int | None = 0, per_page: int | None = 60):
        """Get user access tokens

        user_id: User GUID
        page: The page to select.
        per_page: The number of tokens per page.

        `Read in Mattermost API docs (users - GetUserAccessTokensForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetUserAccessTokensForUser>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/users/{user_id}/tokens", params=__params)

    def get_user_access_tokens(self, page: int | None = 0, per_page: int | None = 60):
        """Get user access tokens

        page: The page to select.
        per_page: The number of tokens per page.

        `Read in Mattermost API docs (users - GetUserAccessTokens) <https://developers.mattermost.com/api-documentation/#/operations/GetUserAccessTokens>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/users/tokens""", params=__params)

    def revoke_user_access_token(self, token_id: str):
        """Revoke a user access token

        token_id: The user access token GUID to revoke

        `Read in Mattermost API docs (users - RevokeUserAccessToken) <https://developers.mattermost.com/api-documentation/#/operations/RevokeUserAccessToken>`_

        """
        __options = {"token_id": token_id}
        return self.client.post("""/api/v4/users/tokens/revoke""", options=__options)

    def get_user_access_token(self, token_id: str):
        """Get a user access token

        token_id: User access token GUID

        `Read in Mattermost API docs (users - GetUserAccessToken) <https://developers.mattermost.com/api-documentation/#/operations/GetUserAccessToken>`_

        """
        return self.client.get(f"/api/v4/users/tokens/{token_id}")

    def disable_user_access_token(self, token_id: str):
        """Disable personal access token

        token_id: The personal access token GUID to disable

        `Read in Mattermost API docs (users - DisableUserAccessToken) <https://developers.mattermost.com/api-documentation/#/operations/DisableUserAccessToken>`_

        """
        __options = {"token_id": token_id}
        return self.client.post("""/api/v4/users/tokens/disable""", options=__options)

    def enable_user_access_token(self, token_id: str):
        """Enable personal access token

        token_id: The personal access token GUID to enable

        `Read in Mattermost API docs (users - EnableUserAccessToken) <https://developers.mattermost.com/api-documentation/#/operations/EnableUserAccessToken>`_

        """
        __options = {"token_id": token_id}
        return self.client.post("""/api/v4/users/tokens/enable""", options=__options)

    def search_user_access_tokens(self, term: str):
        """Search tokens

        term: The search term to match against the token id, user id or username.

        `Read in Mattermost API docs (users - SearchUserAccessTokens) <https://developers.mattermost.com/api-documentation/#/operations/SearchUserAccessTokens>`_

        """
        __options = {"term": term}
        return self.client.post("""/api/v4/users/tokens/search""", options=__options)

    def update_user_auth(self, user_id: str, options: Any):
        """Update a user's authentication method

        user_id: User GUID

        `Read in Mattermost API docs (users - UpdateUserAuth) <https://developers.mattermost.com/api-documentation/#/operations/UpdateUserAuth>`_

        """
        return self.client.put(f"/api/v4/users/{user_id}/auth", options=options)

    def register_terms_of_service_action(self, user_id: str, serviceTermsId: str, accepted: str):
        """Records user action when they accept or decline custom terms of service

        user_id: User GUID
        serviceTermsId: terms of service ID on which the user is acting on
        accepted: true or false, indicates whether the user accepted or rejected the terms of service.

        `Read in Mattermost API docs (users - RegisterTermsOfServiceAction) <https://developers.mattermost.com/api-documentation/#/operations/RegisterTermsOfServiceAction>`_

        """
        __options = {"serviceTermsId": serviceTermsId, "accepted": accepted}
        return self.client.post(f"/api/v4/users/{user_id}/terms_of_service", options=__options)

    def get_user_terms_of_service(self, user_id: str):
        """Fetches user's latest terms of service action if the latest action was for acceptance.

        user_id: User GUID

        `Read in Mattermost API docs (users - GetUserTermsOfService) <https://developers.mattermost.com/api-documentation/#/operations/GetUserTermsOfService>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/terms_of_service")

    def revoke_sessions_from_all_users(self):
        """Revoke all sessions from all users.
        `Read in Mattermost API docs (users - RevokeSessionsFromAllUsers) <https://developers.mattermost.com/api-documentation/#/operations/RevokeSessionsFromAllUsers>`_

        """
        return self.client.post("""/api/v4/users/sessions/revoke/all""")

    def publish_user_typing(self, user_id: str, channel_id: str, parent_id: str | None = None):
        """Publish a user typing websocket event.

        user_id: User GUID
        channel_id: The id of the channel to which to direct the typing event.
        parent_id: The optional id of the root post of the thread to which the user is replying. If unset, the typing event is directed at the entire channel.

        `Read in Mattermost API docs (users - PublishUserTyping) <https://developers.mattermost.com/api-documentation/#/operations/PublishUserTyping>`_

        """
        __options = {"channel_id": channel_id, "parent_id": parent_id}
        return self.client.post(f"/api/v4/users/{user_id}/typing", options=__options)

    def get_uploads_for_user(self, user_id: str):
        """Get uploads for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.

        `Read in Mattermost API docs (users - GetUploadsForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetUploadsForUser>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/uploads")

    def get_channel_members_with_team_data_for_user(
        self, user_id: str, page: int | None = None, per_page: int | None = 60
    ):
        """Get all channel members from all teams for a user

        user_id: The ID of the user. This can also be "me" which will point to the current user.
        page: Page specifies which part of the results to return, by perPage.
        per_page: The size of the returned chunk of results.

        `Read in Mattermost API docs (users - GetChannelMembersWithTeamDataForUser) <https://developers.mattermost.com/api-documentation/#/operations/GetChannelMembersWithTeamDataForUser>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get(f"/api/v4/users/{user_id}/channel_members", params=__params)

    def migrate_auth_to_ldap(self, from_: str, match_field: str, force: bool):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (users - MigrateAuthToLdap) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToLdap>`_

        """
        __options = {"from": from_, "match_field": match_field, "force": force}
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=__options)

    def migrate_auth_to_saml(self, from_: str, matches: dict[str, Any], auto: bool):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (users - MigrateAuthToSaml) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToSaml>`_

        """
        __options = {"from": from_, "matches": matches, "auto": auto}
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=__options)

    def get_users_with_invalid_emails(self, page: int | None = 0, per_page: int | None = 60):
        """Get users with invalid emails

        page: The page to select.
        per_page: The number of users per page.

        `Read in Mattermost API docs (users - GetUsersWithInvalidEmails) <https://developers.mattermost.com/api-documentation/#/operations/GetUsersWithInvalidEmails>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/users/invalid_emails""", params=__params)

    def reset_password_failed_attempts(self):
        """Reset the failed password attempts for a user
        `Read in Mattermost API docs (users - resetPasswordFailedAttempts) <https://developers.mattermost.com/api-documentation/#/operations/resetPasswordFailedAttempts>`_

        """
        return self.client.post(f"/api/v4/users/{user_id}/reset_failed_attempts")

    def convert_bot_to_user(
        self,
        bot_user_id: str,
        email: str | None = None,
        username: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        nickname: str | None = None,
        locale: str | None = None,
        position: str | None = None,
        props: dict[str, Any] | None = None,
        notify_props: Any | None = None,
    ):
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

        `Read in Mattermost API docs (users - ConvertBotToUser) <https://developers.mattermost.com/api-documentation/#/operations/ConvertBotToUser>`_

        """
        __options = {
            "email": email,
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "nickname": nickname,
            "locale": locale,
            "position": position,
            "props": props,
            "notify_props": notify_props,
        }
        return self.client.post(f"/api/v4/bots/{bot_user_id}/convert_to_user", options=__options)

    def get_server_limits(self):
        """Gets the server limits for the server
        `Read in Mattermost API docs (users - GetServerLimits) <https://developers.mattermost.com/api-documentation/#/operations/GetServerLimits>`_

        """
        return self.client.get("""/api/v4/limits/server""")
