from .base import Base


class Elasticsearch(Base):
    def test_elasticsearch(self):
        """Test Elasticsearch configuration"""
        return self.client.post("""/elasticsearch/test""")

    def purge_elasticsearch_indexes(self):
        """Purge all Elasticsearch indexes"""
        return self.client.post("""/elasticsearch/purge_indexes""")
