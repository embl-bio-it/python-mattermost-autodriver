from ._base import Base

__all__ = ["Permissions"]


class Permissions(Base):

    def get_ancillary_permissions_post(self, options):
        """Return all system console subsection ancillary permissions
        `Read in Mattermost API docs (permissions - GetAncillaryPermissionsPost) <https://developers.mattermost.com/api-documentation/#/operations/GetAncillaryPermissionsPost>`_

        """
        return self.client.post("""/api/v4/permissions/ancillary""", options=options)
