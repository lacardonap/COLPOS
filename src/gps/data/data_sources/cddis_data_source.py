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
import os

from src.gps.config.general_config import (FTP_SERVER_CDDIS,
                                           HTTPS_SERVER_CDDIS,
                                           BRDC_ORBITS_DIR,
                                           IGS_ERP_DIR,
                                           IGS_EPH_DIR,
                                           IGS_30_SEC_CLOCK_DIR,
                                           IGS_FINAL_ORBITS_DIR)
from src.gps.util.ftp_util import FTPUtil
from src.gps.util.http_util import HTTPUtil


class CDDISDataSource:
    """
    CDDIS Access to products
    https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/orbit_products.html
    """

    def __init__(self):
        self.__ftp_server = FTP_SERVER_CDDIS
        self.__https_server = HTTPS_SERVER_CDDIS

    def get_brdc_orbits(self, dtu):
        """
        BRDC Orbits
        ftp://cddis.gsfc.nasa.gov/gnss/data/daily/
        YYYY/DDD/YYn/brdcDDD0.YYn.Z   (merged GPS broadcast ephemeris file)
        :param dtu: DateTimeUtil
        :return: path of the brdc downloaded file
        """
        local_dir = os.path.join(BRDC_ORBITS_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join('gnss', 'data', 'daily', dtu.syear(), 'brdc')
        remote_file = "brdc{doy}0.{year}n.Z".format(doy=dtu.sdoy(), year=dtu.yy())
        FTPUtil.ftp_download(self.__ftp_server, remote_dir, remote_file, local_dir)
        return os.path.join(local_dir, remote_file)

    def get_igs_final_gps_orbit(self, dtu):
        """
        IGS Final GPS orbits
        ftp://cddis.gsfc.nasa.gov/gnss/products/2034/igs20342.sp3.Z
        {gpsweek}/igs{gpsweek}{gpsweekday}.sp3.Z
        :param dtu: DateTimeUtil
        :return: path of the igs final gps orbit downloaded file
        """
        local_dir = os.path.join(IGS_FINAL_ORBITS_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join('gnss', 'products', dtu.sgpsweek())
        remote_file = "igs{gpsweek}{gpsweekday}.sp3.Z".format(gpsweek=dtu.sgpsweek(), gpsweekday=dtu.sgpsweekday())
        FTPUtil.ftp_download(self.__ftp_server, remote_dir, remote_file, local_dir)
        return os.path.join(local_dir, remote_file)

    def get_igs_30_sec_clock(self, dtu):
        """
        IGS Clock file 30 seconds
        https://cddis.nasa.gov/archive/gnss/products/2086/igs20864.clk_30s.Z
        {gpsweek}/igs{gpsweek}{gpsweekday}.clk_30s.Z
        :return: path of the igs 30 seconds clock downloaded file
        """
        local_dir = os.path.join(IGS_30_SEC_CLOCK_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join('archive', 'gnss', 'products', dtu.sgpsweek())
        remote_file = "igs{gpsweek}{gpsweekday}.clk_30s.Z".format(gpsweek=dtu.sgpsweek(), gpsweekday=dtu.sgpsweekday())
        HTTPUtil.http_download_cddis_ssl(self.__https_server, remote_dir, remote_file, local_dir)
        return os.path.join(local_dir, remote_file)

    def get_earth_orientation_parameters(self, dtu):
        """
        IGS Earth Orietation parameters
        https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/orbit_products.html
        https://cddis.nasa.gov/archive/gnss/products/2086/igs20867.erp.Z
        {gpsweek}/igs{gpsweek}{gpsweekday}.erp.Z
        {gpsweekday} = day of week (0-6, 7 indicates weekly)
        :return: path of the earth orientation parameters downloaded file
        """
        local_dir = os.path.join(IGS_ERP_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join('archive', 'gnss', 'products', dtu.sgpsweek())
        remote_file = "igs{gpsweek}7.erp.Z".format(gpsweek=dtu.sgpsweek())
        HTTPUtil.http_download_cddis_ssl(self.__https_server, remote_dir, remote_file, local_dir)
        return os.path.join(local_dir, remote_file)

    def get_satellite_orbit_solution(self, dtu):
        """
        IGS Earth Orietation parameters
        https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/orbit_products.html
        https://cddis.nasa.gov/archive/gnss/products/2086/cod20861.eph.Z
        {gpsweek}/cod{gpsweek}{gpsweekday}.eph.Z
        {gpsweekday} = day of week (0-6, 7 indicates weekly)
        :return: path of the earth orientation parameters downloaded file
        """
        local_dir = os.path.join(IGS_EPH_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join('archive', 'gnss', 'products', dtu.sgpsweek())
        remote_file = "cod{gpsweek}{gpsweekday}.eph.Z".format(gpsweek=dtu.sgpsweek(), gpsweekday=dtu.sgpsweekday())
        HTTPUtil.http_download_cddis_ssl(self.__https_server, remote_dir, remote_file, local_dir)
        return os.path.join(local_dir, remote_file)
