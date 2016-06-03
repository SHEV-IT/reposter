from urllib.request import urlopen
import urllib.parse
import requests
import constants

# setting constants
token = constants.token
chat_id = constants.chat_id
# reading last id post
with open('last_id.txt') as f:
    last_id = f.read()
# reading last post txt
with open('{0}.txt'.format(last_id)) as t:
    text = str(t.read())
params = urllib.parse.quote(text, safe='')  # formatting text for url

# sending text
url_send = "https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text={2}".format(token, chat_id, params)
urlopen(url_send)
# sending image

data = {'chat_id': chat_id}
files = {'photo': open("{0}.jpg".format(last_id), "rb")}
requests.post("https://api.telegram.org/bot{0}".format(token) + '/sendPhoto', data=data, files=files)
