import re
def phonemovil():
    while True:
        movilin = input('Movil')
        movilregx = re.compile(r'\d\d\d\d\d\d\d\d\d') # se puede cambiar por r'^\d{9}$'
        if len(movilin) != 9:
            print('No Valido')
            continue
        movil = movilregx.search(movilin)
        if movil == None:
            print('No Valido')
            continue
        else:
            print('OK:' + movil.group())
            return movil.group()

movil = phonemovil()
print(movil)