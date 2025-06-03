from ._base import Base

__all__ = ["Imports"]


class Imports(Base):

    def list_imports(self):
        """List import files
        `Read in Mattermost API docs (imports - ListImports) <https://developers.mattermost.com/api-documentation/#/operations/ListImports>`_

        """
        return self.client.get("""/api/v4/imports""")
