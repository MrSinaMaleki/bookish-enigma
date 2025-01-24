import requests
import logging

class APIClient:
    def __init__(self, url: str):
        self.url = url

    def fetch_data(self):
        """
        Gets data from API
        """
        if not self.url:
            raise Exception("URL must be set")

        try:
            logging.info("Fetching data from API")
            print("Fetching data from API")
            response = requests.get(self.url)
            logging.info("Fetched data from API")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"error while fetching: {e}")
            logging.fatal(f"error: {e}")
            return None

