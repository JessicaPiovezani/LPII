quantidade_numeros = 10
lista_numeros = []
soma = 0

while quantidade_numeros != 0:
    numero = int (input("Digite um número: "))
    lista_numeros.append(numero)
    soma = soma + numero
    quantidade_numeros = quantidade_numeros - 1

media = soma/10

print ("\n\n-> O menor número é:", min(lista_numeros))
print ("-> O maior número é:", max(lista_numeros))
print ("-> A soma dos número é:", soma)
print ("-> A média dos número é:", media)