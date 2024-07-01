from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time 

class Watcher:
    DIRECTORY_TO_WATCH = "./"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_modified(event):
        if event.src_path == ("./input.txt"):
            print("%s has been modified" % event.src_path)
            subprocess.run([".venv/Scripts/python", "main.py"])
            # Place your code to run on file save here


if __name__ == '__main__':
    print("Running watcher.py")
    w = Watcher()
    w.run()
