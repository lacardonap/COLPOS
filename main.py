import logging
from src.gps.task.task_config import TaskConfig
from src.gps.task.task_manager import TaskManager

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

task_config = TaskConfig('rinex_filename')
task_manager = TaskManager()

task = task_manager.create_task(task_config)
task.run()
