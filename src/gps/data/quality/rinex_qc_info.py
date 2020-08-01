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
from src.gps.util.util import execute, xyz2llh


class RinexQCInfo:
    """
    allows to obtain the quality control of the rinex file
    """
    
    def __init__(self, path):
        self.__path = path  # Rinex File path
        self._x = None  # ECEF X antenna coordinate in meters
        self._y = None  # ECEF Y antenna coordinate in meters
        self._z = None  # ECEF Z antenna coordinate in meters

        self._latitude = None  # WGS 84 latitude coordinate in degrees
        self._longitude = None  # WGS 84 longitude coordinate in degrees
        self._height = None  # WGS 84 height coordinate in degrees

        self._traking_hours = None  # Rate time in hours
        self._sample_rate = None  # Rate sample time in seconds
        self._expt_obs = None  # Expected number of observations
        self._real_obs = None  # Real number of observations
        self._percent_obs = None  # Percent of observations
        self._mp1 = None  # Multipath 1 in meters
        self._mp2 = None  # Multipath 2 in meters
        self._cycle_slips = None  # Number of cycle slips

        # get qc info
        self.rinex_qc_info()

    def rinex_qc_info(self):
        command = ["teqc", "+qc", self.__path]
        for line in execute(command):
            if "antenna WGS 84 (xyz)  :" in line:

                xyz_coordinates = line[line.find(':') + 1:].strip().split()
                self._x = float(xyz_coordinates[0])
                self._y = float(xyz_coordinates[1])
                self._z = float(xyz_coordinates[2])

                llh_coordinates = xyz2llh(self._x, self._y, self._z)

                self._latitude = llh_coordinates['lon']
                self._longitude = llh_coordinates['lat']
                self._height = llh_coordinates['height']

            elif line.startswith('SUM '):
                tokens_qc = line.split()
                self._traking_hours = float(tokens_qc[9])
                self._sample_rate = int(tokens_qc[10])
                self._expt_obs = int(tokens_qc[11])
                self._real_obs = int(tokens_qc[12])
                self._percent_obs = float(tokens_qc[13])
                self._mp1 = float(tokens_qc[14])
                self._mp2 = float(tokens_qc[15])
                self._cycle_slips = int(tokens_qc[16])

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def height(self):
        return self._height

    @property
    def traking_hours(self):
        return self._traking_hours

    @property
    def sample_rate(self):
        return self._sample_rate

    @property
    def expected_obsevations(self):
        return self._expt_obs

    @property
    def real_observations(self):
        return self._real_obs

    @property
    def percent_obs(self):
        return self._percent_obs

    @property
    def mp1(self):
        return self._mp1

    @property
    def mp2(self):
        return self._mp2

    @property
    def cycle_slips(self):
        return self._cycle_slips
