class Carrinho_De_compras():
    
    def __init__(self, produtos):
        self.produtos = []
        
    def inserir_produtos(self,produto: str):
        self.produtos.append(produto)
        
    def lista_produto(self):
        for i in self.produtos:
            print(i.nome, i.valor)
            
    def soma_total(self):
        for prod in self.produtos:
            soma = prod.valor + prod.valor
            print(f"{prod.valor}+{prod.valor}")
            print(soma)
        

class Produto():
    
    def __init__(self,nome: str, valor:float) -> None:
        self.nome = nome
        self.valor = valor
        
        
prod = Produto ("maça",1.99)

car_compr = Carrinho_De_compras()
car_compr.inserir_produtos(prod)
car_compr.lista_produto()
car_compr.soma_total()