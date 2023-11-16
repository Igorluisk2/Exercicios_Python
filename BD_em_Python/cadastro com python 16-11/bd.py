import mysql.connector

connect = mysql.connector.connect(
    
    host = "10.28.1.213",
    user = "suporte",
    password = "suporte",
    database = "dcadastro2"
    
)

class BancoDados():
    def __init__(self):
        self.cursor = connect.cursor()
       
        
    # INSERT
    def insert_cadastro(self,nome,sobrenome,cpf,rg,telefone,sexo,cep,cnh,estado_civil,endereco):
        try:
            sql = "INSERT INTO cadastro (nome, sobrenome, cpf, rg, telefone, sexo, cep, cnh, estado_civil, endereco) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (nome, sobrenome,cpf,rg,telefone,sexo,cep,cnh,estado_civil,endereco)
            self.cursor.execute(sql, val)
            connect.commit()
            print(self.cursor.rowcount, "registro inserido.")
        
        except:
            print("Todos os campos devem estar preenchidos")
        