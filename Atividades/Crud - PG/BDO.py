import psycopg2
from BD import Conexao

class Manipulacao():

    #Inserção de cadastro
    def inserir(self, cpf, nome, email):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            inserir = """insert into pessoas (cpf, nome, email) values ('{0}','{1}','{2}')""".format(cpf, nome, email)
            cursor.execute(inserir)
            conexao.commit()
            print("Cadastro inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca de todos os cadastros
    def busca(self):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas"
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                status = i[3]
                if status == 1:
                    cadastro = "Ativo"
                else:
                    cadastro = "Inativo"
                print ("Status: %s\n" %cadastro)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca de cadastros Ativos
    def abusca(self):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where status = 1"
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                print ("Status: Ativo\n")
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    #Busca de cadastros Inativos
    def ibusca(self):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where status = 0"
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                print ("Status: Inativo\n")
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    #Busca por nome
    def busca_nome(self, nome):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where nome like '%{0}%'".format(nome)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                status = i[3]
                if status == 1:
                    cadastro = "Ativo"
                else:
                    cadastro = "Inativo"
                print ("Status: %s\n" %cadastro)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca por e-mail
    def busca_email(self, email):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where email like '%{0}%'".format(email)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                status = i[3]
                if status == 1:
                    cadastro = "Ativo"
                else:
                    cadastro = "Inativo"
                print ("Status: %s\n" %cadastro)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()
    
    #Busca por CPF
    def busca_email(self, cpf):
        try:
            conexao = Conexao().get_connection()
            cursor = conexao.cursor()
            busca = "select * from pessoas where cpf like '%{0}%'".format(cpf)
            cursor.execute(busca)
            pessoas = cursor.fetchall()
            for i in pessoas:
                print ("Nome: ", i[1])
                print ("CPF: ", i[0])
                print ("E-mail: ", i[2])
                status = i[3]
                if status == 1:
                    cadastro = "Ativo"
                else:
                    cadastro = "Inativo"
                print ("Status: %s\n" %cadastro)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Oppss! Algum erro aconteceu :/", error)
        
        finally:
            if (conexao):
                cursor.close()
                conexao.close()