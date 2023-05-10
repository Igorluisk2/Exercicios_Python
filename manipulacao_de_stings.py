'''String  (%s)
inteiro (%d)
boleano (%b)
Float   (%f)
a = "igor luis"
b = "Luís"
c = "Segunda-Feira"
s = "Olá, mundo"
print(a.capitalize()) #deixa a primeira letra em maiusculo
print(a.casefold()) #deixa tudo em minisculo 
print(a.lower()) #deixa tudo em minusculo 
print(a.upper()) #deixa tudo em maiusculo
print(a.islower()) #testa se o texto é minusculo (boleana)
print(a.isupper()) #testa se o texto é maiusculo 
print(a.isdigit()) #testa se o texto é número
print(a.replace("luis","Teixeira")) #troca o primeiro texto pelo segundo
print(c.split("-")) #Divide 
print(a.find("luis")) #localiza da esq
print(a.rfind("luis")) #localiza da dir
print("luis" in a ) #testa se existe a palavra procurada (booleana)
print(a.count("i")) #conta quandos caracteres tem
print(s[2]) #imprime somente a tecla da posição (sempre começa no 0)
print(s[0:3]) #imprime somente o espaço determinado entre [] se nada for determinado no inicio ele pega desde o começo
print(s[:3]) #msm coisa (quando não é declarado, pega desde o começo)
print(s[:]) #imprime tudo, já que não está declarado o inicio e o final

#exercicios

txt = input("Digite um texto: ")
print(len(txt))
print(txt)
 #2
txt1 = input("Digite um texto1: ")
print(len(txt1))
print(txt1)

txt2 = input("Digite um texto1: ")
print(len(txt2))
print(txt2)
#3
nome = input("Digite seu nome: ")
print(nome[0:4])
#5
nome = input("Digite seu nome: ")
print (nome.capitalize())
#6
nome = input("Digite seu nome: ")
print (nome.upper())
#7
nome = input("Digite seu nome: ")
print(nome[0:9])
#8
nome = input("Digite seu nome: ")
print(nome.count("i"))
#9
num = float(input("Digite um numero: "))
print("Seu numero foi %.2f "%num)
#10
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
soma = (num1+num2)
print("A soma dos numeros digitados foi: %s"%soma)
#11
nome = input("\nDigite seu nome: ")
serie = int(input("\nDigite sua série: "))
escola = input("\nDigite sua escola: ")
cidade = input("\nDigite sua cidade: ")
n1 = float(input("\nDigite a nota da primeira prova: "))
n2 = float(input("\nDigite a nota da segunda prova: "))
n3 = float(input("\nDigite a nota da terceira prova: "))
n4 = float(input("\nDigite a nota da quarta prova: "))
media = ((n1+n2+n3+n4)/4) 
print("\nSeu nome é %s, e sua série é %d, o nome de sua escola %s, e você mora em %s, a sua média é %.1f"% (nome,serie,escola,cidade,media))
#13
raio=float(input("Digite o raio do círculo: "))
area= 3.14* (raio**2)
print("A área é : ",area)
#14
quad = float(input("Digite o lado: "))
soma = quad ** 2
dobro = soma * 2
print("A área do quadrado é %.2f,e o dobro da area do quadrdado é %.2f"%(soma,dobro))
#15
salariohora=float(input("Quanto você ganha por hora: "))
horames=float(input("Quantas horas você trabalha no mês: "))
salariomes=salariohora*horames
print("Você recebeu %.0f reais por hora e trabalhou %.0f horas nesse mes, seu salário esse mês será de %.4s"%(salariohora,horames,salariomes))'''
#
inteiro = int(input("Digite um numero inteiro 1º: " ))
inteiro1 = int(input("Digite um numero inteiro 2º: "))
real = float(input("Digite um numero quebrado/real: "))
print ("o 1º é %d,e o 2º é %d, o numero quadrado/real é %f"% (inteiro, inteiro1,real))