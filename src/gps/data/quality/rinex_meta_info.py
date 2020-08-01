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
from src.gps.util.util import execute, format_rinex_time


class RinexMetaInfo:
    """
    allows access to the metadata of the rinex file
    """

    def __init__(self, path):
        self.__path = path
        self._file_size = None  # File size in bytes
        self._start_date_time = None  # Start traking data
        self._final_date_time = None  # Finish traking data
        self._sample_rate_interval = None  # Sample rate in seconds
        self._possible_missing_epochs = None  # Number of possible missing epochs
        self._station_name = None  # Station name
        self._antenna_type = None  # Antenna type
        self._antenna_latitude = None  # Default antenna latitude coordinate in degrees
        self._antenna_longitude = None  # Default antenna longitude coordinate in degrees
        self._antenna_elevation = None  # Default antenna elevation in meters
        self._antenna_height = None  # Default antenna height in meters
        self._receiver_type = None  # GPS receiver type

        # get meta info
        self.rinex_meta_info()

    def rinex_meta_info(self):
        command = ["teqc", "+meta", self.__path]
        for line in execute(command):
            if "file size (bytes):" in line:
                self._file_size = line[line.find(':') + 1:].strip()
            elif "start date & time:" in line:
                self._start_date_time = format_rinex_time(line[line.find(':') + 1:].strip())
            elif "final date & time:" in line:
                self._final_date_time = format_rinex_time(line[line.find(':') + 1:].strip())
            elif "sample interval:" in line:
                self._sample_rate_interval = int(float(line[line.find(':') + 1:].strip()))
            elif "possible missing epochs:" in line:
                self._possible_missing_epochs = int(float(line[line.find(':') + 1:].strip()))
            elif "station name:" in line:
                self._station_name = line[line.find(':') + 1:].strip()
            elif "antenna type:" in line:
                self._antenna_type = line[line.find(':') + 1:].strip()
            elif "antenna latitude (deg):" in line:
                self._antenna_latitude = float(line[line.find(':') + 1:].strip())
            elif "antenna longitude (deg):" in line:
                self._antenna_longitude = float(line[line.find(':') + 1:].strip())
            elif "antenna elevation (m):" in line:
                self._antenna_elevation = float(line[line.find(':') + 1:].strip())
            elif "antenna height (m):" in line:
                self._antenna_height = float(line[line.find(':') + 1:].strip())
            elif "receiver type:" in line:
                self._receiver_type = line[line.find(':') + 1:].strip()

    @property
    def file_size(self):
        """
        File size in bytes
        """
        return self._file_size

    @property
    def start_date_time(self):
        return self._start_date_time

    @property
    def final_date_time(self):
        return self._final_date_time

    @property
    def sample_rate_interval(self):
        return self._sample_rate_interval

    @property
    def possible_missing_epochs(self):
        return self._possible_missing_epochs

    @property
    def station_name(self):
        return self._station_name

    @property
    def antenna_type(self):
        """
        GPS Antenna Type
        """
        return self._antenna_type

    @property
    def antenna_latitude(self):
        """
        Antenna latitude in deg
        """
        return self._antenna_latitude

    @property
    def antenna_longitude(self):
        """
        Antenna latitude in deg
        """
        return self._antenna_longitude

    @property
    def antenna_elevation(self):
        """
        Antenna elevation in meters
        """
        return self._antenna_elevation

    @property
    def antenna_height(self):
        """
        Antenna height in meters
        """
        return self._antenna_height

    @property
    def receiver_type(self):
        """
        GPS Receiver type
        """
        return self._receiver_type
