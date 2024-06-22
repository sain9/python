# import os
# import sys
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# class MyHandler(FileSystemEventHandler):
#     def on_any_event(self, event):
#         if event.src_path.endswith('.py'):
#             print(f'Restarting script due to change in {event.src_path}')
#             os.system('pkill -f "python3 1string.py"')  # Replace with your script name
#             time.sleep(1)
#             os.system('python3 1string.py &')  # Replace with your script name

# if __name__ == "__main__":
#     event_handler = MyHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path='.', recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    
    def on_modified(self, event):

        filename = '7fromatString.py' #add your filename

        if event.src_path.endswith(filename):
            print(f'\n\033[44m\033[37mFile {filename} has been modified. Running script...\033[0m\n','\n')
            result = subprocess.run(['python3', filename], capture_output=True, text=True)
            print(f'\033[1m\033[4m\033[33mCode Output\033[0m \n')
            # print(f'\033[1m\033[4m\033[31mCode Output\033[0m')
             # Print stdout in bold cyan
            # print(f'\033[1m\033[36m\033[40m{result.stdout}\033[1m')
            # Print stdout in bold green
            print(f'\033[1m\033[32m{result.stdout}\033[0m')

            if result.stderr:
              print(f'\033[1m\033[4m\033[31mOOps!, An Error occured...\033[0m \n')
            # print(f'\033[1m\033[4m\033[31mCode Output\033[0m')
              # Print stderr in yellow if it exists
            #   print(f'\033[1m\033[31m{result.stderr}\033[0m')
            #   print(f'\033[1m\033[33m\033[41m{result.stderr}\033[0m')
             
              # Example of bold bright white text on a red background
              print(f'\033[1m\033[97m\033[41m{result.stderr}\033[0m')

              

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

