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
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.dates import HourLocator, DateFormatter
from matplotlib.ticker import FuncFormatter

from src.gps.config.general_config import (GPST_KEY, LAT_KEY, LON_KEY, HEIGHT_KEY, SDN_KEY, SDE_KEY, SDU_KEY,
                                           SDNE_KEY, SDEU_KEY, SDUN_KEY, PLOT_KEY)


class GPSDataAnalysis:
    def __init__(self, output_dir):
        self._file = None
        self.df = None
        self.output_file = os.path.join(output_dir, 'llh_data.png')

    def _read_result_file(self):
        data = list()
        with open(self._file) as f:
            for line in f:
                if not line.startswith("%"):
                    line = line.split()

                    str_date = '{} {}'.format(line[0], line[1].split('.')[0])
                    gpst = pd.to_datetime(str_date)

                    lat = pd.to_numeric(line[2])  # Latitude in degrees
                    lon = pd.to_numeric(line[3])  # Longitude in degrees
                    height = pd.to_numeric(line[4])  # height=WGS84 in meters

                    sdn = pd.to_numeric(line[7])  # Standard deviation NORTH in meters
                    sde = pd.to_numeric(line[8])  # Standard deviation EAST in meters 
                    sdu = pd.to_numeric(line[9])  # Standard deviation UP in meters

                    sdne = pd.to_numeric(line[10])  # Standard deviation NORTH-EAST in meters
                    sdeu = pd.to_numeric(line[11])  # Standard deviation EAST-UP in meters
                    sdun = pd.to_numeric(line[12])  # Standard deviation UP-NORTH in meters

                    data.append([gpst, lat, lon, height, sdn, sde, sdu, sdne, sdeu, sdun])

        self.df = pd.DataFrame(data,
                               columns=[GPST_KEY, LAT_KEY, LON_KEY, HEIGHT_KEY, SDN_KEY, SDE_KEY, SDU_KEY, SDNE_KEY, SDEU_KEY, SDUN_KEY])

    def _plot_llh(self):
        fig, axs = plt.subplots(3, 1)
        self.df.set_index('gpst', inplace=True)

        fig.suptitle("Variación LLH", fontsize=24)

        axs[0].plot(self.df[LAT_KEY], linestyle='-', label='Variación de la latitud en grados')
        axs[1].plot(self.df[LON_KEY], linestyle='-', label='Variación de la longitud en grados')
        axs[2].plot(self.df[HEIGHT_KEY], linestyle='-', label='Variación de la altura en metros')

        def format_lat_long(x, pos):
            return '{}°'.format('%.9f' % x)

        def format_height(x, pos):
            return '{} m'.format('%.3f' % x)

        formatter_degrees = FuncFormatter(format_lat_long)
        formatter_height = FuncFormatter(format_height)

        axs[0].yaxis.set_major_formatter(formatter_degrees)
        axs[0].set_xlabel('Tiempo GPS')
        axs[0].set_ylabel('Latitud')
        axs[0].xaxis.set_major_locator(HourLocator())
        axs[0].xaxis.set_major_formatter(DateFormatter("%H:%M"))
        axs[0].legend()
        axs[0].grid(True)

        axs[1].yaxis.set_major_formatter(formatter_degrees)
        axs[1].set_ylabel('Longitud')
        axs[1].xaxis.set_major_locator(HourLocator())
        axs[1].xaxis.set_major_formatter(DateFormatter("%H:%M"))
        axs[1].legend()
        axs[1].grid(True)

        axs[2].yaxis.set_major_formatter(formatter_height)
        axs[2].set_ylabel('Altura')
        axs[2].xaxis.set_major_locator(HourLocator())
        axs[2].xaxis.set_major_formatter(DateFormatter("%H:%M"))
        axs[2].legend()
        axs[2].grid(True)

        fig.autofmt_xdate()

        fig.set_size_inches(16, 14)
        fig.savefig(self.output_file, dpi=100)

    def run(self, result_file):
        self._file = result_file  # Processing file must be read first
        self._read_result_file()
        self._plot_llh()

    def get_results(self):
        return {PLOT_KEY: self.output_file,
                LAT_KEY: self.df[LAT_KEY].mean(),
                LON_KEY: self.df[LON_KEY].mean(),
                HEIGHT_KEY: self.df[HEIGHT_KEY].mean(),
                SDN_KEY: self.df[SDN_KEY].mean(),
                SDE_KEY: self.df[SDE_KEY].mean(),
                SDU_KEY: self.df[SDU_KEY].mean()}
