import datetime
import platform
import sqlite3


def correo():
    for i in email:
        if i == '@':
            continue


def phonenumber():
    if len(movil) != 9:
        return print('Numero no Valido cantidad')
    if movil == float:
        return print('Numero no Valido letra')
    for i in movil:
        if not movil[i].isdecimal():
            return print('No valido')
    else:
        print('Perfecto')


name = input('Name: ')
surname = input('Surname: ')
email = input('Email: ')
movil = input('Movil:')


machine = str(platform.architecture())
date = str(datetime.datetime.today())


def bdname():

    conn = sqlite3.connect('Identifier.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS identifier
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE, surname, TEXT, email TEXT, movil INTERGER, date INTERGER, machine TEXT)''')
    cur.execute('INSERT OR IGNORE INTO identifier (name, surname, email, movil, date, machine) VALUES (?, ?, ?, ?, ?, ?)' , (name, surname, email, movil, date, machine,))

bdname()