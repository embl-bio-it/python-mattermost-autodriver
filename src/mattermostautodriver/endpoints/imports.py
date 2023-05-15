from .base import Base


class Imports(Base):
    def list_imports(self):
        """List import files
        `Read in Mattermost API docs (imports - ListImports) <https://api.mattermost.com/#tag/imports/operation/ListImports>`_
        """
        return self.client.get("""/api/v4/imports""")
