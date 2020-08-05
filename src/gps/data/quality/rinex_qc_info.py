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
import logging as log
import os
from datetime import datetime

from src.gps.data.config.config_qc import (LIMIT_MP1,
                                           LIMIT_MP2,
                                           LIMIT_CYCLE_SLIPS,
                                           LIMIT_PERCENTAGE_OF_OBSERVATIONS,
                                           LIMIT_TRAKING_HOURS)
from src.gps.data.data_sources.cddis_data_source import CDDISDataSource
from src.gps.data.quality.rinex_meta_info import RinexMetaInfo
from src.gps.util.data_time_util import DataTimeUtil
from src.gps.util.file_util import FileUtil
from src.gps.util.util import execute, xyz2llh


class RinexQCInfo:
    """
    allows to obtain the quality control of the rinex file
    """
    
    def __init__(self, path):
        self.__path = path  # Rinex File path
        self._obs_rinex = None
        self._nav_rinex = None

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

        # require info for qc
        self._tmp_dir = tempfile.mkdtemp()
        self._rinex_meta = RinexMetaInfo(self.__path)
        self._dtu_rinex = DataTimeUtil(self._rinex_meta.start_date_time)

        self._cddis_ds = CDDISDataSource()
        self._brdc = self._cddis_ds.get_brdc_orbits(self._dtu_rinex)  # Download BRDC Orbits

    def _prepare_inputs(self):
        brdc_uncompress = FileUtil.decompress(self._brdc)  # uncompress brdc
        standard_rinex_name_obs = "{rinex_name}{doy}0.{yy}o".format(rinex_name=self._rinex_meta.station_name,
                                                                    doy=self._dtu_rinex.sdoy(),
                                                                    yy=self._dtu_rinex.yy())

        standard_rinex_name_nav = "{rinex_name}{doy}0.{yy}n".format(rinex_name=self._rinex_meta.station_name,
                                                                    doy=self._dtu_rinex.sdoy(),
                                                                    yy=self._dtu_rinex.yy())

        self._obs_rinex = os.path.join(self._tmp_dir, standard_rinex_name_obs)
        self._nav_rinex = os.path.join(self._tmp_dir, standard_rinex_name_nav)

        # Copy inputs for QC to temporal directory
        FileUtil.copy_file(self.__path, self._obs_rinex)
        FileUtil.copy_file(brdc_uncompress, self._nav_rinex)
        log.info("Inputs were copy to " + self._tmp_dir)

    def run_quality_check(self):
        log.info("Start QC using teqc {}".format(datetime.utcnow()))

        log.info("Star to prepare inputs files")
        self._prepare_inputs()  # Prepare inputs before run QC

        log.info("Start to calculate full QC")
        command = ["teqc", "+qc", self._obs_rinex]
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

    def rinex_is_valid(self):
        """
        Check if rinex file is valid
        :return: bool
        """

        if self._mp1 > LIMIT_MP1:
            return False

        if self._mp2 > LIMIT_MP2:
            return False

        if self._cycle_slips > LIMIT_CYCLE_SLIPS:
            return False

        if self._percent_obs < LIMIT_PERCENTAGE_OF_OBSERVATIONS:
            return False

        if self._traking_hours < LIMIT_TRAKING_HOURS:
            return False

        return True

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
