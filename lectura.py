import datetime
import sqlite3

d = datetime.datetime.today()

conn = sqlite3.connect('pass.sqlite')
cur = conn.cursor()

busqueda = input("Escribe tu búsqueda: ")

if not busqueda:
    print("Búsqueda Inválida")
    exit()

sentencia = "SELECT * FROM names WHERE serv LIKE ?;"
cur.execute(sentencia, ["%{}%".format(busqueda)])
row = cur.fetchone()
ultima = row

if ultima == None:
    print("No hay Ninguna Coincidencia en la Base de Datos")
    exit()

print('                                        PLATAFORMA                    PASSWORD')
print('')

print('Password en uso:                     ', ultima[:2],'          ', ultima[2:])
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

