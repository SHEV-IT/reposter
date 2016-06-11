import os
import json
import urllib.request
import constants


def vk_get():
    # get data from vk.com
    vk_id = constants.vk_id
    adr = 'https://api.vk.com/method/wall.get?owner_id={0}&count=10'.format(vk_id)
    data = urllib.request.urlopen(adr)
    decoded_response = data.read().decode()
    final_data = json.loads(decoded_response)
    # getting last post response
    response = final_data['response'][1:2]
    for resp in response:
        current_id = resp['id']  # getting an id
        text = resp['text']  # getting txt
        c = 0
        if 'src_big' in resp:
            c = 1
            url = resp['attachments'][0]['photo']['src_big']
    # getting previous id and writing new id
    if os.path.exists('last_id.txt'):
        with open('last_id.txt') as f:
            prev_id = f.read()
    else:
        prev_id = '0'
    with open('last_id.txt', 'w') as f:
        current_id = str(current_id)  # must be str for writing/creating link
        f.write(str(current_id))
    or_link = "\nOriginal link https://vk.com/wall{0}_{1}".format(vk_id, current_id)
    current_id = int(current_id)  # and now it must be integer
    prev_id = int(prev_id)
    if(current_id - prev_id != 0):
        text = text + or_link
        if c == 1:
            return text, url
        return text, False
    else:
        return False, False
