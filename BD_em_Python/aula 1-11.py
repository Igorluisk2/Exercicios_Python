import mysql.connector

con=mysql.connector.connect(
    host="10.28.1.213",
    database= "hubinnovation",
    user="suporte",
    password="suporte"

)

if con.is_connected():
    db_info=con.get_server_info()
    print("Conectado ao banco de dados = ", db_info)
     

'''comando="insert into cadastro values(49,'kelly','lly@hotmail.com',67992913452,1234567890,'1994-04-24','Feminino',4);"    
cursor=con.cursor()
cursor.execute(comando)
con.commit()
'''

commando = "update cadastro set nome = 'Ederson' where cpf =1234567890;"
cursor=con.cursor()
cursor.execute(commando)
con.commit()



commando = "delete from cadastro where cpf =1234567890; "
cursor=con.cursor()
cursor.execute(commando)
con.commit()



consulta_sql = "select * from cadastro"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("Numero total de registros retornados: ", cursor.rowcount)

print("Mostrando os registros")
for linha in linhas:
    print("Id Autor = ", linha[0])
    print("Nome Autor = ", linha[1])
    print("Sobrenome Autor = ", linha[2])






if con.is_connected():
    cursor.close() #ainda n chamamos o cursor
    con.close()
    print("conexão encerrada")