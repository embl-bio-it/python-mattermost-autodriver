from .base import Base
from typing import Any, BinaryIO


class AuditLogs(Base):

    def add_audit_log_certificate(self, certificate: BinaryIO):
        """Upload audit log certificate

        certificate: The certificate file

        `Read in Mattermost API docs (audit_logs - AddAuditLogCertificate) <https://api.mattermost.com/#tag/audit_logs/operation/AddAuditLogCertificate>`_

        """
        files_71f8b7431cd64fcfa0dabd300d0636d2 = {"certificate": certificate}
        return self.client.post("""/api/v4/audit_logs/certificate""", files=files_71f8b7431cd64fcfa0dabd300d0636d2)

    def remove_audit_log_certificate(self):
        """Remove audit log certificate
        `Read in Mattermost API docs (audit_logs - RemoveAuditLogCertificate) <https://api.mattermost.com/#tag/audit_logs/operation/RemoveAuditLogCertificate>`_

        """
        return self.client.delete("""/api/v4/audit_logs/certificate""")
