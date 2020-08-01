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


class DataManager:
    def __init__(self):
        self._cddis_ds = CDDISDataSource()
        self._dtu = None
        self._brdc = None
        self._orbit = None
        self._clock = None
        self._erp = None
        self._eph = None
        self._stations = list()
        self._rinexs = dict()

    def get_inputs(self, dtu):
        self._dtu = dtu
        self._brdc = self._cddis_ds.get_brdc_orbits(self._dtu)  # Download BRDC Orbits
        self._orbit = self._cddis_ds.get_igs_final_gps_orbit(self._dtu)  # Download IGS final orbit sp3 format
        self._clock = self._cddis_ds.get_igs_30_sec_clock(self._dtu)  # Download IGS 30 sec clock products
        self._erp = self._cddis_ds.get_earth_orientation_parameters(self._dtu)  # Download Earth Rotation Parameters
        self._eph = self._cddis_ds.get_satellite_orbit_solution(self._dtu)  # Download Satellite Orbit solution

    def get_inputs_parameters(self):
        return [self._brdc, self._orbit, self._clock, self._erp, self._eph]

    def get_rinexs(self, stations):
        self._stations = stations
        for station in self._stations:
            self._rinexs[station] = self._cddis_ds.get_rinex_file(self._dtu, station)

    @property
    def orbit(self):
        return self._orbit

    @property
    def clock(self):
        return self._clock

    @property
    def erp(self):
        return self._erp

    @property
    def eph(self):
        return self._eph

    @property
    def stations(self):
        return self._stations

    @property
    def rinexs(self):
        return self._rinexs

    @property
    def brdc(self):
        return self._brdc
