import json
import re
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
idp = re.sub(r'\,|\}|\]', '', idp)

# getting previous id and writing new id
with open('last_id.txt') as f:
    pid = f.read()
with open('last_id.txt', 'w') as f:
    f.write(idp)

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
    with('%s.txt' % (idp), 'w') as w:
        w.write(text)

    # getting image
    c = rp.count('src_big')  # test for image
    if(c > 0):
        pos = rp.index('src_big')
        photol = (rp[pos + 2])
        urllib.request.urlretrieve("%s" % (photol), "%s.jpg" % (idp))
else:
    print('no new posts')
