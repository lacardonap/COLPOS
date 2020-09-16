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

from src.gps.util.data_time_util import DataTimeUtil
from src.gps.data.quality.rinex_meta_info import RinexMetaInfo


class TaskConfig:

    def __init__(self, config):
        self._rinex = config['RINEX']
        self._processing_type = config['TYPE']
        self._receiver_email = config['EMAIL']
        self._rinex_meta = RinexMetaInfo(self._rinex)

    @property
    def rinex(self):
        return self._rinex

    def get_data_time(self):
        dt = self._rinex_meta.start_date_time
        dtu = DataTimeUtil(dt)
        return dtu

    @property
    def rinex_meta(self):
        return self._rinex_meta

    @property
    def receiver_email(self):
        return self._receiver_email
