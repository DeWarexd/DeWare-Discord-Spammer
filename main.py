import requests
from time import sleep
import random
import os
import pyfade

os.system("cls")

print(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red, '''
▓█████▄ ▓█████  ██░ ██  ▒█████   ▒█████   ██ ▄█▀
▒██▀ ██▌▓█   ▀ ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
░██   █▌▒███   ▒██▀▀██░▒██░  ██▒▒██░  ██▒▓███▄░ 
░▓█▄   ▌▒▓█  ▄ ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄ 
░▒████▓ ░▒████▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
 ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
 ░ ▒  ▒  ░ ░  ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
 ░ ░  ░    ░    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
   ░       ░  ░ ░  ░  ░    ░ ░      ░ ░  ░  ░     by Denolaks
 ░    

┌─────────────│DeHook Features│─────────────┐
│Spam Multiple Channels same time.          │
├───────────────────────────────────────────┤
│https://github.com/Denolaks                │
├───────────────────────────────────────────┤
│Undetected 2022                            │
├───────────────────────────────────────────┤
│discord.gg/HXCxmc4G4J                      │
└───────────────────────────────────────────┘'''))

f = open("Token.txt", "r")
t = open("SpamText.txt","r")

token = f.read()

items = [
    t.read()
]
print(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,"\n╔══════════DeHook══════════╗"))

howmuch = int(input(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,"How much channels do you want to spam: ")))

channels = {}

for i in range(howmuch):
    idx = int(input(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,"Enter id: ")))
    channels[f"Channel {i} id: "] = idx
print(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,f"Channels: {channels}"))
print(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,"╚══════════DeHook══════════╝"))

interval = float(input(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,"Spam interval: ")))

for i in range(30):

    pe = False # if true enables proxies.

    content = random.choice(items)

    payload = {
        "content": content
    }


    headers = {'authorization': token, 'user-agent': 'nigerus6/9'}

    #its slow as well because idk
    if pe == True:
        proxies = {
            "https": "185.242.162.87:8080"
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{guildid}/messages", data=payload, headers=headers, proxies=proxies)
        r = requests.post(f"https://discord.com/api/v9/channels/{guildid2}/messages", data=payload, headers=headers, proxies=proxies)
    
    for key,channelids in channels.items():
        print(pyfade.Fade.Vertical(pyfade.Colors.yellow_to_red,f"{key}: {channelids}"))
        r = requests.post(f"https://discord.com/api/v9/channels/{channelids}/messages", data=payload, headers=headers)
        sleep(interval)
        
    #not working idk why ill fix later
    # if(r.text.__contains__ == "<Response [200]>" == True):
    #     print(f"Succesfully sent message.")
    # else:
    #     print(f"Can't send message. Probably because ratelimit. Please wait.")