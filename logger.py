import os
import time
from datetime import datetime, date
import time
import ctypes

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

cwd = os.getcwd()

try:
    filelog = open(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/{datetime.now().strftime("%H-00")}.txt', 'a+')
except FileNotFoundError:
    os.makedirs(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/')
    filelog = open(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/{datetime.now().strftime("%H-00")}.txt', 'a+')
except:
    ctypes.windll.user32.MessageBoxW(0, u"An unexpected error occured. Reporting problem to mircosoft", u"what", 0)
    filelog = 69
    time.sleep(69420)


x = 1
for line in loglines:
    print (line)

    if '[main/INFO]: [CHAT] ' in line:
        filelog.write(line.split('[main/INFO]: [CHAT] ')[1])

    if x > 10:
        filelog.close()
        try:
            filelog = open(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/{datetime.now().strftime("%H-00")}.txt', 'a+')
        except FileNotFoundError:
            os.makedirs(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/')
            filelog = open(f'{cwd}/{datetime.today().year}/{datetime.today().month}/{datetime.today().day}/{datetime.now().strftime("%H-00")}.txt', 'a+')
        except:
            ctypes.windll.user32.MessageBoxW(0, u"An unexpected error occured. Reporting problem to mircosoft", u"what", 0)
        x = 1
    else:
        x += 1

    # now = datetime.now()
    # current_time = datetime.now().strftime("%H-%M")

    # now = datetime.now()
    # current_timeHR = now.strftime("%H")

    # today = date.today()

    # dayofweek = datetime.today().strftime('%A')