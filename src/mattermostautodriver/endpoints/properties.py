from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Properties"]


class Properties(Base):

    def create_property_field(
        self,
        group_name: str,
        object_type: str,
        name: str,
        type: str,
        target_type: str,
        attrs: dict[str, Any] | None = None,
        target_id: str | None = None,
        permission_field: str | None = "member",
        permission_values: str | None = "member",
        permission_options: str | None = "member",
    ):
        """Create a property field

        group_name: The name of the property group
        object_type: The type of object this property field applies to
        name: The name of the property field
        type: The type of property field
        attrs: Additional attributes for the property field
        target_type: The scope level of the property
        target_id: The ID of the target
        permission_field: Permission level for editing the field definition. Only system admins can set this; ignored for non-admin users.

        permission_values: Permission level for setting values on objects. Only system admins can set this; ignored for non-admin users.

        permission_options: Permission level for managing options on select/multiselect fields. Only system admins can set this; ignored for non-admin users.


        `Read in Mattermost API docs (properties - CreatePropertyField) <https://developers.mattermost.com/api-documentation/#/operations/CreatePropertyField>`_

        """
        __options = {
            "name": name,
            "type": type,
            "attrs": attrs,
            "target_type": target_type,
            "target_id": target_id,
            "permission_field": permission_field,
            "permission_values": permission_values,
            "permission_options": permission_options,
        }
        return self.client.post(f"/api/v4/properties/groups/{group_name}/{object_type}/fields", options=__options)

    def get_property_fields(
        self,
        group_name: str,
        object_type: str,
        target_type: str,
        target_id: str | None = None,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Get property fields

        group_name: The name of the property group
        object_type: The type of object to retrieve property fields for
        target_type: The scope level to query. Must be one of 'system', 'team', or 'channel'.
        target_id: Filter by target ID. Required when target_type is 'channel' or 'team'.
        cursor_id: The ID of the last property field from the previous page, for cursor-based pagination.
        cursor_create_at: The create_at timestamp of the last property field from the previous page. Must be provided together with cursor_id.
        per_page: The number of property fields per page.

        `Read in Mattermost API docs (properties - GetPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/GetPropertyFields>`_

        """
        __params = {
            "target_type": target_type,
            "target_id": target_id,
            "cursor_id": cursor_id,
            "cursor_create_at": cursor_create_at,
            "per_page": per_page,
        }
        return self.client.get(f"/api/v4/properties/groups/{group_name}/{object_type}/fields", params=__params)

    def update_property_field(self, group_name: str, object_type: str, field_id: str, options: Any):
        """Update a property field

        group_name: The name of the property group
        object_type: The type of object this property field applies to
        field_id: Property field ID

        `Read in Mattermost API docs (properties - UpdatePropertyField) <https://developers.mattermost.com/api-documentation/#/operations/UpdatePropertyField>`_

        """
        return self.client.patch(
            f"/api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}", options=options
        )

    def delete_property_field(self, group_name: str, object_type: str, field_id: str):
        """Delete a property field

        group_name: The name of the property group
        object_type: The type of object this property field applies to
        field_id: Property field ID

        `Read in Mattermost API docs (properties - DeletePropertyField) <https://developers.mattermost.com/api-documentation/#/operations/DeletePropertyField>`_

        """
        return self.client.delete(f"/api/v4/properties/groups/{group_name}/{object_type}/fields/{field_id}")

    def get_property_values(
        self,
        group_name: str,
        object_type: str,
        target_id: str,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Get property values for a target

        group_name: The name of the property group
        object_type: The type of object
        target_id: The ID of the target object
        cursor_id: The ID of the last property value from the previous page, for cursor-based pagination.
        cursor_create_at: The create_at timestamp of the last property value from the previous page. Must be provided together with cursor_id.
        per_page: The number of property values per page.

        `Read in Mattermost API docs (properties - GetPropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/GetPropertyValues>`_

        """
        __params = {"cursor_id": cursor_id, "cursor_create_at": cursor_create_at, "per_page": per_page}
        return self.client.get(
            f"/api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}", params=__params
        )

    def update_property_values(self, group_name: str, object_type: str, target_id: str, options: list[dict[str, Any]]):
        """Update property values for a target

        group_name: The name of the property group
        object_type: The type of object
        target_id: The ID of the target object

        `Read in Mattermost API docs (properties - UpdatePropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/UpdatePropertyValues>`_

        """
        return self.client.patch(
            f"/api/v4/properties/groups/{group_name}/{object_type}/values/{target_id}", options=options
        )
