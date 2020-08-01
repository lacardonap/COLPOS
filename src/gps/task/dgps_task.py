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

from src.gps.util.file_util import FileUtil
from src.gps.processing.config.dgps_config import DGPSConfig
from src.gps.processing.processing_manager import ProcessingManager
from src.gps.task.gps_task import GPSTask


class DGPSTask(GPSTask):

    def __init__(self, task_config):
        GPSTask.__init__(self, task_config)

    def run(self):
        # Get inputs needed for processing
        self._data_manager.get_inputs(self._dtu)

        # Copy data to processing dir
        inputs = self.prepare_processing_inputs()
        procs_config = DGPSConfig(inputs)
        ProcessingManager.run_ppp(procs_config)

        log.info("Done: Data was copy to {}".format(self._tmp_dir))

    def prepare_processing_inputs(self):
        """
        Return uncompress input files
        :return: input parameters [dtu, tmp_dir, brdc, orbit, clock, erp, eph, rinex]
        """
        inputs = list()
        inputs.append(self._dtu)
        inputs.append(self._tmp_dir)

        # Copy inputs parameter to processing dir
        for parameter in self._data_manager.get_inputs_parameters():
            path = FileUtil.copy_and_decompress(self._tmp_dir, parameter)  # unzipping path file
            inputs.append(path)

        # Copy rinex to processing dir
        rinex = dict()
        for rinex_name, rinex_path in self._data_manager.rinexs.items():
            path = FileUtil.copy_and_decompress(self._tmp_dir, rinex_path)  # unzipping path file
            rinex[rinex_name] = path
        inputs.append(rinex)

        return inputs
