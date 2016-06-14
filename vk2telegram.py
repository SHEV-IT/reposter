"""Work with API scripts."""
import vk
import telebot
import constants


def vk2telegram():
    """Running scrips for getting and posting posts."""
    vk_id = constants.vk_id
    response = vk.get(vk_id)
    if response[0]:
        telebot.send_txt(response[0])
    if response[1]:
        telebot.send_img(response[1])

if __name__ == "__main__":
    vk2telegram()
