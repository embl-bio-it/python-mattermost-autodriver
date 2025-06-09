from ._base import Base

__all__ = ["AuditLogs"]


class AuditLogs(Base):

    def add_audit_log_certificate(self, files, data=None):
        """Upload audit log certificate

        certificate: The certificate file

        `Read in Mattermost API docs (audit_logs - AddAuditLogCertificate) <https://developers.mattermost.com/api-documentation/#/operations/AddAuditLogCertificate>`_

        """
        return self.client.post("""/api/v4/audit_logs/certificate""", files=files, data=data)

    def remove_audit_log_certificate(self):
        """Remove audit log certificate
        `Read in Mattermost API docs (audit_logs - RemoveAuditLogCertificate) <https://developers.mattermost.com/api-documentation/#/operations/RemoveAuditLogCertificate>`_

        """
        return self.client.delete("""/api/v4/audit_logs/certificate""")
