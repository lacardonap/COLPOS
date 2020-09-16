# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-09-01
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

from src.gps.processing.report.gps_processing_report import GPSProcessingReport
from src.gps.processing.report.gps_data_analysis import GPSDataAnalysis

from src.gps.config.general_config import (LAT_KEY,
                                           LON_KEY,
                                           HEIGHT_KEY,
                                           SDN_KEY,
                                           SDE_KEY,
                                           SDU_KEY,
                                           PLOT_KEY)

from src.gps.util.util import dd2dms_label


class GenerateGPSReport:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.output_report = os.path.join(self.output_dir, 'report.pdf')
        self.data_analysis = GPSDataAnalysis(self.output_dir)
        self.pdf = GPSProcessingReport(orientation='P', unit='mm', format='A4')

    def run(self, result_file, station_name):
        # GPS processing data are analyzed
        self.data_analysis.run(result_file)
        result = self.data_analysis.get_results()

        plot_file = result[PLOT_KEY]

        station = station_name
        lat = dd2dms_label(result[LAT_KEY])
        lon = dd2dms_label(result[LON_KEY])
        height = round(result[HEIGHT_KEY], 3)

        sdn = round(result[SDN_KEY], 3)
        sde = round(result[SDE_KEY], 3)
        sdu = round(result[SDU_KEY], 3)

        self.pdf.add_page()
        self.pdf.intro()
        self.pdf.add_coordinates_result(station, lat, lon, height, sdn, sde, sdu)
        self.pdf.add_computation_standards()
        self.pdf.image_processing(plot_file)

        self.pdf.output(self.output_report, 'F')
