from random import *

primeira_lista = []
segunda_lista = []

for i in range(5):
    primeira_lista.append(randrange(0,9))
    segunda_lista.append(randrange(0,9))

print (primeira_lista)
print (segunda_lista)

print("\nUnião das listas:", set(primeira_lista).union(segunda_lista))

print("Intercalação das listas: ")
for i in range(5):
    print(primeira_lista[i],segunda_lista[i])
