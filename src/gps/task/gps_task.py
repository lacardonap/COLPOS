import logging as log
import tempfile
from src.gps.data.data_manager import DataManager
from src.gps.util.file_util import FileUtil



class GPSTask:

    def __init__(self, task_config):
        self._task_config = task_config
        self._dtu = task_config.get_data_time()
        self._stations = task_config.get_stations()
        self._data_manager = DataManager()
        self._tmp_dir = tempfile.mkdtemp()

    def run(self):
        # Get inputs needed for processing
        self._data_manager.get_inputs(self._dtu)
        self._data_manager.get_rinexs(self._stations)

        # Copy data to processing dir
        self.prepare_processing_inputs()
        log.info("Done: Data was copy to {}".format(self._tmp_dir))

    def prepare_processing_inputs(self):

        # Copy inputs parameter to processing dir
        for parameter in self._data_manager.get_inputs_parameters():
            FileUtil.copy_and_decompress(self._tmp_dir, parameter)

        # Copy rinex to processing dir
        for rinex_name, rinex_path in self._data_manager.rinexs.items():
            FileUtil.copy_and_decompress(self._tmp_dir, rinex_path)

    @property
    def tmp_dir(self):
        return self._tmp_dir
