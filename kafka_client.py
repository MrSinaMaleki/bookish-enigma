import json
from kafka import KafkaProducer
import logging

class KafkaProducerClient:
    def __init__(self, topic, bootstrap_servers):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_message(self, message:{}):
        """
        Gets and sends a message to the topic
        """
        try:
            print("message: ",message)
            self.producer.send(self.topic, message)
            self.producer.flush()

            logging.info("Message sent")
            print("Message sent to kafka")
        except Exception as e:
            print(f"error while sending the message to the topic --> {e}")
            logging.critical(f"error while sending the message to the topic --> {e}")

