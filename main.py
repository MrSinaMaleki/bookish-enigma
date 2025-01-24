import logging
from data_fetcher import APIClient
import dotenv
import os
dotenv.load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename="daemon.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")



if __name__ == '__main__':
    data =  APIClient(url=os.getenv("API_URL")).fetch_data()
    print(data)
