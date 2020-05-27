import logging as log
from datetime import datetime

from src.gps.config.general_config import PPP_PROCESSING_DIR
from src.gps.util.file_util import FileUtil



class ProcessingManager:

    def __init__(self, inputs):
        self._inputs = inputs


    def run_ppp(self, data_management):
        """
        Processing GPS data using RTKLib rnx2rtkp
        :return:
        """

        log.info("PPP run using RTKLib rnx2rtkp start at {}".format(datetime.utcnow()))
        FileUtil.check_dir(PPP_PROCESSING_DIR)  # check that target dir exists, if not create it


