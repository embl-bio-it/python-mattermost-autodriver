from .base import Base


class Exports(Base):
    def list_exports(self):
        """List export files"""
        return self.client.get("""/exports""")

    def download_export(self, export_name):
        """Download an export file

        export_name: The name of the export file to download
        """
        return self.client.get(f"/exports/{export_name}")

    def delete_export(self, export_name):
        """Delete an export file

        export_name: The name of the export file to delete
        """
        return self.client.delete(f"/exports/{export_name}")
