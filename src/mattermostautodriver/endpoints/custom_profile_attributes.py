from ._base import Base
from typing import Any, BinaryIO

__all__ = ["CustomProfileAttributes"]


class CustomProfileAttributes(Base):

    def list_all_cpa_fields(self):
        """List all the Custom Profile Attributes fields
        `Read in Mattermost API docs (custom_profile_attributes - ListAllCPAFields) <https://developers.mattermost.com/api-documentation/#/operations/ListAllCPAFields>`_

        """
        return self.client.get("""/api/v4/custom_profile_attributes/fields""")

    def create_cpa_field(self, name: str, type: str, attrs: dict[str, Any] | None = None):
        """Create a Custom Profile Attribute field

        name:
        type:
        attrs:

        `Read in Mattermost API docs (custom_profile_attributes - CreateCPAField) <https://developers.mattermost.com/api-documentation/#/operations/CreateCPAField>`_

        """
        __options = {"name": name, "type": type, "attrs": attrs}
        return self.client.post("""/api/v4/custom_profile_attributes/fields""", options=__options)

    def patch_cpa_field(
        self, field_id: str, name: str | None = None, type: str | None = None, attrs: dict[str, Any] | None = None
    ):
        """Patch a Custom Profile Attribute field

        field_id: Custom Profile Attribute field GUID
        name:
        type:
        attrs:

        `Read in Mattermost API docs (custom_profile_attributes - PatchCPAField) <https://developers.mattermost.com/api-documentation/#/operations/PatchCPAField>`_

        """
        __options = {"name": name, "type": type, "attrs": attrs}
        return self.client.patch(f"/api/v4/custom_profile_attributes/fields/{field_id}", options=__options)

    def delete_cpa_field(self, field_id: str):
        """Delete a Custom Profile Attribute field

        field_id: Custom Profile Attribute field GUID

        `Read in Mattermost API docs (custom_profile_attributes - DeleteCPAField) <https://developers.mattermost.com/api-documentation/#/operations/DeleteCPAField>`_

        """
        return self.client.delete(f"/api/v4/custom_profile_attributes/fields/{field_id}")

    def patch_cpa_values(self, options: list[dict[str, Any]]):
        """Patch Custom Profile Attribute values
        `Read in Mattermost API docs (custom_profile_attributes - PatchCPAValues) <https://developers.mattermost.com/api-documentation/#/operations/PatchCPAValues>`_

        """
        return self.client.patch("""/api/v4/custom_profile_attributes/values""", options=options)

    def get_cpa_group(self):
        """Get Custom Profile Attribute property group data
        `Read in Mattermost API docs (custom_profile_attributes - GetCPAGroup) <https://developers.mattermost.com/api-documentation/#/operations/GetCPAGroup>`_

        """
        return self.client.get("""/api/v4/custom_profile_attributes/group""")

    def list_cpa_values(self, user_id: str):
        """List Custom Profile Attribute values

        user_id: User GUID

        `Read in Mattermost API docs (custom_profile_attributes - ListCPAValues) <https://developers.mattermost.com/api-documentation/#/operations/ListCPAValues>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/custom_profile_attributes")

    def patch_cpa_values_for_user(self, user_id: str, options: list[dict[str, Any]]):
        """Update custom profile attribute values for a user

        user_id: User GUID

        `Read in Mattermost API docs (custom_profile_attributes - PatchCPAValuesForUser) <https://developers.mattermost.com/api-documentation/#/operations/PatchCPAValuesForUser>`_

        """
        return self.client.patch(f"/api/v4/users/{user_id}/custom_profile_attributes", options=options)
