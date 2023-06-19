'''def hello ():
    print("Olá!!!")
hello()


def hallo(nome):
    print("Olá",nome)
hallo("Igor")

def hallou (nomee,idade):
    print("Olá",nomee,'\nSua idade é:',idade)
hallou("Ederson",27)'''

#como calcular salario

'''def calcular_pagamento(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas <=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    print(salario)
calcular_pagamento(10,20)'''

'''def soma(x,y):
    result=x+y
    return result

a=int(input("Primeiro numero: "))
b=int(input("Segundo numero: "))
res=soma(a,b) #atribua uma variavel
print("Soma:",res)'''

'''def inverte(nome,sobrenome):
    nomeInverso=sobrenome+","+nome
    return nomeInverso
nome=input("Nome: ")
sobrenome=input("Sobrenome: ")
invertido=inverte(nome,sobrenome)
print("Olá",invertido)'''

#par e impar
'''def par(x):
    if(x%2)==0:
        return True
    else:
        return False
    
while True:
    num=int(input("Insira um número: "))
    if par(num):
        print("É par")
    else:
        print("É impar")'''

#cadastro
'''def cadastro():
    name=input("Qual seu nome: ")
    age=int(input("Idade: "))
    return name,age

print("Iniciando o cadastro...")
nome,idade=cadastro()
print("Cadastro realizado com sucesso: ")
print("Seu nome é",nome,"E você tem",idade,",anos de idade")'''

#1 faça um programa com uma função que necessite de três argumentos e que forneça a soma desses três argumentos
'''def soma():
    n1=int(input("Valor 1: "))
    n2=int(input("Valor 2: "))
    n3=int(input("Valor 3: "))
    return  n1,n2,n3
print("Fazendo conta...")
val1,val2,val3=soma()
result=val1+val2+val3
print("Conta feita")
print(F"{val1}+{val2}+{val3} = {result}")'''

#2 faça um programa com a função que necessite de um argumento. A função retorna o valor de caractere "P",
#se seu argumento for positivo, e "N", se seu argumento negativo ou "Zero" se o numero for 0

def parimparzero():
    try:
        num=int(input("Digite o valor e eu te direi se é par, impar ou 0: "))
        if num>0:
            print("Fazendo a conta, aguarde...")
            print("Positivo")
        elif num <0:
            print("Fazendo a conta, aguarde...")
            print("Negativo")
        else:
            print("Fazendo a conta, aguarde...")
            print("Zero")
    except:
        print("Valor inválido, tente novamente")
while True:
    parimparzero()
