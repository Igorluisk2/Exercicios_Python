#Obj de converter metros em centimetros
'''m1= 1

cm= m1*100

print(cm)

print("Boas vindas")


boas vindas
pedir um numero para converter para centimetros
convertendo
exibir o calculo pronto
se for menor de 10 cm imprimir ("pequeninho") até 20cm ("suficiente") acima de 20 ("muito grande")
'''


#def metroToCentimetro():
print("Boas vindas ao conversor de medidas")
m = float(input("\nDigite o numero de metros que deseja converter para centímetros: "))
cm= m*100
print("Convertendo...")
print("O resultado foi: ",cm," cm")

if m <= 10:
     print ("Pequeninin")
elif m > 10 and m <= 20:
     print ("Suficiente")
elif m > 20:
     print ("Muito grande")