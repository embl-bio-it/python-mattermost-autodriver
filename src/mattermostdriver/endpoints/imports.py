from .base import Base


class Imports(Base):
    def list_imports(self):
        """List import files"""
        return self.client.get("""/imports""")
