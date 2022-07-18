from .base import Base


class Roles(Base):
    def get_all_roles(self):
        """Get a list of all the roles"""
        return self.client.get("""/roles""")

    def get_role(self, role_id):
        """Get a role

        role_id: Role GUID
        """
        return self.client.get(f"/roles/{role_id}")

    def get_role_by_name(self, role_name):
        """Get a role

        role_name: Role Name
        """
        return self.client.get(f"/roles/name/{role_name}")

    def patch_role(self, role_id, options):
        """Patch a role

        role_id: Role GUID
        permissions: The permissions the role should grant.
        """
        return self.client.put(f"/roles/{role_id}/patch", options=options)

    def get_roles_by_names(self, options):
        """Get a list of roles by name"""
        return self.client.post("""/roles/names""", options=options)
