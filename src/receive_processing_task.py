import logging as log
import pika
import json

from src.gps.config.general_config import QUEUE_SERVER, QUEUE_NAME
from src.gps.task.dgps_task import DGPSTask
from src.gps.task.ppp_task import PPPTask
from src.gps.task.task_config import TaskConfig


def callback(ch, method, properties, body):
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)
    request_config = json.loads(body)  # processing parameters

    task_config = TaskConfig(request_config)
    if request_config['TYPE'] == 'PPP':
        task = PPPTask(task_config)
    elif request_config['TYPE'] == 'DGPS':
        task = DGPSTask(task_config)
    task.run()


connection = pika.BlockingConnection(pika.ConnectionParameters(host=QUEUE_SERVER))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)
channel.basic_consume(queue=QUEUE_NAME,
                      on_message_callback=callback,
                      auto_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
