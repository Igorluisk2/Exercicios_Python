'''print("-- Resevartório de Água --")

altura=float(input(" Digite a altura (cm):"))
largura=float(input(" Digite a largura (cm): "))
comprimento=float(input(" Digite o comprimento (cm): "))
c_diario=float(input("Digite o valor do consumo médio diário(litros/dia)= "))

cap_total=((altura*largura*comprimento)/1000); #o resultado seria em cm3 por isso, dividimos por mil para passar de cm3 para litros
auton_reser=cap_total/c_diario

print("Capacidade do Reservatório= ",cap_total, "litros ")
print("Autonomia do reservatório= ",auton_reser," dias") #Agora, vamos classificar o consumo
if(auton_reser<2):
    print("Consumo Elevado")
elif(auton_reser>=2 and auton_reser<=7):
    print("Consumo Moderado")
else:
    print("\n Consumo Baixo")

#3
letra=input("Digite uma digite uma letra que direi se é vogal ou consoante: ")
letra=letra.casefold()
if letra == "a" or letra=="e" or  letra=="i" or letra=="o" or letra=="u" :
    print("É uma vogal")
else:
    print("É uma consoante")

#5
n1 = float(input("Digite a nota 1º: "))
n2 = float(input("Digite a nota do 2º: "))
media = (n1 + n2)/2
if media >= 7:
    print("Você foi aprovado.")
else:                                                         #respeitar a ordem
    print("Você foi reprovado.")
if media ==10:
    print("Distinção.")

#6 imprimir o numero mais alto na lista

n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))
lista=[n1,n2,n3]
print(max(lista))

#7 imprimir minimo e maximo

n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))
lista=[n1,n2,n3]
print(max(lista))           #maximo
print(min(lista))        #minimo

#8 3 produtos com nome e preço

p1 = input("Digite o nome do produto: ")
v1 = float(input("Digite o valor do 1º produto: "))
p2 = input("Digite o nome do produto: ")
v2 = float(input("Digite o valor do 2º produto: "))
p3 = input("Digite o nome do produto: ")
v3 = float(input("Digite o valor do 3º produto: "))

if v1 < v2 and v1 < v3:
    print(f"\nO produto mais barato é {p1}, valor: {v1}")
elif v2 < v3 and v2 < v3:
    print(f"\nO produto mais barato é {p2}, valor: {v2}")
else:
    print(f"\nO produto mais barato é {p3}, valor: {v3}")

#9 numeros em decrecente 

n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
n3=int(input("Digite o último numero: "))
vn=[n1,n2,n3]
vn.sort(reverse=True)
print(vn)'''

#10 bodia bonoite

turno1 = input("Digite a inicial do turno que você estuda: ")
turno1 = turno1.casefold()

if turno1 == "m":
    print("Bom dia!")
elif turno1 == "t":
    print("Boa noite!")
elif turno1 == "n":
    print("Boa noite!")
else:
    print("Valor inválido")