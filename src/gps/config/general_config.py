import os

# DATA OUTPUT DIRECTORIES
# PREFIX_DIR = os.getcwd()
PREFIX_DIR = '/home/grand/Desktop/TEST'
PREFIX_DATA_DIR = os.path.join(PREFIX_DIR, 'DATA')
PREFIX_ORBITS_DIR = os.path.join(PREFIX_DATA_DIR, 'ORBITS')
PREFIX_CLOCKS_DIR = os.path.join(PREFIX_DATA_DIR, 'CLOCKS')
BRDC_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'BRDC')
IGS_FINAL_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'IGS_FINAL')  # Satellite orbit solution
IGS_30_SEC_CLOCK_DIR = os.path.join(PREFIX_CLOCKS_DIR, 'IGS_30_SEC')  # Clock
IGS_ERP_DIR = os.path.join(PREFIX_DATA_DIR, 'IGS_ERP')  # Earth Rotation Parameters
IGS_EPH_DIR = os.path.join(PREFIX_DATA_DIR, 'IGS_EPH')  # Satellite Orbit Solution
PREFIX_RINEX_DIR = os.path.join(PREFIX_DIR, 'RINEX')

# FTPS DATA SOURCES
FTP_SERVER_ESA = 'gssc.esa.int'
FTP_SERVER_CDDIS = 'cddis.gsfc.nasa.gov'

# HTTPS DATA SOURCES
HTTPS_SERVER_CDDIS = 'cddis.nasa.gov'
EARTH_DATA_NASA_AUTH_HOST = 'urs.earthdata.nasa.gov'

PREFIX_PROCESSING_DIR = os.path.join(PREFIX_DIR, 'PROCESSING')
PPP_PROCESSING_DIR = os.path.join(PREFIX_PROCESSING_DIR, 'PPP')
