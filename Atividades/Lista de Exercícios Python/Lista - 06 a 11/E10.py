n1 = int (input("Digite a primeira nota: "))
n2 = int (input("Digite a segunda nota: "))
n3 = int (input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

if media >= 7:
    print ("\nSua média é %.2f, você está aprovado!" %media)
else:
    print ("\nSua média é %.2f, você está reprovado!" %media)