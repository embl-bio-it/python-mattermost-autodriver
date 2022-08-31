from .base import Base


class Bleve(Base):
    def purge_bleve_indexes(self):
        """Purge all Bleve indexes
        `Read in Mattermost API docs (bleve - PurgeBleveIndexes) <https://api.mattermost.com/#tag/bleve/operation/PurgeBleveIndexes>`_
        """
        return self.client.post("""/bleve/purge_indexes""")
