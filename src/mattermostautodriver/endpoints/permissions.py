from .base import Base


class Permissions(Base):
    def get_ancillary_permissions(self, params=None):
        """Return all system console subsection ancillary permissions

        subsection_permissions: The subsection permissions to return the ancillary permissions for. These values are comma seperated. Ex. subsection_permissions=sysconsole_read_reporting_site_statistics,sysconsole_write_reporting_site_statistics,sysconsole_write_user_management_channels


        `Read in Mattermost API docs (permissions - GetAncillaryPermissions) <https://api.mattermost.com/#tag/permissions/operation/GetAncillaryPermissions>`_
        """
        return self.client.get("""/permissions/ancillary""", params=params)
