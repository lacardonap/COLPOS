# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-08-01
        git sha              : :%H$
        copyright            : (C) 2020 by Leo Cardona
        email                : leo.cardona.p@gmail.com
 ***************************************************************************/
/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License v3.0 as          *
 *   published by the Free Software Foundation.                            *
 *                                                                         *
 ***************************************************************************/
"""
import logging as log
from datetime import datetime
import subprocess

from src.gps.config.general_config import RTKLIB_BINARY


class ProcessingManager:

    @staticmethod
    def run_ppp(rinex, config):
        """
        Processing GPS data using RTKLib rnx2rtkp
        :param config: Processing config file
        :return:
        """
        log.info("PPP run using RTKLib rnx2rtkp start at {}".format(datetime.utcnow()))

        # Processing parameters
        command = RTKLIB_BINARY
        for opt in config.get_processing_options():
            command += " {}".format(opt)

        # Add rinex to processing
        command += " {}".format(rinex)
        log.info(command)

        p = subprocess.Popen(command, shell=True, cwd=config.temp_dir)
        p.communicate()  # wait for processing to finish

        log.info("Processing finish")
