import json
import urllib.request
from urllib.request import urlopen

# get data from vk.com
address = 'https://api.vk.com/method/wall.get?owner_id=-16092359&count=10'
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)

# getting last post response
response = final_data['response'][1:2]
for resp in response:
    current_id = resp['id']  # getting an id
    text = resp['text']  # getting txt

# getting previous id and writing new id
with open('last_id.txt') as f:
    prev_id = f.read()
with open('last_id.txt', 'w') as f:
    current_id = str(current_id)  # it must be string
    f.write(current_id)
current_id = int(current_id)  # and now it must be integer
prev_id = int(prev_id)

# getting post
if(current_id - prev_id != 0):
    with open('{0}.txt'.format(current_id), 'w') as t:
        t.write(text)
    # getting image
    rp = str(resp)
    rp = rp.split()
    c = rp.count('src_big')  # test for image
    if(c > 0):
        pos = rp.index('src_big')  # getting image url
        url = (rp[pos + 2])
        urllib.request.urlretrieve("{0}".format(url), "{0}.jpg".format(current_id))  # writing image
else:
    print('no new posts')
