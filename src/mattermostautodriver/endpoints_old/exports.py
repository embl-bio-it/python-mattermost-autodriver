from ._base import Base

__all__ = ["Exports"]


class Exports(Base):

    def list_exports(self):
        """List export files
        `Read in Mattermost API docs (exports - ListExports) <https://api.mattermost.com/#tag/exports/operation/ListExports>`_

        """
        return self.client.get("""/api/v4/exports""")

    def download_export(self, export_name):
        """Download an export file

        export_name: The name of the export file to download

        `Read in Mattermost API docs (exports - DownloadExport) <https://api.mattermost.com/#tag/exports/operation/DownloadExport>`_

        """
        return self.client.get(f"/api/v4/exports/{export_name}")

    def delete_export(self, export_name):
        """Delete an export file

        export_name: The name of the export file to delete

        `Read in Mattermost API docs (exports - DeleteExport) <https://api.mattermost.com/#tag/exports/operation/DeleteExport>`_

        """
        return self.client.delete(f"/api/v4/exports/{export_name}")
