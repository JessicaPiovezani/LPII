from random import *

primeira_lista = []
segunda_lista = []

for i in range(6):
    primeira_lista.append(randrange(0,9))
    segunda_lista.append(randrange(0,9))

print(primeira_lista)
print(primeira_lista[3:6])
print(segunda_lista)
print(segunda_lista[3:6])