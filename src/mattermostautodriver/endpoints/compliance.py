from .base import Base
from typing import Any


class Compliance(Base):

    def create_compliance_report(self):
        """Create report
        `Read in Mattermost API docs (compliance - CreateComplianceReport) <https://api.mattermost.com/#tag/compliance/operation/CreateComplianceReport>`_

        """
        return self.client.post("""/api/v4/compliance/reports""")

    def get_compliance_reports(self, page: int | None = 0, per_page: int | None = 60):
        """Get reports

        page: The page to select.
        per_page: The number of reports per page.

        `Read in Mattermost API docs (compliance - GetComplianceReports) <https://api.mattermost.com/#tag/compliance/operation/GetComplianceReports>`_

        """
        params_71f8b7431cd64fcfa0dabd300d0636d2 = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/compliance/reports""", params=params_71f8b7431cd64fcfa0dabd300d0636d2)

    def get_compliance_report(self, report_id: str):
        """Get a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - GetComplianceReport) <https://api.mattermost.com/#tag/compliance/operation/GetComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}")

    def download_compliance_report(self, report_id: str):
        """Download a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - DownloadComplianceReport) <https://api.mattermost.com/#tag/compliance/operation/DownloadComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}/download")
