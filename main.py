import logging
from data_fetcher import APIClient
from kafka_client import KafkaProducerClient
from elastic_client import ElasticClient
import dotenv
import os
dotenv.load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename="daemon.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")



if __name__ == '__main__':
    data =  APIClient(url=os.getenv("API_URL")).fetch_data()

    # for data in data['data']:
    #     me_broker = KafkaProducerClient(topic=data, bootstrap_servers=os.getenv("KAFKA_SERVERS"))

    el_client = ElasticClient()
    el_client.create_post_index()
    print("Index created successfully!")

