#LISTA DE EXERCÍCIOS PYTHON

#1. Crie uma lista com 10 nomes e exiba-os no terminal utilizando a estrutura de repetição FOR. OBS: pule linha.

'''lista = []
#cont = []
for i in range(10):
    lista.append(input("Digite um item: "))
    
for itens in lista:
    print(itens) '''

#2. Crie uma lista com com 10 números e exiba a soma dos números no terminal utilizando a estrutura de repetição FOR.

'''
lista2 = []
for num in range (10):
    lista2.append(int(input("Digite um número: ")))
print(sum(lista2))'''

#3.Crie uma lista vazia, que será usado para fazer uma lista de supermercados, utilizando a estrutura FOR preencha a lista com 10 itens e imprima o resultado no terminal.

'''lista4 = []
for i in range(10):
    lista4.append(input("Digite um item: "))
    
for itens in lista4:
    print(itens) '''

#4. Crie uma lista vazia, que será usada para receber 10 números com a estrutura FOR apresente ao final o total de números negativos e positivos digitados pelo usuário.

'''lista4 = []
for i in range (10):
    lista4.append(int(input("Digite um número: ")))
for x in lista4:
    if x>0:
        print("Positivo: ",x)
for y in lista4:
    if y<0:
        print("Negativo: ",y)'''

#5. Faça um Script utilizando a estrutura de repetição FOR que imprima somente os números pares entre 100 e 50 e apresente em ordem decrescente.

'''cont = []
lcont = []
for cont in range(50, 101, 2):
    lcont.append(cont)
    lcont.sort()
for llcont in lcont:
    print(llcont,end=" ")'''



#6. Faça um Script para ler 10 números inteiros e apresentar o quadrado de cada número lido. Utilize a estrutura de repetição FOR.

'''for quant in range (10):
    print(f"{quant}^2 = {quant**2}")'''

#7. Faça um Script que solicite 10 números ao usuário e mostre o maior número digitado. Utilize a estrutura de repetição FOR.

num = []
for a in range(5):
    num.append(input("Digite um numero: "))
    som = max(num)
print(som)



#8. Crie duas listas vazias, na primeira solicite ao usuário para digitar 5 números e multiplique o numero digitado em cada posição por 5, em seguida armazene  o resultado na segunda lista, ao final apresente o resultado

num1 = []
num2 = []
soma = 0
cont = 0

for a in range(5):
    cont = cont + 1
    num1.append(int(input(f"Digite o {cont}º numero: ")))
    num2 = num1

for i in num2:

    soma = (i * i)
    num2 = [soma]
    print("Lista 2 é: ",soma)


#IMAGEM NO DOC