import datetime
import platform
import re
import sqlite3

def nombre():
    while True:
        name = input('Nombre: ')
        name.rstrip()
        namex = re.compile(r'^([A-ZÁÉÍÓÚ]{1}[a-zñáéíóú]+[\s]*)+$')
        search = namex.search(name)
        if search == None:
            print('Nombre Invalido')
            continue
        else:
            print('OK...', name)
            return name

def apellido():
    while True:
        surname = input('Apellido: ')
        surname.strip()
        surnamex = re.compile(r'^([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\']+[\s])+([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\'])+[\s]?([A-Za-zÁÉÍÓÚñáéíóúÑ]{0}?[A-Za-zÁÉÍÓÚñáéíóúÑ\'])?$')
        search = surnamex.search(surname)
        if search == None:
            print('Apellido No Valido')
            continue
        else:
            print('OK...', surname)
            return surname

def correo():
    while True:
        email = input('Introducir Email: ')
        email.strip()
        emailregx = re.compile(r'^[\w.-]+@[\w.-]+\.[\w]{2,6}$' , re.VERBOSE)
        correo = emailregx.search(email)
        if correo == None:
            print('No Valido')
            continue
        else:
            print('Ok...' , email)
            return email


def phonemovil():
    while True:
        movilin = input('Introducir Movil: ')
        movilin.strip()
        movilregx = re.compile(r'^\d{9}$')
        movil = movilregx.search(movilin)
        if movil == None:
            print('No Valido')
            continue
        else:
            print('OK:' + movil.group())
            return movil.group()


name = nombre()
surname = apellido()
email = correo()
movil = phonemovil()
machine = str(platform.architecture())
date = str(datetime.datetime.today())
datemail ='#esta información es enviada desde el terminal a traves de un correo para activar cuenta'

def bdname(name, surname, email, movil, date, machine, datemail):
    print(name, surname, email, movil, date, machine)
    conn = sqlite3.connect('Identifier.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS datos_usuarios
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, surname TEXT, email TEXT UNIQUE, movil INTERGER UNIQUE, date TIMESTAMP, machine TEXT, date-mail TIMESTAMP)''')
    cur.execute('INSERT OR IGNORE INTO datos_usuarios (name, surname, email, movil, date, machine) VALUES (?, ?, ?, ?, ?, ?)', (name, surname, email, movil, date, machine))
    conn.commit()

bdname(name, surname, email, movil, date, machine)