from random import *
import operator

primeira_lista = []
segunda_lista = []

for i in range(6):
    primeira_lista.append(randrange(0,9))
    segunda_lista.append(randrange(0,9))

print(primeira_lista)
print(segunda_lista)
print (any(map(operator.eq,primeira_lista,segunda_lista)))