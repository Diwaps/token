import requests
import json
import os
import sys
import time
s = 1
token = input("token")

while True:
api = requests.get("https://discordapp.com/api/v6/invite/sound")
data = api.json()
check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
stuff = check.json()
requests.post("https://discordapp.com/api/v6/invite/sound", headers={"Authorization": token})
requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})
try:
if stuff['code'] == 0:
print("Successfully disabled")
break
except:
print(f"could not disable, trying again... try:{s}")
s+=1
