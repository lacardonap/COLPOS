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
from shutil import copy
from pathlib import Path
from netrc import netrc, NetrcParseError


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

    @staticmethod
    def get_credentials(server):
        try:
            _netrc = netrc()  # authentication credentials are obtained from the netrc file
            _username, _account_pass, _pass = _netrc.authenticators(server)
        except FileNotFoundError:
            log.error(".netrc file not exist")
            return None
        except TypeError:
            log.error(".netrc file is empty")
            return None
        except NetrcParseError:
            log.error(".netrc don't have the correct to access, permissions must restrict access to only the owner")
            return None

        return _username, _pass

    @staticmethod
    def copy_and_decompress(proc_dir, gfile):
        output_file = None
        if os.path.isfile(gfile):
            FileUtil.check_dir(proc_dir)
            copy_file = copy(gfile, proc_dir)
            output_file = os.path.splitext(copy_file)[0]
            os.system("gunzip {}".format(copy_file))
        return output_file

    @staticmethod
    def decompress(gfile):
        output_file = None
        if os.path.isfile(gfile):
            output_file = os.path.splitext(gfile)[0]
            os.system("gunzip {}".format(gfile))
        return output_file

    @staticmethod
    def copy_file(src, dst):
        copy_file = None
        if os.path.isfile(src):
            copy_file = copy(src, dst)
        return copy_file

    @staticmethod
    def file_exist_no_empty(path):
        if os.path.exists(path) and os.path.getsize(path) > 0:
            return True
        else:
            log.info("File doesn't exist")
            return False
