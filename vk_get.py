import os
import json
import re
import urllib
import telebot
import constants

# get data from vk.com
vk_id = constants.vk_id
adr = 'https://api.vk.com/method/wall.get?owner_id={0}&count=5'.format(vk_id)
data = urllib.request.urlopen(adr)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)

# getting last post response
response = final_data['response'][1:2]
for resp in response:
    current_id = resp['id']  # getting an id
    text = resp['text']  # getting txt
# getting previous id and writing new id
if os.path.exists('last_id.txt'):
    with open('last_id.txt') as f:
        prev_id = f.read()
else:
    prev_id = '0'
with open('last_id.txt', 'w') as f:
    current_id = str(current_id)  # it must be string
    f.write(current_id)
current_id = int(current_id)  # and now it must be integer
prev_id = int(prev_id)

# getting post
if(current_id - prev_id != 0):
    if not text:
        print("No text in post#{0}".format(current_id))
    else:
        telebot.tbotxt(text)  # sending text
    rp = str(resp)
    rp = rp.split()
    c = rp.count("'src_big':")  # test for image
    if(c > 0):
        pos = rp.index("'src_big':")  # getting image url
        url = (rp[pos + 1])
        url = re.sub(r"\'|\,", '', url)
        telebot.tbotimg(url)
else:
    print('no new posts')
