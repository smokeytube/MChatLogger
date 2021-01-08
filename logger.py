import os
import time
from datetime import datetime
import time
import sqlite3

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


logfile = open(os.getenv("APPDATA")+"/.minecraft/logs/latest.log", "r")
loglines = follow(logfile)
for line in loglines:
    print (line)
    now = datetime.now()
    current_timeint = now.strftime("%H%M")