import time

letras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lista_m = []
traducao = []
escrever = True

print("Olá! \nLembre-se de digitar um número inteiro por linha")
while escrever == True:
    try:
        mensagem = int(input(": "))
        lista_m.append(mensagem)
        
        enviar = str(input("Enviar a mensagem agora? s - sim | n - nao "))
        if enviar == "s":
            escrever = False
        else:
            escrever = True
    except(ValueError):
        print("!!!!Você precisa digitar somente numeros!!!!")



num = len(lista_m)

print("\nTraduzindo...")
time.sleep(1)
for i in range(num):
    x = lista_m[i]
    y = letras[x]
    traducao.append(y)

print("\n")
print(''.join(traducao))