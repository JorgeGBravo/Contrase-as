import base64

file = open('output.txt')
data = file.read()
print(data)
numero = int(input('numero de veces: '))
for i in range(1, numero + 1):
    data = base64.b64decode(data)
    print(data)

''' Ojo fijarse en el texto a descifrar al final tendrá que tener '==' si no es así colocar seguidamente los dos iguales'''