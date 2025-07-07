from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Ldap"]


class Ldap(Base):

    def migrate_auth_to_ldap(self, from_: str, match_field: str, force: bool):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (ldap - MigrateAuthToLdap) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToLdap>`_

        """
        __options = {"from": from_, "match_field": match_field, "force": force}
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=__options)

    def sync_ldap(self):
        """Sync with LDAP
        `Read in Mattermost API docs (ldap - SyncLdap) <https://developers.mattermost.com/api-documentation/#/operations/SyncLdap>`_

        """
        return self.client.post("""/api/v4/ldap/sync""")

    def test_ldap(self):
        """Test LDAP configuration
        `Read in Mattermost API docs (ldap - TestLdap) <https://developers.mattermost.com/api-documentation/#/operations/TestLdap>`_

        """
        return self.client.post("""/api/v4/ldap/test""")

    def test_ldap_connection(self, options: Any):
        """Test LDAP connection with specific settings
        `Read in Mattermost API docs (ldap - TestLdapConnection) <https://developers.mattermost.com/api-documentation/#/operations/TestLdapConnection>`_

        """
        return self.client.post("""/api/v4/ldap/test_connection""", options=options)

    def test_ldap_diagnostics(self, options: Any):
        """Test LDAP diagnostics with specific settings
        `Read in Mattermost API docs (ldap - TestLdapDiagnostics) <https://developers.mattermost.com/api-documentation/#/operations/TestLdapDiagnostics>`_

        """
        return self.client.post("""/api/v4/ldap/test_diagnostics""", options=options)

    def get_ldap_groups(self, q: str | None = None, page: int | None = 0, per_page: int | None = 60):
        """Returns a list of LDAP groups

        q: Search term
        page: The page to select.
        per_page: The number of users per page. per page.

        `Read in Mattermost API docs (ldap - GetLdapGroups) <https://developers.mattermost.com/api-documentation/#/operations/GetLdapGroups>`_

        """
        __params = {"q": q, "page": page, "per_page": per_page}
        return self.client.get("""/api/v4/ldap/groups""", params=__params)

    def link_ldap_group(self, remote_id: str):
        """Link a LDAP group

        remote_id: Group GUID

        `Read in Mattermost API docs (ldap - LinkLdapGroup) <https://developers.mattermost.com/api-documentation/#/operations/LinkLdapGroup>`_

        """
        return self.client.post(f"/api/v4/ldap/groups/{remote_id}/link")

    def migrate_id_ldap(self, toAttribute: str):
        """Migrate Id LDAP

        toAttribute: New IdAttribute value

        `Read in Mattermost API docs (ldap - MigrateIdLdap) <https://developers.mattermost.com/api-documentation/#/operations/MigrateIdLdap>`_

        """
        __options = {"toAttribute": toAttribute}
        return self.client.post("""/api/v4/ldap/migrateid""", options=__options)

    def upload_ldap_public_certificate(self, certificate: BinaryIO):
        """Upload public certificate

        certificate: The public certificate file

        `Read in Mattermost API docs (ldap - UploadLdapPublicCertificate) <https://developers.mattermost.com/api-documentation/#/operations/UploadLdapPublicCertificate>`_

        """
        __files = {"certificate": certificate}
        return self.client.post("""/api/v4/ldap/certificate/public""", files=__files)

    def delete_ldap_public_certificate(self):
        """Remove public certificate
        `Read in Mattermost API docs (ldap - DeleteLdapPublicCertificate) <https://developers.mattermost.com/api-documentation/#/operations/DeleteLdapPublicCertificate>`_

        """
        return self.client.delete("""/api/v4/ldap/certificate/public""")

    def upload_ldap_private_certificate(self, certificate: BinaryIO):
        """Upload private key

        certificate: The private key file

        `Read in Mattermost API docs (ldap - UploadLdapPrivateCertificate) <https://developers.mattermost.com/api-documentation/#/operations/UploadLdapPrivateCertificate>`_

        """
        __files = {"certificate": certificate}
        return self.client.post("""/api/v4/ldap/certificate/private""", files=__files)

    def delete_ldap_private_certificate(self):
        """Remove private key
        `Read in Mattermost API docs (ldap - DeleteLdapPrivateCertificate) <https://developers.mattermost.com/api-documentation/#/operations/DeleteLdapPrivateCertificate>`_

        """
        return self.client.delete("""/api/v4/ldap/certificate/private""")

    def add_user_to_group_syncables(self, user_id: str):
        """Create memberships for LDAP configured channels and teams for this user

        user_id: User Id

        `Read in Mattermost API docs (ldap - AddUserToGroupSyncables) <https://developers.mattermost.com/api-documentation/#/operations/AddUserToGroupSyncables>`_

        """
        return self.client.post(f"/api/v4/ldap/users/{user_id}/group_sync_memberships")
