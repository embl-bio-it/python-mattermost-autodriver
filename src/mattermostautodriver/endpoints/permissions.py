from .base import Base
from typing import Any, BinaryIO


class Permissions(Base):

    def get_ancillary_permissions_post(self, options: list[str]):
        """Return all system console subsection ancillary permissions
        `Read in Mattermost API docs (permissions - GetAncillaryPermissionsPost) <https://api.mattermost.com/#tag/permissions/operation/GetAncillaryPermissionsPost>`_

        """
        return self.client.post("""/api/v4/permissions/ancillary""", options=options)
