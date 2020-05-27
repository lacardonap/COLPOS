from src.gps.task.gps_task import GPSTask


class TaskManager:
    def __init__(self):
        self.__pull_task = list()

    def create_task(self, task_config):
        task = GPSTask(task_config)
        self.__pull_task.append(task)  # Register task to the pull
        return task
