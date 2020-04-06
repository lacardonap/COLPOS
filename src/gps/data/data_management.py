# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-03-30
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
from src.gps.data.data_sources.cddis_data_source import CDDISDataSource


class DataManagement:
    def __init__(self):
        self.cddis_ds = CDDISDataSource()

    def retrieve_brdc_file(self, dtu):
        return self.cddis_ds.get_brdc_file(dtu)

    def retrieve_igs_final_gps_orbit(self, dtu):
        return self.cddis_ds.get_igs_final_gps_orbit(dtu)
