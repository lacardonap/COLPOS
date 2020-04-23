import datetime
from src.gps.data.data_management import DataManagement
from src.gps.util.data_time_util import DataTimeUtil

import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

dt = datetime.datetime.utcnow() - datetime.timedelta(days=100)
dtu = DataTimeUtil(dt)
dm = DataManagement()

# Download brdc orbit
dm.retrieve_brdc_file(dtu)

# Download igs final orbit sp3 format
dm.retrieve_igs_final_gps_orbit(dtu)

# Download igs 30 sec clock products
dm.retrieve_igs_30_sec_clock(dtu)
