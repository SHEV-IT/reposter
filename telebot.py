from urllib.request import urlopen
import requests

token = "<here your bot token>"
chat_id = "<here your chat id>"
# reading last id post
with open('last_id.txt') as f:
    lid = f.read()
# reading last post txt
with open('{0}.txt'.format(lid)) as t:
    text = t.read()
# sending text
url_send = "https://api.telegram.org/bot{0}/sendmessage?chat_id={1}&text={2}".format(token, chat_id, text)
urlopen(url_send)
# sending image
data = {'chat_id': chat_id}
files = {'photo': open("{0}.jpg".format(lid), "rb")}
requests.post("https://api.telegram.org/bot{0}s".format(token) + '/sendPhoto', data=data, files=files)
