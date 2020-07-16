
import datetime
import sqlite3
import string
from random import SystemRandom

d = datetime.datetime.today()
print(d)

conn = sqlite3.connect('pass.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS names
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, serv TEXT UNIQUE, psd TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS pass
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, date TEXT, psd TEXT, serv TEXT)''')

def gen():
    ord = input('Programa: ')
    if len(ord) == 0:
        print('Introduce una plataforma')
        gen()
    longitud = 18
    valores = string.ascii_letters + string.digits + ord
    cryptogen = SystemRandom()
    pss = ""
    while longitud > 0:
        pss = pss + cryptogen.choice(valores)
        longitud = longitud - 1
    cur.execute('INSERT OR REPLACE INTO names (serv, psd) VALUES (?, ?)' , (ord , pss))
    cur.execute('INSERT OR IGNORE INTO pass (date, psd, serv) VALUES (?, ?, ?)' , (d , pss , ord ,))
    conn.commit()
    print(pss)
    opciones()

def lectura():
    busqueda = input("Escribe tu búsqueda: ")
    if not busqueda:
        print("Búsqueda Inválida")
        opciones()
    sentencia = "SELECT * FROM names WHERE serv LIKE ?;"
    cur.execute(sentencia , ["%{}%".format(busqueda)])
    row = cur.fetchone()
    ultima = row
    if ultima == None:
        print("No hay Ninguna Coincidencia en la Base de Datos")
        lectura()

    print('                                        PLATAFORMA                    PASSWORD')
    print('')
    print('Password en uso:                     ' , ultima[:2] , '          ' , ultima[2:])
    print('---------------------------------------------------------------------------------------')

    sentencia2 = "SELECT ALL * FROM pass WHERE serv LIKE ?;"
    cur.execute(sentencia2 , ["%{}%".format(busqueda)])
    encuentro = cur.fetchall()
    psd2 = encuentro
    if len(psd2) > 1:
        lista = list()
        for psd in psd2:
            lista.append(psd)
        lista.sort()
        penultima = lista[len(lista) - 2]

        print('Penultima contraseña: ' , penultima)
        opciones()
    else:
        print('                      Solo hay un Password en uso editada')
        opciones()

def opciones():
    print('')
    print('Pulsa: '
          ' A Para Generar -'
          ' B Para Buscar')
    opcion = input('Elige la opción: ')
    opcion = opcion.lower()
    if len(opcion) < 1:
        print('Esa Opcion No es Correcta, Escribe Algo')
        opciones()
    if opcion == 'a':
        gen()
        return
    if opcion == 'b':
        lectura()
    else:
        print('Esa Opcion No Existe')
        opciones()

opciones()