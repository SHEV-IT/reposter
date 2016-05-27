import json
import urllib.request
from urllib.request import urlopen

# get data from vk.com
address = 'https://api.vk.com/method/wall.get?owner_id=-100567023&count=10'
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)

# formattig response
response1 = final_data['response'][1:2]
respid = str(response1)
respid = respid.split()

# getting last id post
position = respid.index("'id':")
idp = (respid[position + 1])
idp = idp.replace(',', '')
idp = idp.replace('}', '')
idp = idp.replace(']', '')

# getting previous id and writing new id
filename = '/home/wasper/Documents/Python/Projects/reposter/vk_check/last_id.txt'
pid = open(filename, 'r')
pid = pid.read()
file = open(filename, 'w')
file.write(idp)
file.close()

idp = int(idp)
pid = int(pid)
rp = (response1)
# getting post
if(idp - pid != 0):
    # getting text of last post
    rp = str(rp)
    rp = rp.split("'")
    pos = rp.index('text')
    text = (rp[pos + 2])
    print(text)
    fn = '/home/wasper/Documents/Python/Projects/reposter/vk_check/%s.txt' % (idp)
    file = open(fn, 'w')
    file.write(text)
    file.close()

    # getting image
    c = rp.count('src_big')  # test for image
    if(c > 0):
        pos = rp.index('src_big')
        photol = (rp[pos + 2])
        urllib.request.urlretrieve("%s" % (photol), "/home/wasper/Documents/Python/Projects/reposter/vk_check/%s.jpg" % (idp))
else:
    print('no new posts')
