import base64
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
        opciones()
    encript = 18
    valores = string.ascii_letters + string.digits + ord
    cryptogen = SystemRandom()
    pss = ""
    for i in range(18):
        pss = pss + cryptogen.choice(valores)
        pssbytes = bytes(pss, encoding ="utf-8")
        for i in range(1, encript + 1):
            pss64 = base64.b64encode(pssbytes)

    cur.execute('INSERT OR REPLACE INTO names (serv, psd) VALUES (?, ?)' , (ord , pss64))
    cur.execute('INSERT OR IGNORE INTO pass (date, psd, serv) VALUES (?, ?, ?)' , (d , pss64 , ord ,))
    conn.commit()
    print(pss)
    opciones()

def lectura():
    decript = 18
    busqueda = input("Escribe tu búsqueda: ")
    if not busqueda:
        print("Búsqueda Inválida")
        opciones()
    sentencia = "SELECT * FROM names WHERE serv LIKE ?;"
    cur.execute(sentencia , ["{}".format(busqueda)])  #'.*pattern.*'
    row = cur.fetchone()
    if row == None:
        print("No hay Ninguna Coincidencia en la Base de Datos")
        lectura()
    ultimabytes = row[2]
    for i in range(1 , decript + 1):
        ultima = base64.b64decode(ultimabytes)
    ultima = ultima.decode()

    print('                                        PLATAFORMA                    PASSWORD')
    print('')
    print('Password en uso:                          ', row[1], '                 ', ultima)
    print('---------------------------------------------------------------------------------------')

    sentencia2 = "SELECT ALL * FROM pass WHERE serv LIKE ?;"
    cur.execute(sentencia2, ["{}".format(busqueda)])
    datos64 = cur.fetchall()
    if len(datos64) > 1:
        lista = list()
        for pss64 in datos64:
            lista.append(pss64)
            lista.sort()
            penultima64 = lista[len(lista) - 2]
            pasw64 = penultima64[2]
            for i in range(1 , decript + 1):
                penultima = base64.b64decode(pasw64)
            penultima = penultima.decode()

            print('Penultima contraseña:        ', penultima64[1], '        ', penultima)
            opciones()
    else:
        print('                      Solo hay un Password Editado')
        opciones()

def opciones():
    print('')
    print('Pulsa: '
          ' A Para Generar -'
          ' B Para Buscar -'
          ' Q Para Salir')
    opcion = input('Elige la opción: ')
    opcion = opcion.lower()
    if len(opcion) < 1:
        print('Esa Opcion No es Correcta, Escribe Algo')
        opciones()
    if opcion == 'a':
        gen()
    if opcion == 'b':
        lectura()
    if opcion == 'q':
        print('Hasta Otra')
        exit()
    else:
        print('Esa Opcion No Existe')
        opciones()

opciones()