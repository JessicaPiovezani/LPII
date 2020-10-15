
class Operacoes:
    #Busca da maior quantidade de presos
    def qndMaior(self, qndPresos):
        maior = qndPresos[0]
        for i in qndPresos:
            if i > maior:
                maior = i
        return print("O maior número é:", maior)

    #Busca da menor quantidade de presos
    def qndMenor(self, qndPresos):
        menor = qndPresos[0]
        for j in qndPresos:
            if j < menor:
                menor = j
        return print("O menor número é:", menor)

    #Calculo da média de presos
    def mediaPresos(self, qndPresos):
        qndTotalPresos = 0.0
        for k in qndPresos:
            qndTotalPresos += k
        qndMediaPresos = qndTotalPresos / len(qndPresos)
        
        print ("A quantidade média de presos é de: %.2f" %qndMediaPresos)
        
        #Busca de número de presos mais próximas a média calculada
        valorProximo = {valor: abs(valor - qndMediaPresos) for valor in qndPresos}
        return print("A quantidade mais próxima da média de presos é de:",min(valorProximo, key=valorProximo.get))
           


#Inicializando o inserir com True para entrar no looping de pesquisa
inserir = True

#Inicializando lista de presos vazia
qndPresos = []

#Menu de repetição para inserção de nomes
while inserir == True:
    try:
        numero = int(input("Qual o número de presos do mês? "))
        qndPresos.append(numero)

        pergunta = str(input("Deseja informar mais números? N - Não  | S - Sim ")).upper()

        if pergunta == "N":
            inserir = False
    
    except ValueError:
        print("Você precisa digitar números inteiros.")

#Instanciando a classe para poder utilizar as funções
operacoes = Operacoes()

#Exibindo lista original da maneira que foi inserida
print("\nA lista de presos inseridos é a seguinte: \n", qndPresos)

operacoes.qndMaior(qndPresos)
operacoes.qndMenor(qndPresos)
operacoes.mediaPresos(qndPresos)