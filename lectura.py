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



#sentencia = "SELECT * FROM names WHERE serv LIKE ?;"
#cur.execute(sentencia, ["%{}%".format(busqueda)])
#row = cur.fetchone()
#psd = row[2]
#print(psd)

sentencia2 = "SELECT ALL * FROM pass WHERE serv LIKE ?;"
cur.execute(sentencia2, ["%{}%".format(busqueda)])
row2 = cur.fetchall()
psd2 = row2

lista = list()

for psd in psd2:
    lista.append(psd)
if len(lista) == 1:
    ultima = max(lista)
    orden = lista.sort()
    borult = lista.pop()
    penultima = None


    print('                                      FECHA                    PASSWORD')
    print('')
    print('Contraseña en uso:    ', ultima)
    print('---------------------------------------------------------------------------------------')
    print('Penultima contraseña: ', penultima)