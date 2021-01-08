import os
import time
import sqlite3
from datetime import datetime, date
import time

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
x = 1
for line in loglines:
    print (line)
    now = datetime.now()
    current_time = now.strftime("%H_%M")

    today = date.today()

    conn = sqlite3.connect(f'log{today}.db')

    c= conn.cursor()

    if x == 1:
        try:
            c.execute(f"""CREATE TABLE log{current_time} (
                        playername text,
                        message text,
                        other text,
                        timestamp text
                )""")
            x = x+1
        except:
            pass

    c.execute(f"INSERT INTO log{current_time} VALUES ({line.split(']')[2]}, 'i am popbob', '', 'hi')")
    c.execute(f"SELECT * FROM log{current_time}")

    print(c.fetchall())

    conn.commit()

    conn.close()