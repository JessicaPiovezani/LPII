import time

#Definindo a lista de caracteres para tradução
letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Definindo uma lista para armazenar a mensagem digitada
lista_m = []

#Definindo uma lista para armazenar a tradução
traducao = []

#Inicializando o escrever com True para entrar no looping do menu
escrever = True

print("Olá! \nLembre-se de digitar um número inteiro por linha")

#Looping do menu principal
while escrever == True:
    try:
        mensagem = int(input(": "))

        #Por motivos de segurança das mensagens, caso o usuário digite um número que não possa ser traduzido um espaço será adicionado no seu lugar
        #Se fosse colocada uma mensagem de erro poderia ser facilitado o entendimento de como funciona a linguagem secreta.
        if mensagem > 27 or mensagem < 0:
            mensagem = 0
            lista_m.append(mensagem)
        lista_m.append(mensagem)
        enviar = str(input("Enviar a mensagem agora? S - Sim | N - Não ")).upper()
        if enviar == "S":
            escrever = False
        else:
            escrever = True
    except(ValueError):
        print("!!!!Você precisa digitar somente numeros!!!!")


#Verificando o tamanho da lista mensagem para colocar no looping for da tradução
num = len(lista_m)

print("\nTraduzindo...")
time.sleep(1)

#Looping da tradução, onde a cada rodada o x armazena o número digitado e y o coloca como índice 
# da lista de letras fazendo a busca da sua tradução e inserindo na lista de tradução.
for i in range(num):
        x = lista_m[i]
        y = letras[x]
        traducao.append(y)

print("Mensagem traduzida:")
print(''.join(traducao))