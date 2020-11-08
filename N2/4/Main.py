from Pessoa import *
from Validadores import *

opcao = int(input("\n1 - Cadastrar\n2 - Editar\n3 - Remover\n4 - Consultar\nEscolha uma das opções acima: "))

if opcao == 1:
    Pessoa.cadastro()

elif opcao == 2:
    print("\n\nBusca de cadastro para edição")
    Pessoa.busca()
    Pessoa.edita()

elif opcao == 3:
    print("\n\nBusca de cadastro para remoção")
    Pessoa.busca()
    Pessoa.inativa()

elif opcao == 4:
    Pessoa.busca()
