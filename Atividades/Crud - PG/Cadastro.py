from BDO import Manipulacao
from Validadores import *

class Pessoa():
    def cadastro(self, cpf, nome, email):
        self.cpf = False
        #Looping de solicitação e validação de CPF
        while cpf == False:
            numero_cpf = list(input('CPF: '))
            numero_cpf = ''.join(numero_cpf)
            validador_cpf = ValidadorCPF(numero_cpf)
            if validador_cpf.validador():
                cpf = True
            else:
                print("CPF inválido!")
                cpf = False

        self.nome = False
        #Looping de solicitação e validação de nome
        while nome == False:
            nome = list(input("Nome: "))
            nome = ''.join(nome).upper()
            validador_nome = ValidadorNome()
            if validador_nome.validador(nome):
                nome = True
            else:
                print("Nome inválido")
                nome = False

        self.email = False
        #Looping de solicitação e validação de e-mail
        while email == False:
            email = list(input("E-mail: "))
            email = ''.join(email).upper()
            validador_email = ValidadorEmail()
            if validador_email.validador(email):
                email = True
            else:
                print("E-mail inválido")
                email = False

        inserir = Manipulacao()
        return inserir.inserir(cpf,nome,email)
