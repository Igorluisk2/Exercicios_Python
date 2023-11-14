import mysql.connector

connect = mysql.connector.connect(
    
    host = "10.28.1.213",
    user = "suporte",
    password = "suporte",
    database = "deckshop"
    
)

class BancoD():
    def __init__(self):
        self.cursor = connect.cursor()
       
        
    # INSERT
    def insert_table(self, nome, quant):
        sql = "INSERT INTO produtos (nome, quantidade) VALUES (%s, %s)"
        val = (nome, quant)
        self.cursor.execute(sql, val)
        connect.commit()

    # SELECTS
    def select_table(self):
        self.cursor.execute("SELECT * FROM produtos")
        myresult = self.cursor.fetchall()
        for x in myresult:
            pass
        
    def select_id_table(self, id):
        comando = "SELECT nome FROM produtos WHERE id = %s"
        self.cursor.execute(comando, (id,))
        myresult = self.cursor.fetchall()
        for x in myresult:
            for self.i in x:
                pass
        
        comando = "SELECT quantidade FROM produtos WHERE id = %s"
        self.cursor.execute(comando, (id,))
        myresult = self.cursor.fetchall()
        for x in myresult:
            for self.a in x:
                pass
        
    # UPDATE
    def update_table(self, nome, quant, id_mudar):
        sql = "UPDATE produtos SET nome = %s, quantidade = %s WHERE id = %s"
        val = (nome, quant, id_mudar)
        self.cursor.execute(sql, val)
        connect.commit()

    # DELETE
    def delete(self, id):
        sql = "DELETE FROM produtos WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        connect.commit()
        