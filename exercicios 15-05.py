#exercicios dia 15/02

#1
'''t = [[1,2],[3],[4,5,6]]
print(t)
a = t[0]+t[1]+t[2]
print(sum(a))
#3
t = [1,2,3,4]
print(t[1:3])
#outra forma abaixo
t = [1,2,3,4]
print(t[1:3]) #ele esta printando a lista sem um numero mas n tera na list
del t[0] #apaga o numero escolhido
del t[2] #msm coisa
print(t)
#if
#loja de bebidas
print("Loja de birita, somente maiores podem comprar aqui.")
idade = int(input("digite sua idade: "))
print(idade)
if idade >= 18:
    print("Bora tomar umas!")
else:
    print("Hoje não bb")

a = int(input("Digite sua idade2: ")) #Exemplo do slide do prof
if a == 16:
    print("Pode Votar")   # ----
else:
    if a >= 16:
        print("Pode Dirigir")  # ----
    else:
        if a <16: 
            print("Apenas Estude")  # -------

b = int(input("Digite sua idade2: ")) #Exemplo do slide do prof
if b >= 16 and b <= 18:
    print("Pode Votar")
elif b <16:
    print("Apenas estude")
else:
    print("Pode Digirir se tiver CNH")

#exercicios if
#1
print("Digite dois numeros: ")
num1= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
if num1>num2:
    print(num1)
else:
    print(num2)
#ou
num1= int(input("Digite um numero: "))
num2= int(input("Digite um numero: "))
if num1> num2:
    print(f"O numero {num1} é maior que {num2}")
elif num2>num1:
    print(f"O numero {num2} é maior que {num1}")
else:
    print("Os numeros são identicos! Tente com numeros diferentes!")

p = int(input("Digite um número"))
if p > 0:
    print("O numero é positivo.")
elif p <0:
    print("O numero é negativo")
else:
    print("O numeor digitado é neutro")
# ex. media art
n1 = float(input("Digite a nota 1º: "))
n2 = float(input("Digite a nota do 2º: "))
media = (n1 + n2)/2
if media >= 7:
    print("Você foi aprovado.")
elif media >=5 and media <=6.99:
    print("Você esta de recuperação.")
else:
    print("Você foi reprovado.")
#
sal1=float(input("Digite o seu salário atual: "))
if sal1<500:
    ajuste=sal1*15/100
    print("O seu novo salário é de",sal1+ajuste,"\nseu salário era de ",sal1,"\nseu aumento foi de" ,ajuste)
elif sal1 >= 500 and sal1<1000:
    ajuste=sal1*10/100
    print("O seu novo salário é de",sal1+ajuste,"\nseu salário era de ",sal1,"\nseu aumento foi de" ,ajuste)
else:
    ajuste=sal1*5/100
    print("O seu novo salário é de",sal1+ajuste,"\nseu salário era de ",sal1,"\nseu aumento foi de" ,ajuste)'''

#
z = input("Digite a primeira letra do seu sexo: ")

if z == "m" :
    print("Seu sexo é masculino.")
elif z == "f" :
    print("Seu sexo é feminino.")
elif z == "o" :
    print("Só tem benino ou benina, se decide ae.")
else:
    print("Erro, digite apenas a inicial do seu sexo.") 
