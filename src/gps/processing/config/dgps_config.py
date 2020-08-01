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
from src.gps.processing.config.processing_config import ProcessingConfig


class DGPSConfig(ProcessingConfig):
    def __init__(self, config):
        ProcessingConfig.__init__(self, config)
        self._station_name = list(config[7].keys())

    def get_processing_options(self):
        raise NotImplementedError
