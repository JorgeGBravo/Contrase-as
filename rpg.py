from random import SystemRandom
import random
import string



longitud = 10

valores =  string.ascii_letters+string.digits
cryptogen = SystemRandom()
pss = ""

while longitud > 0:
    pss = pss + cryptogen.choice(valores)
    longitud = longitud - 1

print(pss)