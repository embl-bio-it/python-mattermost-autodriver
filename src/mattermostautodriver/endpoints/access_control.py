from .base import Base


class AccessControl(Base):

    def create_access_control_policy(self, options):
        """Create an access control policy
        `Read in Mattermost API docs (access_control - CreateAccessControlPolicy) <https://api.mattermost.com/#tag/access_control/operation/CreateAccessControlPolicy>`_

        """
        return self.client.put("""/api/v4/access_control_policies""", options=options)

    def check_access_control_policy_expression(self, options):
        """Check an access control policy expression

        expression: The expression to check.

        `Read in Mattermost API docs (access_control - CheckAccessControlPolicyExpression) <https://api.mattermost.com/#tag/access_control/operation/CheckAccessControlPolicyExpression>`_

        """
        return self.client.post("""/api/v4/access_control_policies/cel/check""", options=options)

    def test_access_control_policy_expression(self, options):
        """Test an access control policy expression
        `Read in Mattermost API docs (access_control - TestAccessControlPolicyExpression) <https://api.mattermost.com/#tag/access_control/operation/TestAccessControlPolicyExpression>`_

        """
        return self.client.post("""/api/v4/access_control_policies/cel/test""", options=options)

    def search_access_control_policies(self, options):
        """Search access control policies
        `Read in Mattermost API docs (access_control - SearchAccessControlPolicies) <https://api.mattermost.com/#tag/access_control/operation/SearchAccessControlPolicies>`_

        """
        return self.client.post("""/api/v4/access_control_policies/search""", options=options)

    def get_access_control_policy_autocomplete_fields(self, params=None):
        """Get autocomplete fields for access control policies

        after: The field ID to start after for pagination.
        limit: The maximum number of fields to return.

        `Read in Mattermost API docs (access_control - GetAccessControlPolicyAutocompleteFields) <https://api.mattermost.com/#tag/access_control/operation/GetAccessControlPolicyAutocompleteFields>`_

        """
        return self.client.get("""/api/v4/access_control_policies/cel/autocomplete/fields""", params=params)

    def get_access_control_policy(self, policy_id):
        """Get an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - GetAccessControlPolicy) <https://api.mattermost.com/#tag/access_control/operation/GetAccessControlPolicy>`_

        """
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}")

    def delete_access_control_policy(self, policy_id):
        """Delete an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - DeleteAccessControlPolicy) <https://api.mattermost.com/#tag/access_control/operation/DeleteAccessControlPolicy>`_

        """
        return self.client.delete(f"/api/v4/access_control_policies/{policy_id}")

    def update_access_control_policy_active_status(self, policy_id, params=None):
        """Activate or deactivate an access control policy

        policy_id: The ID of the access control policy.
        active: Set to "true" to activate, "false" to deactivate.

        `Read in Mattermost API docs (access_control - UpdateAccessControlPolicyActiveStatus) <https://api.mattermost.com/#tag/access_control/operation/UpdateAccessControlPolicyActiveStatus>`_

        """
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}/activate", params=params)

    def assign_access_control_policy_to_channels(self, policy_id, options):
        """Assign an access control policy to channels

        policy_id: The ID of the access control policy.
        channel_ids: The IDs of the channels to assign the policy to.

        `Read in Mattermost API docs (access_control - AssignAccessControlPolicyToChannels) <https://api.mattermost.com/#tag/access_control/operation/AssignAccessControlPolicyToChannels>`_

        """
        return self.client.post(f"/api/v4/access_control_policies/{policy_id}/assign", options=options)

    def unassign_access_control_policy_from_channels(self, policy_id, params):
        """Unassign an access control policy from channels

        policy_id: The ID of the access control policy.
        channel_ids: The IDs of the channels to unassign the policy from.

        `Read in Mattermost API docs (access_control - UnassignAccessControlPolicyFromChannels) <https://api.mattermost.com/#tag/access_control/operation/UnassignAccessControlPolicyFromChannels>`_

        """
        return self.client.delete(f"/api/v4/access_control_policies/{policy_id}/unassign", params=params)

    def get_channels_for_access_control_policy(self, policy_id, params=None):
        """Get channels for an access control policy

        policy_id: The ID of the access control policy.
        after: The channel ID to start after for pagination.
        limit: The maximum number of channels to return.

        `Read in Mattermost API docs (access_control - GetChannelsForAccessControlPolicy) <https://api.mattermost.com/#tag/access_control/operation/GetChannelsForAccessControlPolicy>`_

        """
        return self.client.get(f"/api/v4/access_control_policies/{policy_id}/resources/channels", params=params)

    def search_channels_for_access_control_policy(self, policy_id, options):
        """Search channels for an access control policy

        policy_id: The ID of the access control policy.

        `Read in Mattermost API docs (access_control - SearchChannelsForAccessControlPolicy) <https://api.mattermost.com/#tag/access_control/operation/SearchChannelsForAccessControlPolicy>`_

        """
        return self.client.post(
            f"/api/v4/access_control_policies/{policy_id}/resources/channels/search", options=options
        )

    def get_channel_access_control_attributes(self, channel_id):
        """Get access control attributes for a channel

        channel_id: The ID of the channel.

        `Read in Mattermost API docs (access_control - GetChannelAccessControlAttributes) <https://api.mattermost.com/#tag/access_control/operation/GetChannelAccessControlAttributes>`_

        """
        return self.client.get(f"/api/v4/channels/{channel_id}/access_control/attributes")

    def get_cel_visual_ast(self, options):
        """Get the visual AST for a CEL expression
        `Read in Mattermost API docs (access_control - GetCELVisualAST) <https://api.mattermost.com/#tag/access_control/operation/GetCELVisualAST>`_

        """
        return self.client.post("""/api/v4/access_control_policies/cel/visual_ast""", options=options)
