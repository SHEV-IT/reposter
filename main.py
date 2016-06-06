import threading
import os
# repeater for our script. check for updates every 5 min


def repeater():
    threading.Timer(300.0, repeater).start()
    os.system('python3 vk_get.py')

if __name__ == "__main__":
    repeater()
