import subprocess
import psutil
import time
import os
import ctypes

def is_process_running(pid):    
    return psutil.pid_exists(pid)

def main():
    print("Program Start")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    python_path = os.path.join(script_dir, ".venv", "Scripts", "python")
    watcher_path = os.path.join(script_dir, "src/watcher.py")
    input_path = os.path.join(script_dir, "input.txt")

    watchdog_proc = subprocess.Popen([python_path, watcher_path])
    notepad_proc = subprocess.Popen(["notepad", input_path])

    try:
        while is_process_running(notepad_proc.pid):
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        watchdog_proc.terminate()
        watchdog_proc.wait()

    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(script_dir, "output.png"), 0)
    print('Wallpaper set')

    print("Program End")

if __name__ == '__main__':
    main()