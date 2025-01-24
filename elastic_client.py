from elasticsearch import Elasticsearch

class ElasticClient:
    def __init__(self, host='http://localhost:9200'):
        self.client = Elasticsearch(host)

    def create_index(self, index_name, schema):
        """
        index creation
        """

        if self.client.indices.exists(index_name):
            print("Index already exists")
        else:
            self.client.indices.create(index_name, schema)
            print(f"Index ({index_name}) created")

