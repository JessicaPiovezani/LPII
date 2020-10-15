#Criando a classe Funcionário
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0
    
    def aumentaSalario(self):
        self.salario = self.salario + self.aumento

#Criando a subclasse Analista
class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20

#Criando a subclasse Programador
class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

#Classe criada para realizar os testes com os mesmos valores passados posteriormente
class Testes(Analista, Programador):
    def __init__(self, nome, idade, salario):
        Analista.__init__(self, nome, idade, salario)
        print("Nome do Analista: ", self.nome)
        print("Idade: ", self.idade)
        print("Salario atual: ", self.salario)
        self.aumentaSalario()
        print("Salário pós aumento: ", self.salario)
        
        print("\n")

        Programador.__init__(self, nome, idade, salario)
        print("Nome do Programador: ", self.nome)
        print("Idade: ", self.idade)
        print("Salario atual: ", self.salario)
        self.aumentaSalario()
        print("Salário pós aumento: ", self.salario)

#Passando valores para o teste
Testes("Jessica", 20, 3500)

