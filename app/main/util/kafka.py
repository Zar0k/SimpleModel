import logging
import json

from kafka import KafkaProducer, KafkaConsumer, TopicPartition

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOPIC = 'model'


class Producer:

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka:29092',
                                      api_version=(0,10), value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def send(self, topic, msg):
        try:
            self.producer.send(topic, msg)
            self.producer.flush()
        except Exception as e:
            print("type error: " + str(e))


class Consumer:

    def __init__(self):
        self.consumer = KafkaConsumer(TOPIC, auto_offset_reset='earliest',
                             bootstrap_servers=['kafka:29092'], api_version=(0, 10), consumer_timeout_ms=1000)

    def consume(self):
        try:
             for msg in self.consumer:
                return json.loads(msg.value)
        except Exception as e:
            print("type error: " + str(e))
