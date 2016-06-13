"""Work with API scripts."""
import vk
import telebot
import constants


def vk2telegram():
    """Running scrips for getting and posting posts."""
    vk_id = constants.vk_id
    response = vk.vk_get(vk_id)
    if response[0]:
        telebot.tbotxt(response[0])
    if response[1]:
        telebot.tbotimg(response[1])

if __name__ == "__main__":
    vk2telegram()
