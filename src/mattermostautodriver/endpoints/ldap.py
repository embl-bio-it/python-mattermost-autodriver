from .base import Base


class Ldap(Base):

    def get_ldap_groups(self, params=None):
        """Returns a list of LDAP groups

        q: Search term
        page: The page to select.
        per_page: The number of users per page. There is a maximum limit of 200 users per page.

        `Read in Mattermost API docs (ldap - GetLdapGroups) <https://api.mattermost.com/#tag/ldap/operation/GetLdapGroups>`_

        """
        return self.client.get("""/api/v4/ldap/groups""", params=params)

    def link_ldap_group(self, remote_id):
        """Link a LDAP group

        remote_id: Group GUID

        `Read in Mattermost API docs (ldap - LinkLdapGroup) <https://api.mattermost.com/#tag/ldap/operation/LinkLdapGroup>`_

        """
        return self.client.post(f"/api/v4/ldap/groups/{remote_id}/link")
