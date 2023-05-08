nome = input ("Nome do produto: ")
quant = float(input("Quantidade que ira comprar: "))
desc = float(input("Desconto: "))
valor = float(input("Valor do produto: "))
somaquant = (quant*valor)
soma = (somaquant * desc)/100

print("O Sr. comprou ",nome,",comprou",quant," o valor desses itens é",valor,", valor com desconto",soma,", valor dos itens pela quantidade",somaquant)