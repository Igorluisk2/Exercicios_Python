#1 pela numeros inteiros, calcule e mostre a quantidadew de números pares e impares
'''par = []
impar = []
for x in range(10):
    num=int(input("Digite um valor inteiro: "))
    if num%2==0:
        par.append(num)
    elif num%2!=0:
        impar.append(num)
    else:
        ("Número invalido, tente novamente!")
print (f"Números impares: {len(impar)}\nNúmeros pares: {len(par)}")'''

#2 O dp estadual de meterologia lhe contratou para desenvolver um programa que leia um conjunto indeterminado de temperatura
#bem como o mes e o ano que ocorreu essa temperatura, imprimir no final a menor e a maior temperatura informada,
#imprimir o mes e o ano em que a temperatura aconteceu
#imprimir a média de todas as temperaturas
#se o usuario apertar x, ele sai do programa
print("="*120)
lista_temp=[]
lista_mes=[]
lista_ano=[]
soma=0
cont=0
while True:
    temp=(input("\nDigite a temperatura ou digite X para sair: "))
    if temp=='x' or temp=='X':
        print("Obrigado por usar nosso programa! Saindo...")
        break
    mes=int(input("Digite o mês em que essa temperatura ocorreu: "))
    ano=int(input("Digite o ano em que ocorreu: "))
    cont=cont+1

    temp=float(temp) #transforma a string em float 
    lista_temp.append(temp)
    lista_mes.append(mes)
    lista_ano.append(ano)
    soma=soma+temp
    media=soma/cont

    if lista_temp!=0:
        print("\nA menor temperatura é ",min(lista_temp))
        x=min(lista_temp)
        z=lista_temp.index(x)
        print("O mês que ocorreu: ",lista_mes[z])
        print("O ano que ocorreu: ",lista_ano[z])
        print("\n")
        y=max(lista_temp)
        w=lista_temp.index(y)
        print("A maior temperatura: ",max(lista_temp))
        print("O mês que ocorreu: ",lista_mes[w])
        print("O ano que ocorreu: ",lista_ano[w])
        print("A media das temperaturas: ",media)
print("\n="*120)
