import pika
import json

from src.gps.config.general_config import QUEUE_SERVER, QUEUE_NAME, EXCHANGE_NAME, ROUTING_KEY_NAME

parameters = {'RINEX': '/home/grand/Desktop/TEST/bogt0590.20o',
              'TYPE': 'PPP',
              'EMAIL': 'receiver-email'}

connection = pika.BlockingConnection(pika.ConnectionParameters(QUEUE_SERVER))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)
channel.basic_publish(exchange=EXCHANGE_NAME,
                      routing_key=ROUTING_KEY_NAME,
                      body=json.dumps(parameters))

print("Send processing parameter {}".format(parameters))
connection.close()
