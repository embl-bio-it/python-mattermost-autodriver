from .base import Base


class Migrate(Base):
    def migrate_auth_to_ldap(self, options=None):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:
        """
        return self.client.post("""/users/migrate_auth/ldap""", options=options)

    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:
        """
        return self.client.post("""/users/migrate_auth/saml""", options=options)
