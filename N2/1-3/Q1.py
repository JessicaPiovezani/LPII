import psycopg2
from BD import PGConexao

class ManipulacaoPG():

    #Inserção de dados
    def inserir(self, nome, autor, genero):
        
        try:
            #Estabelece conexão com o Banco de Dados
            conexao = PGConexao().get_connection()
            cursor = conexao.cursor()

            #Insere os dados na tabela musica
            inserir = """insert into musica (nome, autor, genero) values ('{0}','{1}','{2}')""".format(nome, autor, genero)
            cursor.execute(inserir)
            conexao.commit()
            print("PostgreSQL: Cadastro inserido com sucesso!")

        except (Exception, psycopg2.DatabaseError) as error:
            print("PostgreSQL: Oppss! Algum erro aconteceu :/", error)
        
        finally:
            #Ao final encerra a conexão com o banco
            if (conexao):
                cursor.close()
                conexao.close()