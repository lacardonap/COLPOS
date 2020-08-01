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
from src.gps.processing.config.processing_config import ProcessingConfig


class PPPConfig(ProcessingConfig):
    def __init__(self, config):
        ProcessingConfig.__init__(self, config)

    def get_processing_options(self):
        self._procs_options.append("-k {}".format(self._rtklib_ppp_config))
        # " -p 7",               # mode 7:ppp-static
        # " -t", # lat/lon/height time output
        # " -u", # UTC time Don't use it, we get epochs of min:11 and min:41 instead of min:00 and min:00
        # " -d %d" % 12, # number of decimals in time output
        self._procs_options.append("-o {}".format(self._output_file))
        self._procs_options.append("-m {}".format(5))  # elevation mask
        # " -m 10",                       # elevation mask
        # " -c", # combined forward/backward solutions
        # " -y 1", # state output
        # " -h", # fix and hold for integer ambiguity resolution [off]
        # " -f 2", # 2:L1+L2
        # " -x 2", # debug level
        self._procs_options.append(self._eph)
        self._procs_options.append(self._clock)
        self._procs_options.append(self._brdc)
        self._procs_options.append(self._igs_atx_file)

        return self._procs_options
