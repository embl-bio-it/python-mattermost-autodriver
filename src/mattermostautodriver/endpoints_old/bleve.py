from ._base import Base

__all__ = ["Bleve"]


class Bleve(Base):

    def purge_bleve_indexes(self):
        """Purge all Bleve indexes
        `Read in Mattermost API docs (bleve - PurgeBleveIndexes) <https://developers.mattermost.com/api-documentation/#/operations/PurgeBleveIndexes>`_

        """
        return self.client.post("""/api/v4/bleve/purge_indexes""")
