from ._base import Base

__all__ = ["Compliance"]


class Compliance(Base):

    def create_compliance_report(self):
        """Create report
        `Read in Mattermost API docs (compliance - CreateComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/CreateComplianceReport>`_

        """
        return self.client.post("""/api/v4/compliance/reports""")

    def get_compliance_reports(self, params=None):
        """Get reports

        page: The page to select.
        per_page: The number of reports per page.

        `Read in Mattermost API docs (compliance - GetComplianceReports) <https://developers.mattermost.com/api-documentation/#/operations/GetComplianceReports>`_

        """
        return self.client.get("""/api/v4/compliance/reports""", params=params)

    def get_compliance_report(self, report_id):
        """Get a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - GetComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/GetComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}")

    def download_compliance_report(self, report_id):
        """Download a report

        report_id: Compliance report GUID

        `Read in Mattermost API docs (compliance - DownloadComplianceReport) <https://developers.mattermost.com/api-documentation/#/operations/DownloadComplianceReport>`_

        """
        return self.client.get(f"/api/v4/compliance/reports/{report_id}/download")
