import os

# CONFIG FILES
MAIN_APP_DIR = '/mnt/LDATA/DEV/COLPOS'
COMMON_CONFIG_DIR = os.path.join(MAIN_APP_DIR, 'src/gps/common')
RTKLIB_PPP_CONFIG_FILE = os.path.join(COMMON_CONFIG_DIR, 'rtklib_ppp.conf')
IGS_14_ATX_FILE = os.path.join(COMMON_CONFIG_DIR, 'igs14.atx')

# DATA OUTPUT DIRECTORIES
INPUTS_PREFIX_DIR = '/home/grand/Desktop/TEST'
PREFIX_DATA_DIR = os.path.join(INPUTS_PREFIX_DIR, 'DATA')
PREFIX_ORBITS_DIR = os.path.join(PREFIX_DATA_DIR, 'ORBITS')
PREFIX_CLOCKS_DIR = os.path.join(PREFIX_DATA_DIR, 'CLOCKS')
BRDC_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'BRDC')
IGS_FINAL_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'IGS_FINAL')  # Satellite orbit solution
IGS_30_SEC_CLOCK_DIR = os.path.join(PREFIX_CLOCKS_DIR, 'IGS_30_SEC')  # Clock
IGS_ERP_DIR = os.path.join(PREFIX_DATA_DIR, 'IGS_ERP')  # Earth Rotation Parameters
IGS_EPH_DIR = os.path.join(PREFIX_DATA_DIR, 'IGS_EPH')  # Satellite Orbit Solution
RINEX_DIR = os.path.join(INPUTS_PREFIX_DIR, 'RINEX')

# FTPS DATA SOURCES
FTP_SERVER_ESA = 'gssc.esa.int'
FTP_SERVER_CDDIS = 'cddis.gsfc.nasa.gov'

# HTTPS DATA SOURCES
HTTPS_SERVER_CDDIS = 'cddis.nasa.gov'
EARTH_DATA_NASA_AUTH_HOST = 'urs.earthdata.nasa.gov'

# OUTPUT PROCESSING DIRS
PREFIX_PROCESSING_DIR = os.path.join(INPUTS_PREFIX_DIR, 'PROCESSING')
PPP_PROCESSING_DIR = os.path.join(PREFIX_PROCESSING_DIR, 'PPP')
RTKLIB_TAG = "rtklib"  # used in the results-file filename
RTKLIB_BINARY = "rnx2rtkp"  # must have this executable in path

# RABBIT QM QUEUE SERVER
QUEUE_SERVER = 'localhost'
QUEUE_NAME = 'processing_gps'
EXCHANGE_NAME = ''
ROUTING_KEY_NAME = 'processing_gps'

