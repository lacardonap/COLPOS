import logging as log
import pika
import json


from datetime import datetime
from src.gps.config.general_config import QUEUE_SERVER, QUEUE_NAME
from src.gps.task.dgps_task import DGPSTask
from src.gps.task.ppp_task import PPPTask
from src.gps.task.task_config import TaskConfig
from src.gps.data.quality.rinex_qc_info import RinexQCInfo
from src.gps.util.file_util import FileUtil


def callback(ch, method, properties, body):
    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)
    request_config = json.loads(body)  # processing parameters

    if not FileUtil.file_exist_no_empty(request_config['RINEX']):
        log.error("Finish processing because RINEX file doesn't exist or is empty {}".format(datetime.utcnow()))
        return

    task_config = TaskConfig(request_config)
    qc = RinexQCInfo(task_config.rinex)
    qc.run_quality_check()

    log.info("Check if RINEX is valid")

    if not qc.rinex_is_valid():
        log.error("Finish processing because RINEX file don't pass the quality check {}".format(datetime.utcnow()))
        return
    else:
        log.info("RINEX file passed quality check")

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
