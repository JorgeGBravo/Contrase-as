import re
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

movil = phonemovil()
print(movil)