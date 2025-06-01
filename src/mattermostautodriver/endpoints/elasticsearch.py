from .base import Base
from typing import Any


class Elasticsearch(Base):

    def test_elasticsearch(self):
        """Test Elasticsearch configuration
        `Read in Mattermost API docs (elasticsearch - TestElasticsearch) <https://api.mattermost.com/#tag/elasticsearch/operation/TestElasticsearch>`_

        """
        return self.client.post("""/api/v4/elasticsearch/test""")

    def purge_elasticsearch_indexes(self):
        """Purge all Elasticsearch indexes
        `Read in Mattermost API docs (elasticsearch - PurgeElasticsearchIndexes) <https://api.mattermost.com/#tag/elasticsearch/operation/PurgeElasticsearchIndexes>`_

        """
        return self.client.post("""/api/v4/elasticsearch/purge_indexes""")
