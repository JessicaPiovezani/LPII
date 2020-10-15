import psycopg2

class Conexao():
    def get_connection(self):
        conexao = psycopg2.connect(user="admin",password="1234", host="127.0.0.1", port="5432", database="LPII")
        return conexao