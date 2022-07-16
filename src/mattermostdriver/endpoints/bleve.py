from .base import Base


class Bleve(Base):
    def purge_bleve_indexes(self):
        """Purge all Bleve indexes"""
        return self.client.post("""/bleve/purge_indexes""")
