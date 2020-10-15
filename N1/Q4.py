
'''Decorators são um padrão de projeto que permite alterar o comportamento de uma função, classe ou método, dinamicamente.
Isso significa que para alterar um comportamento, não é preciso fazer uso de subclasses ou alterar o código na função diretamente.
Ele também irá facilitar o reuso de código entre as aplicações.
No exemplo desse exercicio é criada uma função que mostra o tempo de execução de uma função que soma 4 números aleatórios.'''

import time
from random import *

#Exemplo de Decorators
class CalcularTempo():
    def __init__(self, f):
        #Os argumentos colocados no init serão executados antes do retorno da função que realizou a chamada.
        self.f = f

    #No método call a função original é alterada.
    def __call__(self, *args):
        inicio = time.time()
        self.f()
        fim = time.time()
        tempoTotal = fim - inicio
        print("O tempo de execução das somas foi de: %.8f" %tempoTotal + " segundos")

@CalcularTempo #Chamando o Decorator para fazer a alteração na função.
def numeros():
    numero1 = randrange(0,100)
    print("1º número:", numero1)
    numero2 = randrange(100,200)
    print("2º número:",numero2)
    numero3 = randrange(200,300)
    print("3º número:",numero3)
    numero4 = randrange(300,400)
    print("4º número:",numero4)
    soma = numero1 + numero2 + numero3 + numero4
    print("O resultado da soma dos números é:",soma)

numeros()