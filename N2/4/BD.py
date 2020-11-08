#Importação de biblioteca para maniplação de dados no PostgreeSQL
import psycopg2

class Conexao():
    #Estabelecendo conexão com banco de dados
    def get_connection(self):
        conexao = psycopg2.connect(user="postgres",password="1234", host="127.0.0.1", port="5432", database="prova")
        cursor = conexao.cursor()
        #Se a tabela não existir ela será criada
        cria_tabela = "CREATE TABLE IF NOT EXISTS pessoas (id serial primary key, cpf varchar(14) not null, nome varchar(150) not null, email varchar(400) not null, status integer default 1)"
        cursor.execute(cria_tabela)
        conexao.commit()
        return conexao