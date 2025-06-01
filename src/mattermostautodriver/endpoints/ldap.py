from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Ldap"]


class Ldap(Base):

    def get_ldap_groups(self, q: str | None = None, page: int | None = 0, per_page: int | None = 60):
        """Returns a list of LDAP groups

        q: Search term
        page: The page to select.
        per_page: The number of users per page. per page.

        `Read in Mattermost API docs (ldap - GetLdapGroups) <https://api.mattermost.com/#tag/ldap/operation/GetLdapGroups>`_

        """
        __params = {"q": q, "page": page, "per_page": per_page}
        return self.client.get("""/api/v4/ldap/groups""", params=__params)

    def link_ldap_group(self, remote_id: str):
        """Link a LDAP group

        remote_id: Group GUID

        `Read in Mattermost API docs (ldap - LinkLdapGroup) <https://api.mattermost.com/#tag/ldap/operation/LinkLdapGroup>`_

        """
        return self.client.post(f"/api/v4/ldap/groups/{remote_id}/link")
