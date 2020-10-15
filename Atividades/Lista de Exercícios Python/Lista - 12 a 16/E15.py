lista_numeros = []

for i in range(10):
    numero = int (input("Digite um número: "))
    lista_numeros.append(numero)

print("\nO maior número da lista é", max(lista_numeros))