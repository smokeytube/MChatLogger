import sqlite3
from datetime import datetime, date
import time

now = datetime.now()
current_time = now.strftime("%H%M")

today = date.today()

conn = sqlite3.connect(f'log{today}.db')

c= conn.cursor()

c.execute(f"""CREATE TABLE log{current_time} (
            playername text,
            message text,
            other text,
            timestamp text
    )""")

c.execute(f"INSERT INTO log{current_time} VALUES ('popbob', 'i am popbob', '', '[12:23]')")
c.execute(f"SELECT * FROM log{current_time}")

print(c.fetchall())

conn.commit()

conn.close()