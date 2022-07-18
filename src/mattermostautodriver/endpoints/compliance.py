from .base import Base


class Compliance(Base):
    def create_compliance_report(self):
        """Create report"""
        return self.client.post("""/compliance/reports""")

    def get_compliance_reports(self, params=None):
        """Get reports

        page: The page to select.
        per_page: The number of reports per page.
        """
        return self.client.get("""/compliance/reports""", params=params)

    def get_compliance_report(self, report_id):
        """Get a report

        report_id: Compliance report GUID
        """
        return self.client.get(f"/compliance/reports/{report_id}")

    def download_compliance_report(self, report_id):
        """Download a report

        report_id: Compliance report GUID
        """
        return self.client.get(f"/compliance/reports/{report_id}/download")
