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
import logging as log
import os
import sys
from netrc import netrc

import requests

from src.gps.config.general_config import EARTH_DATA_NASA_AUTH_HOST
from src.gps.util.file_util import FileUtil


class SessionWithHeaderRedirection(requests.Session):
    AUTH_HOST = EARTH_DATA_NASA_AUTH_HOST

    def __init__(self, username, password):
        super().__init__()
        self.auth = (username, password)  # Overrides from the library to keep headers when redirected to or from

    # the NASA auth host.
    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url

        if 'Authorization' in headers:
            original_parsed = requests.utils.urlparse(response.request.url)
            redirect_parsed = requests.utils.urlparse(url)

            if ((original_parsed.hostname != redirect_parsed.hostname)
                    and (redirect_parsed.hostname != self.AUTH_HOST)
                    and (original_parsed.hostname != self.AUTH_HOST)):
                del headers['Authorization']
        return


class HTTPUtil:

    @staticmethod
    def http_download_cddis_ssl(server, remote_dir, remote_file, local_dir, overwrite=False):
        """
        Generic function to download a file using https from cddis
        Place it in the local_directory. If it already exists, don't download.
        Return the full local filename.
        :param server: ip/domain address of the server where the information is located
        :param remote_dir: target directory on the http server
        :param remote_file: target file name in http server
        :param local_dir: path where the file will be downloaded
        :param overwrite: overwrite file if exists
        :return: full path where the file was downloaded to the local server.
        None if it was not possible to obtain it.
        """
        local_fullname = os.path.join(local_dir, remote_file)
        remote_fullname = "https://{}/{}/{}".format(server, remote_dir, remote_file)

        log.info("http_download start at {}".format(datetime.datetime.utcnow()))

        _netrc = netrc()  # authentication credentials are obtained from the netrc file
        _username, _account_pass, _pass = _netrc.authenticators(server)

        session = SessionWithHeaderRedirection(_username, _pass)

        if not os.path.exists(local_fullname) or overwrite:
            log.info('Remote: ' + remote_fullname)
            log.info('Local : ' + local_fullname)
            sys.stdout.flush()
            try:
                # check if request file exist in the server
                response = session.get(remote_fullname + "*?list")
                if response.status_code is not requests.codes.ok:
                    log.error("File not found in the server. HTML code: %d" % response.status_code)
                    return None

                FileUtil.check_dir(local_dir)  # check that target dir exists, if not create it
                response = session.post(remote_fullname)  # retrieve file
                if response.status_code is requests.codes.ok:
                    with open(local_fullname, "wb") as f_out:
                        f_out.write(response.content)
                else:
                    log.error("Was not able to download the file from the server.")
                    return None
            except requests.exceptions.ConnectionError:
                log.error("An error occurred while trying to retrieve the file from the server.")
                return None
        else:
            log.info(remote_file + " already exists locally, not downloading.")
        log.info("http_download Done {}".format(datetime.datetime.utcnow()))
        sys.stdout.flush()

        return local_fullname
