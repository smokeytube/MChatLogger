import os
import time
from datetime import datetime
import time
import pyautogui
from discord_webhook import DiscordWebhook
import random

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


print ("Starting...")
repit = 1
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print ("Checking time...")
    while True:
        logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
        loglines = follow(logfile)
        now = datetime.now()
        current_timeintlast = now.strftime("%H%M")
        current_timeintlast1 = int(current_timeintlast)
        for line in loglines:
            print (line)
            now = datetime.now()
            current_timeint = now.strftime("%H%M")