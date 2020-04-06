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
from datetime import date
from gnsscal import date2gpswd


class DataTimeUtil:
    def __init__(self, dt):
        self.__dt = dt
        self._year = self.__dt.year
        self._month = self.__dt.month
        self._day = self.__dt.day
        self._doy = dt.timetuple().tm_yday

        gpswd = date2gpswd(date(self._year, self._month, self._day))
        self._gpsweek = gpswd[0]
        self._gpsweekday = gpswd[1]

    @property
    def year(self):
        """
        Year
        :return: int (e.g 2020/09/15 --> 2020)
        """
        return self._year

    def syear(self):
        """
        Year in string
        :return: str (e.g 2020/09/15 --> 2020)
        """
        return str(self._year)

    @property
    def month(self):
        """
        Month
        :return: int (e.g 2020/09/15 --> 9)
        """
        return self._month

    @property
    def day(self):
        """
        Day
        :return: int (e.g 2020/09/15 --> 15)
        """
        return self._day

    @property
    def doy(self):
        """
        Day of year
        :return: str (e.g: 2020/09/15 --> 259)
        """
        return self._doy

    def sdoy(self):
        """
        Day of the year in string format
        :return: str (e.g 2020/01/01 --> 001)
        """
        return "%03d" % self._doy

    @property
    def gpsweek(self):
        """
        Return GPS Week
        :return: int (e.g: 2020/09/15 --> 2123)
        """
        return self._gpsweek

    def sgpsweek(self):
        """
        Return GPS Week in string format
        :return: int (e.g: 2020/09/15 --> 2123)
        """
        return "%04d" % self._gpsweek

    @property
    def gpsweekday(self):
        """
        Return GPS Week day
        :return: int (e.g: 2020/09/15 --> 2)
        """
        return self._gpsweekday

    def sgpsweekday(self):
        """
        Return GPS Week day in string format
        :return: int (e.g: 2020/09/15 --> 2)
        """
        return str(self._gpsweekday)

    def yy(self):
        """
        the year in last two-digit format.
        :return: int (e.g 2020/09/15 --> 20)
        """
        return self.__dt.strftime('%y')
