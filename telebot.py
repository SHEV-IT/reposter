import requests
import constants
import urllib
import io


def tbotxt(text):
    params = urllib.parse.quote(text, safe='')  # formatting text for url
    url_send = "https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text={2}".format(constants.token, constants.chat_id, params)
    urllib.request.urlopen(url_send)


def tbotimg(url):
    data = {'chat_id': constants.chat_id}
    bnr = urllib.request.urlopen(url).read()  # binary response
    raw = io.BytesIO(bnr)  # raw image
    raw.name = "bullshit.jpg"  # setting name for image. must have for telegram
    files = {'photo': io.BufferedReader(raw)}
    requests.post("https://api.telegram.org/bot{0}".format(constants.token) + '/sendPhoto', data=data, files=files)
