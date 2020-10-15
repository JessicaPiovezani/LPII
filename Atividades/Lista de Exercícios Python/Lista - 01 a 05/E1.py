class Maioridade:

    def validacao(self, idade):

        if idade >= 18:
            print ("Essa pessoa é maior de idade!")

        else:
            print ("Essa pessoa não é maior de idade!")

class Notas:

    def caculo_de_media(self, n1, n2, n3):

        media = (n1+n2+n3) /3

        if media >= 7:
            print ("A média do aluno é de %.2f e ele está aprovado."%media)

        else:
            print("A média do aluno é de %.2f e ele está reprovado"%media)


maximoalunos=5

while maximoalunos != 0:
    idade = int (input("Digite a idade: "))
    nota1 = float (input("Digite a primeira nota: "))
    nota2 = float (input("Digite a segunda nota: "))
    nota3 = float (input("Digite a terceira nota: "))
    maximoalunos = maximoalunos-1
    print ("\n")

    validador_idade = Maioridade()
    validador_idade.validacao(idade)

    validador_media = Notas()
    validador_media.caculo_de_media(nota1, nota2, nota3)



