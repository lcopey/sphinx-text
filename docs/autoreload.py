from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from datetime import datetime, timedelta
import os


class Watcher:

    def __init__(self, directory=".", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class SphinxHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_modified = datetime.now()

    def on_modified(self, event):
        delta = datetime.now() - self.last_modified
        if delta > timedelta(seconds=1) and not event.is_directory and event.src_path.endswith('.py'):
            self.last_modified = datetime.now()
            print(event)
            os.system('make html')


if __name__ == '__main__':
    source_watcher = Watcher('../src', SphinxHandler())
    source_watcher.run()

    doc_watcher = Watcher('./source', SphinxHandler())
    doc_watcher.run()
