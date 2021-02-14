import os
import logging as log
import tempfile
import flask
from flask import request


import urllib.request
from datetime import datetime
from src.gps.task.dgps_task import DGPSTask
from src.gps.task.ppp_task import PPPTask
from src.gps.task.task_config import TaskConfig
from src.gps.data.quality.rinex_qc_info import RinexQCInfo
from src.gps.util.file_util import FileUtil

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1> <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/processing', methods=['GET'])
def processing_rinex():

    log.basicConfig(format='%(levelname)s:%(message)s', level=log.INFO)
    request_config = dict()

    # get processing parameters
    request_config['RINEX'] = request.args['RINEX']
    request_config['TYPE'] = request.args['TYPE']
    request_config['EMAIL'] = request.args['EMAIL']

    # The user sends a url of the rinex file, the file must be downloaded to be processed.
    temp_rinex_path = os.path.join(tempfile.mkdtemp(), 'rinex_file')

    try:
        urllib.request.urlretrieve(request_config['RINEX'], temp_rinex_path)
    except:
        print("an error occurred while trying to download rinex file")
        return

    request_config['RINEX'] = temp_rinex_path
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

    return "Done"


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)