# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-04-06
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
import logging as log
from pathlib import Path


class FileUtil:
    @staticmethod
    def check_dir(target_dir):
        """
        check that local target directory exists, create it if not
        :param target_dir: local target dir (str)
        """
        if not os.path.isdir(target_dir):
            Path(target_dir).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def delete_files(path_dir):
        """
        delete all files in given local folder
        :param path_dir: targ
        """
        for the_file in os.listdir(path_dir):
            file_path = os.path.join(path_dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                log.error(e)
