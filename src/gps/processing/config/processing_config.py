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

import os
from src.gps.config.general_config import (RTKLIB_PPP_CONFIG_FILE,
                                           IGS_14_ATX_FILE)


class ProcessingConfig:

    def __init__(self, config):
        self._dtu = config[0]
        self._temp_dir = config[1]
        self._brdc = config[2]
        self._orbit = config[3]
        self._clock = config[4]
        self._erp = config[5]
        self._eph = config[6]

        # Config files
        self._igs_atx_file = IGS_14_ATX_FILE
        self._rtklib_ppp_config = RTKLIB_PPP_CONFIG_FILE
        self._procs_options = list()

        # Output file
        self._output_file = os.path.join(self._temp_dir, 'processing_result.txt')

    def get_processing_options(self):
        raise NotImplementedError

    @property
    def temp_dir(self):
        return self._temp_dir
