from urllib.request import urlopen
import json
address = 'https://api.vk.com/method/wall.get?owner_id=-100567023&count=10'
data = urlopen(address)
decoded_response = data.read().decode()
final_data = json.loads(decoded_response)
response = final_data['response'][1:2]
resp = str(response)
resp = resp.split()
position = resp.index("'id':")
idp = (resp[position + 1])
idp = idp.replace(',', '')
idp = idp.replace('}', '')
idp = idp.replace(']', '')
print (idp)
