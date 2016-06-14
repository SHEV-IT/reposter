"""This module for work with Telegram BOT API."""
import requests
import constants
import urllib
import urllib.parse
import io


def send_txt(text):
    """Sending text to telegram."""
    url_send = "https://api.telegram.org/bot{}/sendmessage?{}".format(
        constants.token,
        urllib.parse.urlencode({
            "chat_id": constants.chat_id,
            "text": text
        })
    )
    urllib.request.urlopen(url_send)


def send_img(url):
    """Sending image to telegram."""
    data = {'chat_id': constants.chat_id}
    bnr = urllib.request.urlopen(url).read()  # binary response
    raw = io.BytesIO(bnr)  # raw image
    raw.name = "image.jpg"  # setting name for image. must have for telegram
    files = {'photo': io.BufferedReader(raw)}
    requests.post(
        "https://api.telegram.org/bot{0}".format(constants.token) +
        "/sendPhoto", data=data, files=files
    )
