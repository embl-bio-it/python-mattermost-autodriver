from .base import Base
from typing import Any


class CustomProfileAttributes(Base):

    def list_all_cpa_fields(self):
        """List all the Custom Profile Attributes fields
        `Read in Mattermost API docs (custom_profile_attributes - ListAllCPAFields) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/ListAllCPAFields>`_

        """
        return self.client.get("""/api/v4/custom_profile_attributes/fields""")

    def create_cpa_field(self, name: str, type: str, attrs: str | None = None):
        """Create a Custom Profile Attribute field

        name:
        type:
        attrs:

        `Read in Mattermost API docs (custom_profile_attributes - CreateCPAField) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/CreateCPAField>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"name": name, "type": type, "attrs": attrs}
        return self.client.post(
            """/api/v4/custom_profile_attributes/fields""", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def patch_cpa_field(
        self, field_id: str, name: str | None = None, type: str | None = None, attrs: str | None = None
    ):
        """Patch a Custom Profile Attribute field

        field_id: Custom Profile Attribute field GUID
        name:
        type:
        attrs:

        `Read in Mattermost API docs (custom_profile_attributes - PatchCPAField) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/PatchCPAField>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"name": name, "type": type, "attrs": attrs}
        return self.client.patch(
            f"/api/v4/custom_profile_attributes/fields/{field_id}", options=options_71f8b7431cd64fcfa0dabd300d0636d2
        )

    def delete_cpa_field(self, field_id: str):
        """Delete a Custom Profile Attribute field

        field_id: Custom Profile Attribute field GUID

        `Read in Mattermost API docs (custom_profile_attributes - DeleteCPAField) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/DeleteCPAField>`_

        """
        return self.client.delete(f"/api/v4/custom_profile_attributes/fields/{field_id}")

    def patch_cpa_values(self, options: list[dict[str, Any]]):
        """Patch Custom Profile Attribute values
        `Read in Mattermost API docs (custom_profile_attributes - PatchCPAValues) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/PatchCPAValues>`_

        """
        return self.client.patch("""/api/v4/custom_profile_attributes/values""", options=options)

    def get_cpa_group(self):
        """Get Custom Profile Attribute property group data
        `Read in Mattermost API docs (custom_profile_attributes - GetCPAGroup) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/GetCPAGroup>`_

        """
        return self.client.get("""/api/v4/custom_profile_attributes/group""")

    def list_cpa_values(self, user_id: str):
        """List Custom Profile Attribute values

        user_id: User GUID

        `Read in Mattermost API docs (custom_profile_attributes - ListCPAValues) <https://api.mattermost.com/#tag/custom_profile_attributes/operation/ListCPAValues>`_

        """
        return self.client.get(f"/api/v4/users/{user_id}/custom_profile_attributes")
