"""Main file for repostig."""
import threading
import vk2telegram


def repeater():
    """Repeater for repeating scripts every 5 min."""
    threading.Timer(300.0, repeater).start()
    vk2telegram.vk2telegram()

if __name__ == "__main__":
    repeater()
