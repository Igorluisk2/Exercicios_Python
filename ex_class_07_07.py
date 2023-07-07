class Vendedor ():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas
    def vendeu (self,vendas):
        self.vendas = vendas 
        print(self.vendas)
