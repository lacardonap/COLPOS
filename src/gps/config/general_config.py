import os

from src.gps.config.enums import EnumDataSourceType
from src.gps.config.key_names import KeyNames

# PREFIX_DIR = os.getcwd()
PREFIX_DIR = '/home/grand/Desktop/TEST'
PREFIX_ORBITS_DIR = os.path.join(PREFIX_DIR, 'DATA', 'ORBITS')
BRDC_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'BRDC')
IGS_FINAL_ORBITS_DIR = os.path.join(PREFIX_ORBITS_DIR, 'IGS_FINAL')

FTP_DATA_SOURCES = {
    EnumDataSourceType.ESA: {
        KeyNames.FTP_SERVER: 'gssc.esa.int',
        KeyNames.FTP_PRODUCT_BASE_PATH: os.path.join('gnss'),
        KeyNames.FTP_PORT: '22',
        KeyNames.FTP_USERNAME: 'anonymous',
        KeyNames.FTP_PASSWORD: ''
    },
    EnumDataSourceType.CDDIS: {
        KeyNames.FTP_SERVER: 'cddis.gsfc.nasa.gov',
        KeyNames.FTP_PRODUCT_BASE_PATH: os.path.join('gnss'),
        KeyNames.FTP_PORT: '22',
        KeyNames.FTP_USERNAME: 'anonymous',
        KeyNames.FTP_PASSWORD: ''
    }
}
