from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Saml"]


class Saml(Base):

    def migrate_auth_to_saml(self, from_: str, matches: dict[str, Any], auto: bool):
        """Migrate user accounts authentication type to SAML.

        from: The current authentication type for the matched users.
        matches: Users map.
        auto:

        `Read in Mattermost API docs (saml - MigrateAuthToSaml) <https://developers.mattermost.com/api-documentation/#/operations/MigrateAuthToSaml>`_

        """
        __options = {"from": from_, "matches": matches, "auto": auto}
        return self.client.post("""/api/v4/users/migrate_auth/saml""", options=__options)

    def get_saml_metadata(self):
        """Get metadata
        `Read in Mattermost API docs (saml - GetSamlMetadata) <https://developers.mattermost.com/api-documentation/#/operations/GetSamlMetadata>`_

        """
        return self.client.get("""/api/v4/saml/metadata""")

    def get_saml_metadata_from_idp(self, saml_metadata_url: str | None = None):
        """Get metadata from Identity Provider

        saml_metadata_url: The URL from which to retrieve the SAML IDP data.

        `Read in Mattermost API docs (saml - GetSamlMetadataFromIdp) <https://developers.mattermost.com/api-documentation/#/operations/GetSamlMetadataFromIdp>`_

        """
        __options = {"saml_metadata_url": saml_metadata_url}
        return self.client.post("""/api/v4/saml/metadatafromidp""", options=__options)

    def upload_saml_idp_certificate(self, certificate: BinaryIO):
        """Upload IDP certificate

        certificate: The IDP certificate file

        `Read in Mattermost API docs (saml - UploadSamlIdpCertificate) <https://developers.mattermost.com/api-documentation/#/operations/UploadSamlIdpCertificate>`_

        """
        __files = {"certificate": certificate}
        return self.client.post("""/api/v4/saml/certificate/idp""", files=__files)

    def delete_saml_idp_certificate(self):
        """Remove IDP certificate
        `Read in Mattermost API docs (saml - DeleteSamlIdpCertificate) <https://developers.mattermost.com/api-documentation/#/operations/DeleteSamlIdpCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/idp""")

    def upload_saml_public_certificate(self, certificate: BinaryIO):
        """Upload public certificate

        certificate: The public certificate file

        `Read in Mattermost API docs (saml - UploadSamlPublicCertificate) <https://developers.mattermost.com/api-documentation/#/operations/UploadSamlPublicCertificate>`_

        """
        __files = {"certificate": certificate}
        return self.client.post("""/api/v4/saml/certificate/public""", files=__files)

    def delete_saml_public_certificate(self):
        """Remove public certificate
        `Read in Mattermost API docs (saml - DeleteSamlPublicCertificate) <https://developers.mattermost.com/api-documentation/#/operations/DeleteSamlPublicCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/public""")

    def upload_saml_private_certificate(self, certificate: BinaryIO):
        """Upload private key

        certificate: The private key file

        `Read in Mattermost API docs (saml - UploadSamlPrivateCertificate) <https://developers.mattermost.com/api-documentation/#/operations/UploadSamlPrivateCertificate>`_

        """
        __files = {"certificate": certificate}
        return self.client.post("""/api/v4/saml/certificate/private""", files=__files)

    def delete_saml_private_certificate(self):
        """Remove private key
        `Read in Mattermost API docs (saml - DeleteSamlPrivateCertificate) <https://developers.mattermost.com/api-documentation/#/operations/DeleteSamlPrivateCertificate>`_

        """
        return self.client.delete("""/api/v4/saml/certificate/private""")

    def get_saml_certificate_status(self):
        """Get certificate status
        `Read in Mattermost API docs (saml - GetSamlCertificateStatus) <https://developers.mattermost.com/api-documentation/#/operations/GetSamlCertificateStatus>`_

        """
        return self.client.get("""/api/v4/saml/certificate/status""")

    def reset_saml_auth_data_to_email(
        self, include_deleted: bool | None = False, dry_run: bool | None = False, user_ids: list[str] | None = []
    ):
        """Reset AuthData to Email

        include_deleted: Whether to include deleted users.
        dry_run: If set to true, the number of users who would be affected is returned.
        user_ids: If set to a non-empty array, then users whose IDs are not in the array will be excluded.

        `Read in Mattermost API docs (saml - ResetSamlAuthDataToEmail) <https://developers.mattermost.com/api-documentation/#/operations/ResetSamlAuthDataToEmail>`_

        """
        __options = {"include_deleted": include_deleted, "dry_run": dry_run, "user_ids": user_ids}
        return self.client.post("""/api/v4/saml/reset_auth_data""", options=__options)
