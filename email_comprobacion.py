import re

def emailcomprobe():
    while True:
        email = input('Introducir Email: ')
        emailregx = re.compile(r'[\w.-]+@[\w.-]+\.[\w+]' , re.VERBOSE)
        correo = emailregx.search(email)
        print(correo)
        if correo == None:
            print('No Valido')
            continue
        else:
            print('Ok...' , email)
            return email




email = emailcomprobe()
print(email)