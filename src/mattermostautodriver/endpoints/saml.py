from .base import Base


class Saml(Base):
    def migrate_auth_to_saml(self, options=None):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:
        """
        return self.client.post("""/users/migrate_auth/saml""", options=options)

    def get_saml_metadata(self):
        """Get metadata"""
        return self.client.get("""/saml/metadata""")

    def get_saml_metadata_from_idp(self, options=None):
        """Get metadata from Identity Provider

        saml_metadata_url: The URL from which to retrieve the SAML IDP data.
        """
        return self.client.post("""/saml/metadatafromidp""", options=options)

    def upload_saml_idp_certificate(self, data=None):
        """Upload IDP certificate

        certificate: The IDP certificate file
        """
        return self.client.post("""/saml/certificate/idp""", data=data)

    def delete_saml_idp_certificate(self):
        """Remove IDP certificate"""
        return self.client.delete("""/saml/certificate/idp""")

    def upload_saml_public_certificate(self, data=None):
        """Upload public certificate

        certificate: The public certificate file
        """
        return self.client.post("""/saml/certificate/public""", data=data)

    def delete_saml_public_certificate(self):
        """Remove public certificate"""
        return self.client.delete("""/saml/certificate/public""")

    def upload_saml_private_certificate(self, data=None):
        """Upload private key

        certificate: The private key file
        """
        return self.client.post("""/saml/certificate/private""", data=data)

    def delete_saml_private_certificate(self):
        """Remove private key"""
        return self.client.delete("""/saml/certificate/private""")

    def get_saml_certificate_status(self):
        """Get certificate status"""
        return self.client.get("""/saml/certificate/status""")

    def reset_saml_auth_data_to_email(self, options=None):
        """Reset AuthData to Email

        include_deleted: Whether to include deleted users.
        dry_run: If set to true, the number of users who would be affected is returned.
        user_ids: If set to a non-empty array, then users whose IDs are not in the array will be excluded.
        """
        return self.client.post("""/saml/reset_auth_data""", options=options)
