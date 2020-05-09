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
import datetime
import ftplib
import os
import sys
import logging as log

from src.gps.util.file_util import FileUtil


class FTPUtil:

    @staticmethod
    def ftp_download(server, remote_dir, remote_file, local_dir, overwrite=False):
        """
        Generic function to download a file using ftp.
        Place it in the local_directory.
        If it already exists, don't download.
        Return the full local filename.
        :param server: ip/dns ftp server
        :param remote_dir: target directory on the ftp server
        :param remote_file: target file name in ftp server
        :param local_dir: path where the file will be downloaded
        :param overwrite: overwrite file if exists
        :return: full path where the file was downloaded to the local server
        """
        credentials = FileUtil.get_credentials(server)
        if not credentials:
            log.info("it was not possible to obtain the credentials from .netrc")
            return None

        _username = credentials[0]
        _pass = credentials[1]

        local_fullname = os.path.join(local_dir, remote_file)
        remote_fullname = remote_dir + " " + remote_file
        log.info("ftp_download start at {}".format(datetime.datetime.utcnow()))
        if not os.path.exists(local_fullname) or overwrite:
            log.info('Remote: ' + remote_fullname)
            log.info('Local : ' + local_fullname)
            sys.stdout.flush()

            try:
                ftp = ftplib.FTP(server)  # Establish the connection
                ftp.login(_username, _pass)

                try:
                    ftp.cwd(remote_dir)  # Change to the proper directory
                except ftplib.error_perm:
                    log.error("Remote directory not exist")
                    return None

                try:
                    if ftp.size(remote_file):
                        FileUtil.check_dir(local_dir)  # check that target dir exists, if not create it
                        fhandle = open(local_fullname, 'wb')
                        ftp.retrbinary('RETR ' + remote_file, fhandle.write)
                        fhandle.close()
                except ftplib.error_perm:
                    log.error("File not exist")
                    return None

                ftp.close()
            except ftplib.error_perm:
                log.error("An error occurred while trying to retrieve the file from the server.")
                return None
        else:
            log.info(remote_file + " already exists locally, not downloading.")
        log.info("ftp_download Done {}".format(datetime.datetime.utcnow()))
        sys.stdout.flush()

        return local_fullname
