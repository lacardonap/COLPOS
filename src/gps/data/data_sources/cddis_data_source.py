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

from src.gps.config.enums import EnumDataSourceType
from src.gps.config.general_config import (FTP_DATA_SOURCES,
                                           BRDC_ORBITS_DIR,
                                           IGS_FINAL_ORBITS_DIR)
from src.gps.config.key_names import KeyNames
from src.gps.util.ftp_util import FTPUtil


class CDDISDataSource:
    """
    CDDIS Access to products
    https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/orbit_products.html
    """

    def __init__(self):
        self.__ftp_server = FTP_DATA_SOURCES[EnumDataSourceType.CDDIS][KeyNames.FTP_SERVER]
        self.__ftp_port = FTP_DATA_SOURCES[EnumDataSourceType.CDDIS][KeyNames.FTP_PORT]
        self.__ftp_username = FTP_DATA_SOURCES[EnumDataSourceType.CDDIS][KeyNames.FTP_USERNAME]
        self.__ftp_password = FTP_DATA_SOURCES[EnumDataSourceType.CDDIS][KeyNames.FTP_PASSWORD]
        self.__ftp_product_base_path = FTP_DATA_SOURCES[EnumDataSourceType.CDDIS][KeyNames.FTP_PRODUCT_BASE_PATH]

    def get_brdc_file(self, dtu):
        """
        ftp://cddis.gsfc.nasa.gov/gnss/data/daily/
        YYYY/DDD/YYn/brdcDDD0.YYn.Z   (merged GPS broadcast ephemeris file)
        :param dtu: DateTimeUtil
        :return: path of the brdc downloaded file
        """
        local_dir = os.path.join(BRDC_ORBITS_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join(self.__ftp_product_base_path, 'data', 'daily', dtu.syear(), 'brdc')
        remote_file = "brdc{doy}0.{year}n.Z".format(doy=dtu.sdoy(), year=dtu.yy())
        FTPUtil.ftp_download(self.__ftp_server,
                             self.__ftp_username,
                             self.__ftp_password,
                             remote_dir,
                             remote_file,
                             local_dir)
        return os.path.join(local_dir, remote_file)

    def get_igs_final_gps_orbit(self, dtu):
        """
        ftp://cddis.gsfc.nasa.gov/gnss/products/2034/igs20342.sp3.Z
        {gpsweek}/igs{gpsweek}{gpsweekday}.sp3.Z
        :param dtu: DateTimeUtil
        :return: path of the igs final gps orbit downloaded file
        """
        local_dir = os.path.join(IGS_FINAL_ORBITS_DIR, dtu.syear(), dtu.sdoy())
        remote_dir = os.path.join(self.__ftp_product_base_path, 'products', dtu.sgpsweek())
        remote_file = "igs{gpsweek}{gpsweekday}.sp3.Z".format(gpsweek=dtu.sgpsweek(), gpsweekday=dtu.sgpsweekday())
        FTPUtil.ftp_download(self.__ftp_server,
                             self.__ftp_username,
                             self.__ftp_password,
                             remote_dir,
                             remote_file,
                             local_dir)
        return os.path.join(local_dir, remote_file)
