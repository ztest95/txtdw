import subprocess
import psutil
import time

def is_process_running(pid):    
    return psutil.pid_exists(pid)

if __name__ == '__main__':
    print("Program Start")
    watchdog_proc = subprocess.Popen([".venv/Scripts/python", "./watcher.py"])
    notepad_proc = subprocess.Popen(["notepad", "./input.txt"])

    try:
        while is_process_running(notepad_proc.pid):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        watchdog_proc.terminate()
        watchdog_proc.wait()

    print("Program End")