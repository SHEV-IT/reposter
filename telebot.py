from urllib.request import urlopen
import urllib.parse
import requests

token = "<here your bot token>"
chat_id = "<here your chat id>"

# reading last id post
with open('last_id.txt') as f:
    last_id = f.read()

# reading last post txt
with open('%s.txt' % (last_id)) as t:
    text = str(t.read())
params = urllib.parse.quote(text, safe='')  # formatting text for url

# sending text
url_send = "https://api.telegram.org/bot%s/sendmessage?chat_id=%s&text=%s" % (token, chat_id, params)
urlopen(url_send)

# sending image
data = {'chat_id': chat_id}
files = {'photo': open("%s.jpg" % (last_id), "rb")}
requests.post("https://api.telegram.org/bot%s" % (token) + '/sendPhoto', data=data, files=files)
