from ._base import Base

__all__ = ["Elasticsearch"]


class Elasticsearch(Base):

    def test_elasticsearch(self):
        """Test Elasticsearch configuration
        `Read in Mattermost API docs (elasticsearch - TestElasticsearch) <https://developers.mattermost.com/api-documentation/#/operations/TestElasticsearch>`_

        """
        return self.client.post("""/api/v4/elasticsearch/test""")

    def purge_elasticsearch_indexes(self):
        """Purge all Elasticsearch indexes
        `Read in Mattermost API docs (elasticsearch - PurgeElasticsearchIndexes) <https://developers.mattermost.com/api-documentation/#/operations/PurgeElasticsearchIndexes>`_

        """
        return self.client.post("""/api/v4/elasticsearch/purge_indexes""")
