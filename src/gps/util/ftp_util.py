# -*- coding: utf-8 -*-
"""
/***************************************************************************
        COLPOS: Colombian online GPS data processing service
        ------------------------------------------------------------
        begin                : 2020-03-29
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
import ftplib
import datetime
import os
import sys
from pathlib import Path


class FTPUtil:

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
                print(e)

    @staticmethod
    def ftp_download(server, username, password, remote_dir, remote_file, local_dir, overwrite=False):
        """
        Generic function to download a file using ftp.
        Place it in the local_directory.
        If it already exists, don't download.
        Return the full local filename.
        :param server: ip/dns ftp server
        :param username: ftp login user
        :param password: ftp password user
        :param remote_dir: target directory on the ftp server
        :param remote_file: target file name in ftp
        :param local_dir: path where the file will be downloaded
        :param overwrite: overwrite file if exists
        :return: full path where the file was downloaded to the local server 
        """
        FTPUtil.check_dir(local_dir)  # check that target dir exists, if not create it
        local_fullname = os.path.join(local_dir, remote_file)
        print("ftp_download start at ", datetime.datetime.utcnow())
        if not os.path.exists(local_fullname) or overwrite:
            print('Remote: ', remote_dir + " " + remote_file)
            print('Local : ', local_fullname)
            sys.stdout.flush()
            ftp = ftplib.FTP(server)  # Establish the connection
            ftp.login(username, password)
            ftp.cwd(remote_dir)  # Change to the proper directory
            fhandle = open(local_fullname, 'wb')
            ftp.retrbinary('RETR ' + remote_file, fhandle.write)
            fhandle.close()
            ftp.close()
        else:
            print(remote_file, " already exists locally, not downloading.")
        print("ftp_download Done ", datetime.datetime.utcnow())
        sys.stdout.flush()
        return local_fullname

