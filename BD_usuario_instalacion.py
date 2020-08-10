import datetime
import platform
import re
import sqlite3


def correo():
    email = input('Introducir Email: ')
    emailregx = re.compile(r'''(
                [a-zA-Z0-9._%+-]+
                @
                [a-zA-Z0-9._]+
                (\.[a-zA-Z0-9]{2-6})
                )''' , re.VERBOSE)
    correo = emailregx.search(email)
    print(correo)
    if correo == None:
        print('No Valido')
        return correo()
    else:
        print('Ok...' , email)
        return email



def phonemovil():
    movilin = input('Movil')
    movilregx = re.compile(r'\d\d\d\d\d\d\d\d\d')
    if len(movilin) != 9:
        print('No Valido')
        return phonemovil()
    movil = movilregx.search(movilin)
    if movil == None:
        print('No Valido')
        return phonemovil()
    else:
        print('OK:' +movil.group())
        return movil.group()




name = input('Name: ')
surname = input('Surname: ')
email = correo()
movil = phonemovil()
machine = str(platform.architecture())
date = str(datetime.datetime.today())

def bdname(name, surname, email, movil, date, machine):
    print(name, surname, email, movil, date, machine)
    conn = sqlite3.connect('Identifier.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS datos_usuarios
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, surname TEXT, email TEXT UNIQUE, movil INTERGER UNIQUE, date TIMESTAMP, machine TEXT)''')
    cur.execute('INSERT OR IGNORE INTO datos_usuarios (name, surname, email, movil, date, machine) VALUES (?, ?, ?, ?, ?, ?)', (name, surname, email, movil, date, machine))
    conn.commit()

bdname(name, surname, email, movil, date, machine)