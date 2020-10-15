from BDO import Manipulacao

class Pessoa():
    def cadastro(self, cpf, nome, email):
        self.cpf = list(input("CPF: "))
        self.nome = list(input("Nome: "))
        self.email = list(input("E-mail: "))
        Tstring(cpf,nome,email)


#Classe para converter listas em strings e inserir no banco
class Tstring():
    def __init__(self, cpf, nome, email):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        cpf = ''.join(cpf)
        nome = ''.join(nome).upper()
        email = ''.join(email).upper()
        inserir = Manipulacao()
        return inserir.inserir(cpf,nome,email)