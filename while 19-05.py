'''while True:
    print("Loop Infinito\n")
    break

while True:
    valor=int(input("Digite o valor 1 ou 0 para encerrar: "))
    if valor==1:
        print("Valor correto")
    else:
        print("Valor para sair")
        break'''

cont = 101

while cont <= 101:
    cont = cont - 1
    print(cont)
    if cont == 0:
        break