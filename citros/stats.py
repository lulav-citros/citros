import csv
import time
import psutil
import threading



# Example:
# stats = Stats("name.csv", 1)
# stats.start()
# stats.stop()
class SystemStatsRecorder:
    def __init__(self, file_name, interval=1):
        self.file_name = file_name
        self.interval = interval
        with open(file_name, "w") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(
                [
                    "cpu usage (%)",
                    "total memory",
                    "available memory",
                    "used memory",
                    "memory usage (%)",
                ]
            )

        self.stop_flag = threading.Event()
        self.thread = None

    def start(self):
        self.stop_flag.clear()
        # self.thread = threading.Thread(
        #     target=self._run, args=(self.interval, self.file_name)
        # )
        self.thread = threading.Thread(
            target=self._run
        )
        self.thread.start()

    def stop(self):
        if self.thread is not None:
            self.stop_flag.set()
            self.thread.join()

    def _run(self):
        while not self.stop_flag.is_set():
            with open(self.file_name, "a") as file:
                writer = csv.writer(file, delimiter="\t")
                writer.writerow(self._sample())
            time.sleep(self.interval)

    def _sample(self):
        cpu_usage = psutil.cpu_percent()

        memory_info = psutil.virtual_memory()

        total_memory = memory_info.total
        available_memory = memory_info.available
        used_memory = memory_info.used
        memory_percent = memory_info.percent

        return cpu_usage, total_memory, available_memory, used_memory, memory_percent
