from fastapi import FastAPI, Depends
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError

app = FastAPI()



def get_elasticsearch_client():
    client = Elasticsearch(hosts=['http://localhost:9200'])
    if not client.ping():
        raise ConnectionError("Could not connect to Elasticsearch")
    return client


@app.get("/")
def read_root(es : Elasticsearch = Depends(get_elasticsearch_client)):
    return {"message": "Search service is connected to Elasticsearch!"}

