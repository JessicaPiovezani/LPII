import psycopg2

class Conexao():
    #Estabelecendo conexão com banco de dados
    def get_connection(self):
        conexao = psycopg2.connect(user="postgres",password="1234", host="127.0.0.1", port="5432", database="LPII")
        return conexao