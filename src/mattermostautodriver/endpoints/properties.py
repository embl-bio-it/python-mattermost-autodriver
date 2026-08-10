from ._base import Base, FileType
from typing import Any

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
        linked_field_id: str | None = None,
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

        linked_field_id: The ID of a template field to link to. The source must be a template field in the same group, must not itself be linked, and must not be deleted. When set, the created field inherits the source's type, options, and security attributes; the ``type`` field in the request body is ignored. Can only be set at creation time.


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
            "linked_field_id": linked_field_id,
        }
        return self.client.post(f"/api/v4/properties/groups/{group_name}/{object_type}/fields", options=__options)

    def get_property_fields(
        self,
        group_name: str,
        object_type: str,
        channel_id: str | None = None,
        team_id: str | None = None,
        target_type: str | None = None,
        target_id: str | None = None,
        since: int | None = None,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        cursor_update_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Get property fields

        group_name: The name of the property group
        object_type: The type of object to retrieve property fields for
        channel_id: Hierarchical scope. When set, the response includes system-level rows, team-level rows for the channel's team, and channel-level rows for this channel. Mutually exclusive with ``target_type`` and ``target_id``. Requires ``read_channel`` on the channel.

        team_id: Hierarchical scope. When set without ``channel_id``, the response includes system-level and team-level rows for this team. When ``channel_id`` is also set, this value is ignored — the channel's team is resolved server-side and used instead. Mutually exclusive with ``target_type`` and ``target_id``. Requires ``view_team`` on the team.

        target_type: Single-target scope. One of ``system``, ``team``, or ``channel``. Required in single-target mode. Mutually exclusive with ``channel_id`` and ``team_id``.

        target_id: Single-target scope. Required when ``target_type`` is ``channel`` or ``team``. Mutually exclusive with ``channel_id`` and ``team_id``.

        since: Unix timestamp in milliseconds. When greater than 0, returns fields with ``update_at`` greater than or equal to this value, including tombstones.

        cursor_id: The ID of the last property field from the previous page, for cursor-based pagination.
        cursor_create_at: The ``create_at`` timestamp of the last property field from the previous page. Required alongside ``cursor_id`` when ``since`` is absent. Mutually exclusive with ``cursor_update_at``.

        cursor_update_at: The ``update_at`` timestamp of the last property field from the previous page. Required alongside ``cursor_id`` when ``since`` is present. Mutually exclusive with ``cursor_create_at``.

        per_page: The number of property fields per page.

        `Read in Mattermost API docs (properties - GetPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/GetPropertyFields>`_

        """
        __params = {
            "channel_id": channel_id,
            "team_id": team_id,
            "target_type": target_type,
            "target_id": target_id,
            "since": since,
            "cursor_id": cursor_id,
            "cursor_create_at": cursor_create_at,
            "cursor_update_at": cursor_update_at,
            "per_page": per_page,
        }
        return self.client.get(f"/api/v4/properties/groups/{group_name}/{object_type}/fields", params=__params)

    def search_property_fields(
        self,
        group_name: str,
        object_types: list[str],
        channel_id: str | None = None,
        team_id: str | None = None,
        target_type: str | None = None,
        target_id: str | None = None,
        since: int | None = None,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        cursor_update_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Search property fields across multiple object types

        group_name: The name of the property group
        object_types: One or more object types to include in the response. At least one value is required; unknown values return 400.

        channel_id: Hierarchical scope. When set, the response includes system-level rows, team-level rows for the channel's team, and channel-level rows for this channel across every requested ``object_types``. Mutually exclusive with ``target_type``/``target_id``. Requires ``read_channel`` on the channel.

        team_id: Hierarchical scope. When set without ``channel_id``, the response includes system-level and team-level rows for this team across every requested ``object_types``. When ``channel_id`` is also set, this value is ignored — the channel's team is resolved server-side and used instead. Mutually exclusive with ``target_type``/``target_id``. Requires ``view_team`` on the team.

        target_type: Single-target scope. Mutually exclusive with ``channel_id`` and ``team_id``. Required if no hierarchical scope is given, except when ``object_types`` is exactly ``["system"]`` — in that case any scope or target params are ignored and the endpoint resolves to ``target_type=system``.

        target_id: Single-target scope. Required when ``target_type`` is ``channel`` or ``team``. Mutually exclusive with ``channel_id`` and ``team_id``.

        since: Unix timestamp in milliseconds. When greater than 0, returns fields with ``update_at`` greater than or equal to this value, including tombstones.

        cursor_id: The ID of the last property field from the previous page, for cursor-based pagination.
        cursor_create_at: The ``create_at`` timestamp of the last property field from the previous page. Required alongside ``cursor_id`` when ``since`` is absent. Mutually exclusive with ``cursor_update_at``.

        cursor_update_at: The ``update_at`` timestamp of the last property field from the previous page. Required alongside ``cursor_id`` when ``since`` is present. Mutually exclusive with ``cursor_create_at``.

        per_page: The number of property fields per page.

        `Read in Mattermost API docs (properties - SearchPropertyFields) <https://developers.mattermost.com/api-documentation/#/operations/SearchPropertyFields>`_

        """
        __options = {
            "object_types": object_types,
            "channel_id": channel_id,
            "team_id": team_id,
            "target_type": target_type,
            "target_id": target_id,
            "since": since,
            "cursor_id": cursor_id,
            "cursor_create_at": cursor_create_at,
            "cursor_update_at": cursor_update_at,
            "per_page": per_page,
        }
        return self.client.post(f"/api/v4/properties/groups/{group_name}/fields/search", options=__options)

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
        since: int | None = None,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        cursor_update_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Get property values for a target

        group_name: The name of the property group
        object_type: The type of object
        target_id: The ID of the target object
        since: Unix timestamp in milliseconds. When greater than 0, returns values with ``update_at`` greater than or equal to this value, including tombstones.

        cursor_id: The ID of the last property value from the previous page, for cursor-based pagination.
        cursor_create_at: The ``create_at`` timestamp of the last property value from the previous page. Required alongside ``cursor_id`` when ``since`` is absent. Mutually exclusive with ``cursor_update_at``.

        cursor_update_at: The ``update_at`` timestamp of the last property value from the previous page. Required alongside ``cursor_id`` when ``since`` is present. Mutually exclusive with ``cursor_create_at``.

        per_page: The number of property values per page.

        `Read in Mattermost API docs (properties - GetPropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/GetPropertyValues>`_

        """
        __params = {
            "since": since,
            "cursor_id": cursor_id,
            "cursor_create_at": cursor_create_at,
            "cursor_update_at": cursor_update_at,
            "per_page": per_page,
        }
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

    def get_system_property_values(
        self,
        group_name: str,
        since: int | None = None,
        cursor_id: str | None = None,
        cursor_create_at: int | None = None,
        cursor_update_at: int | None = None,
        per_page: int | None = 60,
    ):
        """Get property values for the system

        group_name: The name of the property group
        since: Unix timestamp in milliseconds. When greater than 0, returns values with ``update_at`` greater than or equal to this value, including tombstones.

        cursor_id: The ID of the last property value from the previous page, for cursor-based pagination.
        cursor_create_at: The ``create_at`` timestamp of the last property value from the previous page. Required alongside ``cursor_id`` when ``since`` is absent. Mutually exclusive with ``cursor_update_at``.

        cursor_update_at: The ``update_at`` timestamp of the last property value from the previous page. Required alongside ``cursor_id`` when ``since`` is present. Mutually exclusive with ``cursor_create_at``.

        per_page: The number of property values per page.

        `Read in Mattermost API docs (properties - GetSystemPropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/GetSystemPropertyValues>`_

        """
        __params = {
            "since": since,
            "cursor_id": cursor_id,
            "cursor_create_at": cursor_create_at,
            "cursor_update_at": cursor_update_at,
            "per_page": per_page,
        }
        return self.client.get(f"/api/v4/properties/groups/{group_name}/system/values", params=__params)

    def update_system_property_values(self, group_name: str, options: list[dict[str, Any]]):
        """Update property values for the system

        group_name: The name of the property group

        `Read in Mattermost API docs (properties - UpdateSystemPropertyValues) <https://developers.mattermost.com/api-documentation/#/operations/UpdateSystemPropertyValues>`_

        """
        return self.client.patch(f"/api/v4/properties/groups/{group_name}/system/values", options=options)
