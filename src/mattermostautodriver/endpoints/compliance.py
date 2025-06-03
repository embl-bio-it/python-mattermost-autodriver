from ._base import Base
from typing import Any, BinaryIO

__all__ = ["Compliance"]


class Compliance(Base):

    def create_compliance_report(self):
        """Create report
        `Read in Mattermost API docs (compliance - CreateComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/CreateComplianceReport>`_

        """
        return self.client.post("""/api/v4/compliance/reports""")

    def get_compliance_reports(self, page: int | None = 0, per_page: int | None = 60):
        """Get reports

        page: The page to select.
        per_page: The number of reports per page.

        `Read in Mattermost API docs (compliance - GetComplianceReports) <https://developers.mattermost.com/api-documentation/#/operations/GetComplianceReports>`_

        """
        __params = {"page": page, "per_page": per_page}
        return self.client.get("""/api/v4/compliance/reports""", params=__params)

    def get_compliance_report(self, report_id: str):
        """Get a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - GetComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/GetComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}")

    def download_compliance_report(self, report_id: str):
        """Download a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - DownloadComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/DownloadComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}/download")
