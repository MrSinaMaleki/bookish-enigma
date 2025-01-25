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


    def create_post_index(self):
        """
        creating post indexes
        """

        index_name = "posts"
        if self.client.indices.exists(index=index_name):
            print(f"Index '{index_name}' already exists. Skipping creation.")
            return

        schema = {
            "mappings": {
                "properties": {
                    "Username": {"type": "text"},
                    "Category": {"type": "keyword"},
                    "text": {"type": "text"},
                    "inserted_at": {"type": "date"}
                }
            }
        }
        self.client.indices.create(index=index_name, body=schema)


