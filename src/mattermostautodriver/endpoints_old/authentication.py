from ._base import Base

__all__ = ["Authentication"]


class Authentication(Base):

    def migrate_auth_to_ldap(self, options=None):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (authentication - MigrateAuthToLdap) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToLdap>`_

        """
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=options)

    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (authentication - MigrateAuthToSaml) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToSaml>`_

        """
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=options)
