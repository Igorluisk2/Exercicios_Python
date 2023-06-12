#1
num = float(input("Digite o 1º numero: "))
num1 = float(input("Digite o 2º numero: "))
some = (num+num1)
print (some)

#2
for par in range(0,100,2):
    print(par)
#3
for impar in range(1,100,2):
    print(impar)
#4
try:
    num2 = int(input("Digite o 1º numero: "))
    num3 = int(input("Digite o 2º numero: "))
    soma1=(num2/num3)
    print(soma1)
except:
    print("Use somente numeros")
#5
a=str(input("Cadastro x\n cadastro y\n cadastro z \n: "))

#6
while True:
    try:
        a=int(input("v1: "))
        b=int(input("v2: "))
        result=a/b
        print(result)
        continue
    except:
        print("Erro, tente novamente")
        continue