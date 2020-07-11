from colorama import Fore, init, Style
import requests
import random
import ctypes
import time
import os

token = "mfa.Jvw_OjDYP9fv98tmQZKeSpaf8PpQ1UhOttRvZWd9aaMYqLCs4Om3W6uUwttHCldB0ZfcI8F-tIaKunmlyZS4"
def ChangeStatus():
    try:
        session = requests.Session()
        headers = {
            'authorization': token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
            'content-type': 'application/json'
        }
        text = random.choice(['Sleeping.', "Sleeping.", "Sleeping."])
        data = '{"custom_status":{"text":"' + text + '"}}'
        r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
        if '"custom_status": {"text": "' in r.text:
            print(Fore.GREEN + '[SUCCESS] ' + Fore.WHITE + Style.BRIGHT + 'Status changed: ' + str(text))
        else:
            print(r.text)
    except:
        pass
    time.sleep(1)
while True:
    ChangeStatus()
    time.sleep(9000)