from ._base import Base
from typing import Any, BinaryIO

__all__ = ["AccessControl"]


class AccessControl(Base):

    def create_access_control_policy(self, options: Any):
        """Create an access control policy
        `Read in Mattermost API docs (access_control - CreateAccessControlPolicy) <https://developers.mattermost.com/api-documentation/#/operations/CreateAccessControlPolicy>`_

        """
        return self.client.put("""/api/v4/access_control_policies""", options=options)

    def check_access_control_policy_expression(self, expression: str | None = None):
        """Check an access control policy expression

        expression: The expression to check.

        `Read in Mattermost API docs (access_control - CheckAccessControlPolicyExpression) <https://developers.mattermost.com/api-documentation/#/operations/CheckAccessControlPolicyExpression>`_

        """
        __options = {"expression": expression}
        return self.client.post("""/api/v4/access_control_policies/cel/check""", options=__options)

    def validate_expression_against_requester(self, expression: str, channelId: str | None = None):
        """Validate if the current user matches a CEL expression

        expression: The CEL expression to validate against the current user.
        channelId: The channel ID for channel-specific permission checks (required for channel admins).

        `Read in Mattermost API docs (access_control - ValidateExpressionAgainstRequester) <https://developers.mattermost.com/api-documentation/#/operations/ValidateExpressionAgainstRequester>`_

        """
        __options = {"expression": expression, "channelId": channelId}
        return self.client.post("""/api/v4/access_control_policies/cel/validate_requester""", options=__options)

    def test_access_control_policy_expression(self, options: Any):
        """Test an access control policy expression
        `Read in Mattermost API docs (access_control - TestAccessControlPolicyExpression) <https://developers.mattermost.com/api-documentation/#/operations/TestAccessControlPolicyExpression>`_

        """
        return self.client.post("""/api/v4/access_control_policies/cel/test""", options=options)

    def search_access_control_policies(self, options: Any):
        """Search access control policies
        `Read in Mattermost API docs (access_control - SearchAccessControlPolicies) <https://developers.mattermost.com/api-documentation/#/operations/SearchAccessControlPolicies>`_

        """
        return self.client.post("""/api/v4/access_control_policies/search""", options=options)

    def get_access_control_policy_autocomplete_fields(self, after: str | None = None, limit: int = 60):
        """Get autocomplete fields for access control policies

        after: The field ID to start after for pagination.
        limit: The maximum number of fields to return.

        `Read in Mattermost API docs (access_control - GetAccessControlPolicyAutocompleteFields) <https://developers.mattermost.com/api-documentation/#/operations/GetAccessControlPolicyAutocompleteFields>`_

        """
        __params = {"after": after, "limit": limit}
        return self.client.get("""/api/v4/access_control_policies/cel/autocomplete/fields""", params=__params)

    def get_access_control_policy(self, policy_id: str):
        """Get an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - GetAccessControlPolicy) <https://developers.mattermost.com/api-documentation/#/operations/GetAccessControlPolicy>`_

        """
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}")

    def delete_access_control_policy(self, policy_id: str):
        """Delete an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - DeleteAccessControlPolicy) <https://developers.mattermost.com/api-documentation/#/operations/DeleteAccessControlPolicy>`_

        """
        return self.client.delete(f"/api/v4/access_control_policies/{policy_id}")

    def update_access_control_policy_active_status(self, policy_id: str, active: bool):
        """Activate or deactivate an access control policy

        policy_id: The ID of the access control policy.
        active: Set to "true" to activate, "false" to deactivate.

        `Read in Mattermost API docs (access_control - UpdateAccessControlPolicyActiveStatus) <https://developers.mattermost.com/api-documentation/#/operations/UpdateAccessControlPolicyActiveStatus>`_

        """
        __params = {"active": active}
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}/activate", params=__params)

    def assign_access_control_policy_to_channels(self, policy_id: str, channel_ids: list[str] | None = None):
        """Assign an access control policy to channels

        policy_id: The ID of the access control policy.
        channel_ids: The IDs of the channels to assign the policy to.

        `Read in Mattermost API docs (access_control - AssignAccessControlPolicyToChannels) <https://developers.mattermost.com/api-documentation/#/operations/AssignAccessControlPolicyToChannels>`_

        """
        __options = {"channel_ids": channel_ids}
        return self.client.post(f"/api/v4/access_control_policies/{policy_id}/assign", options=__options)

    def unassign_access_control_policy_from_channels(self, policy_id: str, channel_ids: list[str] | None = None):
        """Unassign an access control policy from channels

        policy_id: The ID of the access control policy.
        channel_ids: The IDs of the channels to unassign the policy from.

        `Read in Mattermost API docs (access_control - UnassignAccessControlPolicyFromChannels) <https://developers.mattermost.com/api-documentation/#/operations/UnassignAccessControlPolicyFromChannels>`_

        """
        __params = {"channel_ids": channel_ids}
        return self.client.delete(f"/api/v4/access_control_policies/{policy_id}/unassign", params=__params)

    def get_channels_for_access_control_policy(self, policy_id: str, after: str | None = None, limit: int = 60):
        """Get channels for an access control policy

        policy_id: The ID of the access control policy.
        after: The channel ID to start after for pagination.
        limit: The maximum number of channels to return.

        `Read in Mattermost API docs (access_control - GetChannelsForAccessControlPolicy) <https://developers.mattermost.com/api-documentation/#/operations/GetChannelsForAccessControlPolicy>`_

        """
        __params = {"after": after, "limit": limit}
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}/resources/channels", params=__params)

    def search_channels_for_access_control_policy(self, policy_id: str, options: Any):
        """Search channels for an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - SearchChannelsForAccessControlPolicy) <https://developers.mattermost.com/api-documentation/#/operations/SearchChannelsForAccessControlPolicy>`_

        """
        return self.client.post(
            f"/api/v4/access_control_policies/{policy_id}/resources/channels/search", options=options
        )

    def get_channel_access_control_attributes(self, channel_id: str):
        """Get access control attributes for a channel

        channel_id: The ID of the channel.

        `Read in Mattermost API docs (access_control - GetChannelAccessControlAttributes) <https://developers.mattermost.com/api-documentation/#/operations/GetChannelAccessControlAttributes>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/access_control/attributes")

    def get_cel_visual_ast(self, options: Any):
        """Get the visual AST for a CEL expression
        `Read in Mattermost API docs (access_control - GetCELVisualAST) <https://developers.mattermost.com/api-documentation/#/operations/GetCELVisualAST>`_

        """
        return self.client.post("""/api/v4/access_control_policies/cel/visual_ast""", options=options)
