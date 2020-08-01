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
import tempfile
from src.gps.data.data_manager import DataManager


class GPSTask:
    def __init__(self, task_config):
        self._task_config = task_config
        self._rinex = task_config.rinex
        self._dtu = task_config.get_data_time()
        self._data_manager = DataManager()
        self._tmp_dir = tempfile.mkdtemp()

    def run(self):
        raise NotImplementedError

    def prepare_processing_inputs(self):
        raise NotImplementedError

    @property
    def tmp_dir(self):
        return self._tmp_dir
