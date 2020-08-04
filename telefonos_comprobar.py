movil = input('movil: ')

def phonenumber():
    if len(movil) != 9:
        return print('Numero no Valido cantidad')
    if movil == float:
        return print('Numero no Valido letra')
    for i in movil:
        if not movil[1].isdecimal():
            return print('No valido')
    else:
        print('Perfecto')


phonenumber()