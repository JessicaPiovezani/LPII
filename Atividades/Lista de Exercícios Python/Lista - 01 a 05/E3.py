class Calculadora:

    def soma (self, numero1, numero2):
        resultado = numero1 + numero2 + 1
        print("O resultado com a adição do número 1 é:", resultado)
    
    def subtracao (self, numero1, numero2):
        resultado = numero1 - numero2 + 1
        print("O resultado com a adição do número 1 é:", resultado)
    
    def multiplicacao (self, numero1, numero2):
        resultado = numero1 * numero2 +1
        print("O resultado com a adição do número 1 é:", resultado)
    
    def divisao (self, numero1, numero2):
        resultado = numero1 / numero2+ 1
        print("O resultado com a adição do número 1 é:", resultado)

calculadora = Calculadora()
opcao = -1


while opcao != 0:
    numero1 = int (input("Digite o primeiro número: "))
    numero2 = int (input("Digite o segundo número: "))

    opcao = int (input("\nPara encerrar o programa digite 0\n\nEscolha uma operação básica: \n1- Soma \n2- Subtração\n3- Multiplicação\n4- Divisão\n"))
    
    if opcao == 1:
        calculadora.soma(numero1,numero2)
    
    if opcao == 2:
        calculadora.subtracao(numero1,numero2)

    if opcao == 3:
        calculadora.multiplicacao(numero1,numero2)

    if opcao == 4:
        calculadora.divisao(numero1,numero2)

print("Calculadora encerrada!")
