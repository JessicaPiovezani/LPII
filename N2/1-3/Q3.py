from BD import MongoConexao
from pymongo import MongoClient

class ManipulacaoMongo():

    #Inserção de dados
    def inserir(self, nome, autor, genero):
        
        #Estabelece conexão com o Banco de Dados
        conexao = MongoConexao()

        #Insere os dados na collection
        inserir = {'nome' : nome, 'autor' : autor, 'genero' : genero}
        conexao.connection(inserir)
        print("MongoDB: Cadastro inserido com sucesso!")