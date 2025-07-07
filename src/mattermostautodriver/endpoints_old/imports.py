from ._base import Base

__all__ = ["Imports"]


class Imports(Base):

    def list_imports(self):
        """List import files
        `Read in Mattermost API docs (imports - ListImports) <https://developers.mattermost.com/api-documentation/#/operations/ListImports>`_

        """
        return self.client.get("""/api/v4/imports""")

    def delete_import(self, import_name):
        """Delete an import file

        import_name: The name of the import file to delete

        `Read in Mattermost API docs (imports - DeleteImport) <https://developers.mattermost.com/api-documentation/#/operations/DeleteImport>`_

        """
        return self.client.delete(f"/api/v4/imports/{import_name}")
