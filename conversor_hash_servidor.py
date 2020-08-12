import hashlib
import sqlite3


def encript(date, surname):
    aencript = date + surname
    bytetable = str.encode(aencript)
    hashname = hashlib.sha256(bytetable).hexdigest()
    return
hashname = encript()

def tabla_create(hashname):
    conn = sqlite3.connect(hashname +'.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS names
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, serv TEXT UNIQUE, psd TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS pass
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, date TEXT, psd TEXT, serv TEXT)''')
    conn.commit()

def bdname(name, surname, email, movil, date, machine):         #falta detalles como es la confirmación del correo electronico que está en la BD de usuarios, que está definida como date-mail
    print(name, surname, email, movil, date, machine)
    conn = sqlite3.connect('Identifier.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS datos_usuarios
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, surname TEXT, email TEXT UNIQUE, movil INTERGER UNIQUE, date TIMESTAMP, machine TEXT, date-mail TIMESTAMP)''')
    cur.execute('INSERT OR IGNORE INTO datos_usuarios (name, surname, email, movil, date, machine) VALUES (?, ?, ?, ?, ?, ?)', (name, surname, email, movil, date, machine))
    conn.commit()

