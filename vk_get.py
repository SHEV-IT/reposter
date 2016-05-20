import json
from urllib.request import urlopen

address = 'https://api.vk.com/method/wall.get?owner_id=-100567023&count=10'
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)

response1 = final_data['response'][1:2]
respid = str(response1)
respid = respid.split()

position = respid.index("'id':")
idp = (respid[position + 1])
idp = idp.replace(',', '')
idp = idp.replace('}', '')
idp = idp.replace(']', '')
print(idp)

filename = '/home/wasper/Documents/Python/Projects/reposter/vk_check/last_id.txt'
pid = open(filename, 'r')
pid = pid.read()
file = open(filename, 'w')
file.write(idp)
file.close()

idp = int(idp)
pid = int(pid)
rp = (response1)
if(idp - pid == 1):
    rp = str(rp)
    rp = rp.split("'")
    pos = rp.index('copy_text')
    print(pos)
    text = (rp[pos + 2])
    print(text)
    fn = '/home/wasper/Documents/Python/Projects/reposter/vk_check/%s.txt' % (idp)
    file = open(fn, 'w')
    file.write(text)
    file.close()

else:
    print('no new posts')
