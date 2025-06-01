from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Roles"]


class Roles(Base):

    def get_all_roles(self):
        """Get a list of all the roles
        `Read in Mattermost API docs (roles - GetAllRoles) <https://api.mattermost.com/#tag/roles/operation/GetAllRoles>`_

        """
        return self.client.get("""/api/v4/roles""")

    def get_role(self, role_id: str):
        """Get a role

        role_id: Role GUID

        `Read in Mattermost API docs (roles - GetRole) <https://api.mattermost.com/#tag/roles/operation/GetRole>`_

        """
        return self.client.get(f"/api/v4/roles/{role_id}")

    def get_role_by_name(self, role_name: str):
        """Get a role

        role_name: Role Name

        `Read in Mattermost API docs (roles - GetRoleByName) <https://api.mattermost.com/#tag/roles/operation/GetRoleByName>`_

        """
        return self.client.get(f"/api/v4/roles/name/{role_name}")

    def patch_role(self, role_id: str, permissions: list[str] | None = None):
        """Patch a role

        role_id: Role GUID
        permissions: The permissions the role should grant.

        `Read in Mattermost API docs (roles - PatchRole) <https://api.mattermost.com/#tag/roles/operation/PatchRole>`_

        """
        __options = {"permissions": permissions}
        return self.client.put(f"/api/v4/roles/{role_id}/patch", options=__options)

    def get_roles_by_names(self, options: list[str]):
        """Get a list of roles by name
        `Read in Mattermost API docs (roles - GetRolesByNames) <https://api.mattermost.com/#tag/roles/operation/GetRolesByNames>`_

        """
        return self.client.post("""/api/v4/roles/names""", options=options)
