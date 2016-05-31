from urllib.request import urlopen
import requests

token = "<here your bot token>"
chat_id = "<here your chat id>"
# reading last id post
with open('last_id.txt') as f:
    lid = f.read()
# reading last post txt
with open('%s.txt' % (lid)) as t:
    text = t.read()
# sending text
url_send = "https://api.telegram.org/bot%s/sendmessage?chat_id=%s&text=%s" % (token, chat_id, text)
urlopen(url_send)
# sending image
data = {'chat_id': chat_id}
files = {'photo': open("%s.jpg" % (lid), "rb")}
requests.post("https://api.telegram.org/bot%s" % (token) + '/sendPhoto', data=data, files=files)
