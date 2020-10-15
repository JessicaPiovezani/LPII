#Inicializando nota com -1 para ativar o looping do while
nota = -1

while nota < 0 or nota > 10:
    nota= float (input('Digite uma nota válida de 0 a 10: '))

print('Programa encerrado!')