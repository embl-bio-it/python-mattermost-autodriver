from .base import Base
from typing import Any, BinaryIO


class Authentication(Base):

    def migrate_auth_to_ldap(self, from_: str, match_field: str, force: bool):
        """Migrate user accounts authentication type to LDAP.

        from: The current authentication type for the matched users.
        match_field: Foreign user field name to match.
        force:

        `Read in Mattermost API docs (authentication - MigrateAuthToLdap) <https://api.mattermost.com/#tag/authentication/operation/MigrateAuthToLdap>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"from": from_, "match_field": match_field, "force": force}
        return self.client.post("""/api/v4/users/migrate_auth/ldap""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)

    def migrate_auth_to_saml(self, from_: str, matches: dict[str, Any], auto: bool):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (authentication - MigrateAuthToSaml) <https://api.mattermost.com/#tag/authentication/operation/MigrateAuthToSaml>`_

        """
        options_71f8b7431cd64fcfa0dabd300d0636d2 = {"from": from_, "matches": matches, "auto": auto}
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=options_71f8b7431cd64fcfa0dabd300d0636d2)
