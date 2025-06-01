from .base import Base
from typing import Any, BinaryIO


class Bleve(Base):

    def purge_bleve_indexes(self):
        """Purge all Bleve indexes
        `Read in Mattermost API docs (bleve - PurgeBleveIndexes) <https://api.mattermost.com/#tag/bleve/operation/PurgeBleveIndexes>`_

        """
        return self.client.post("""/api/v4/bleve/purge_indexes""")
