lista_numeros = []

for i in range(5):
    numeros = int (input("Digite um número para adicionar a lista: "))
    lista_numeros.append(numeros)

soma = sum(lista_numeros)
print("\nO maior elemento é:", max(lista_numeros))
print("A soma dos elementos é de:", soma)
ocorrencia = lista_numeros[0]
print("A quantidade de ocorrências do número %i é de %s" %(lista_numeros[0], lista_numeros.count(ocorrencia)))
print("A média dos elementos é de:", soma/len(lista_numeros))