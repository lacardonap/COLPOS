from datetime import datetime, timedelta
from src.gps.util.data_time_util import DataTimeUtil

class TaskConfig:

    def __init__(self, rinex):
        self._rinex = None

    @property
    def rinex(self):
        return self._rinex

    @staticmethod
    def get_data_time():
        dt = datetime.utcnow() - timedelta(days=100)
        dtu = DataTimeUtil(dt)
        return dtu

    @staticmethod
    def get_stations():
        return ['bogt', 'gold']
