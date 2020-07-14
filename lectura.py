import sqlite3
import time
import datetime

d = datetime.datetime.today()

conn = sqlite3.connect('pass.sqlite')
cur = conn.cursor()

busqueda = input("Escribe tu búsqueda: ")

if not busqueda:
    print("Búsqueda inválida")
    exit()




sentencia = "SELECT * FROM names WHERE serv LIKE ?;"
cur.execute(sentencia, ["%{}%".format(busqueda)])
row = cur.fetchone()
ultima = row

if ultima == None:
    print("No hay ninguna coincidencia")
    exit()

print('                                      FECHA                    PASSWORD')
print('')

print('Password en uso:      ', ultima)
print('---------------------------------------------------------------------------------------')

sentencia2 = "SELECT ALL * FROM pass WHERE serv LIKE ?;"
cur.execute(sentencia2, ["%{}%".format(busqueda)])
encuentro = cur.fetchall()
psd2 = encuentro



if len(psd2) > 1:
    lista = list()
    for psd in psd2:
        lista.append(psd)
    lista.sort()
    penultima = lista[len(lista)-2]

    print('Penultima contraseña: ' , penultima)

else: print('                      Solo hay un Password en uso editada')
