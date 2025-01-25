import time
from elastic_client import ElasticClient
from data_fetcher import APIClient
import os
import dotenv

dotenv.load_dotenv()

# Initialize clients
elastic_client = ElasticClient()
api_client = APIClient(url=os.getenv("API_URL"))


def fetch_and_store():
    """
    Fetch data from API and store it in Elasticsearch.
    """
    data = api_client.fetch_data()
    if data:
        for item in data['data']:
            document = {
                "Username": item.get("username", "unknown"),
                "Category": item.get("category", "uncategorized"),
                "text": item.get("text", ""),
                "inserted_at": item.get("inserted_at", time.strftime("%Y-%m-%dT%H:%M:%SZ")),
            }
            elastic_client.insert_data(index_name="posts", data=document)

    else:
        print("No data found.")
    print("Data fetch and store completed.")


if __name__ == '__main__':

    # for data in data['data']:
    #     me_broker = KafkaProducerClient(topic=data, bootstrap_servers=os.getenv("KAFKA_SERVERS"))

    print("Starting the scheduled task...")
    while True:
        fetch_and_store()
        time.sleep(60)
