import threading
import vk2telegram
# repeater for our script. check for updates every 5 min


def repeater():
    threading.Timer(300.0, repeater).start()
    vk2telegram.vk2telegram()

if __name__ == "__main__":
    repeater()
