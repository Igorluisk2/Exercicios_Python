#3
'''a = 1
n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
for b in range(n1,n2+1):
    for b1 in range(a):       
        print(b,"+",a,"=",b+a)
    
#4

nun1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))
for p1 in range (nun1,num2+1):
    print(p1,end=" ")
#5 media se 5 informando a soma e a media 
cont=0
nu1=int(input("Digite o primeiro numero: "))
nu2=int(input("Digite o segundo  numero: "))
nu3=int(input("Digite o terceiro numero: "))
nu4=int(input("Digite o quarto numero: "))
nu5=int(input("Digite o quinto numero: "))
li = [nu1,nu2,nu3,nu4,nu5]
for f in range (1):
    print(sum(li)/5)

#5

menor = 0
maior = 0
while True:
    

    di = str(input("Digite um numero: "))


    if di == 'x':
        soma = maior+menor
        print("soma:",soma)
        break

    di = int(di)

    if di < maior:
        menor = di  
        print("menor:",menor) 

    elif di > menor:
        maior = di
        print("maior: ",maior)'''

#6

listade=[]
cont = -1
while True:
    idade = int(input("Digite 0 para parar\nDigite sua idade: "))
    listade.append(idade)
    soma = sum(listade)
    cont = (cont + 1) 
    print(f"Na sua turma tem {cont+1} pessoas")

    if idade == 0:
        som = (soma/cont)
        print(som)
        if som > 0 and som <=25:
            print("A sua turma é jovem")
            break
        elif som >= 26 and som < 60:
            print("A sia turma é adulta.")
            break
        else:
            print("A sua turma é idosa.")
            break