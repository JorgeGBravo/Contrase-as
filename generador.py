from random import SystemRandom
import sqlite3
import time
import datetime
import random
import string

d = datetime.datetime.today()
print(d)

conn = sqlite3.connect('pass.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS names
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, serv TEXT UNIQUE, psd TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS pass
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, date TEXT, psd TEXT, serv TEXT)''')

ord = input('Programa: ')


#Creacion de password

longitud = 18

valores =  string.ascii_letters+string.digits + ord
cryptogen = SystemRandom()
pss = ""

while longitud > 0:
    pss = pss + cryptogen.choice(valores)
    longitud = longitud - 1


cur.execute('INSERT OR REPLACE INTO names (serv, psd) VALUES (?, ?)', (ord, pss))
cur.execute('INSERT OR IGNORE INTO pass (date, psd, serv) VALUES (?, ?, ?)', (d, pss, ord,))

conn.commit()

print(pss)