#1 eleição 
'''lnum=[]
lleila=[]
lnobre=[]
lmustafa=[]
lnumelei=[]

numelei=int(input("Quantos eleitores votarão? "))
lnumelei.append(numelei)

for i in range(numelei):
    lnum.append(int(input("voto: ")))
for x in lnum:
    if x==11:
        lleila.append(x)
for y in lnum:
    if y==14:
        lnobre.append(y)
for z in lnum:
    if z==99:
        lmustafa.append(z)

print("Total de votos de Leila Pereira: ",len(lleila) )
print("Total de votos de Paulo Nobre: ",len(lnobre))
print("Total de votos de Mustafá Contursi: ",len(lmustafa))
print("Total de votos foi de: ",len(lnum))'''

#2  programa que imprime uma folha de preço de 1 item ao 50 valendo 1,99 cada

'''for i in range (1,51):
    print("Número de produtos:",i,"Valor:",i*1.99)'''

#3 preço do pão informado pelo usuário

'''pp=float(input("Preço do pão: "))
for i in range(1,51):
    print("Pães:%.2f,Valor: %.2f"(i,i*pp))'''

#4 
maior=-1
menor=999999999999

for i in range (5):
    nAcidente = int (input("Digite o Nr Acidente = "))
    nVeiculos = int (input("Digite o Nr Veiculos = "))

    if nAcidente>maior:
        maior = nAcidente
        cidadedeMaior=i+1

    if nAcidente<menor:
        menor = nAcidente
        cidadedeMenor=i+1
    somaAcidente = somaAcidente + nAcidente
    if nAcidente<2000:
        menor