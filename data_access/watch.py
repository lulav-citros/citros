import os
import sys
import time
import json
import glob
import logging
from rich import print, inspect, print_json
from rich.panel import Panel
from rich.padding import Padding
from rich.logging import RichHandler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler

# from batch import Batch
from citros.batch import Batch


# start listening on the folder changes and calls on_folder_change_handler on each change
class BatchRunFolderWatch:    
    def __init__(self, path, log):
        self.observer = Observer()
        
        self.path = path
        self.log = log
        
        # we are looking on 
        #   batch/info.json
        #   batch/simulation/info.json
        self.event_handler = HandlerPattern(
            root=self.path,
            log=self.log,
            patterns=["*/info.json"],
            ignore_patterns=[],
            ignore_directories=True)

    def run(self):
        self.observer.schedule(self.event_handler, 'tmp', recursive=True)
        
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()            
            self.log.exception("Error")

        self.observer.join()


class HandlerPattern(PatternMatchingEventHandler):
    def __init__(self, root, log=None, patterns=["*"],
            ignore_patterns=[],
            ignore_directories=False):
        PatternMatchingEventHandler.__init__(self, patterns=patterns,
            ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories)
        self.root = root   
        self.log = log    
        
    def on_any_event(self, event):
        # inspect(event)
        # print("vova", self.root)
        # print("vova", event.src_path)
        # print("vova", event.src_path.removeprefix(self.root))
        # print("event.event_type", event.event_type)
        if event.event_type == 'deleted':
            return
        simulation_name = event.src_path.removeprefix(self.root).removeprefix('/').split('/')[0]
        batch_name = event.src_path.removeprefix(self.root).removeprefix('/').split('/')[1]
        
        print(Panel(f"detected changed in simulaiton / batch run name: [green]{simulation_name}/{batch_name}[/green]"))
        batch = Batch(self.root, simulation_name, batch_name, self.log)
        print_json(data=batch.data)



if __name__ == '__main__':
    logging.basicConfig(
        level=os.environ.get("LOGLEVEL", "INFO"),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    log = logging.getLogger(__name__)
    
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'    
    path = os.environ.get("RUNS_DIR", "tmp")
    
    print("[bold green]CITROS[/bold green] data-access")
    
    w = BatchRunFolderWatch(os.path.join(os.getcwd(), path) , log)
    w.run()
    
    print("[bold green]CITROS[/bold green] data-access is out of the building.")
    
    