import pika
import json

from src.gps.config.general_config import QUEUE_SERVER, QUEUE_NAME, EXCHANGE_NAME, ROUTING_KEY_NAME

parameters = {'RINEX': 'https://nowsoft.app/bienes-raices/descargar/dc279cf0-194a-11eb-808c-47c506d8ff8e',
              'TYPE': 'PPP',
              'EMAIL': 'ivancho4321@gmail.com'}

connection = pika.BlockingConnection(pika.ConnectionParameters(QUEUE_SERVER))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)
channel.basic_publish(exchange=EXCHANGE_NAME,
                      routing_key=ROUTING_KEY_NAME,
                      body=json.dumps(parameters))

print("Send processing parameter {}".format(parameters))
connection.close()
