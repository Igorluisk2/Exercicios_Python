from ex_class_conta_10_07 import *
while True:
    op = int(input("1 Para cadastro:\n2 Para extrato\n3 Para depósito\n4 Para saque\n:"))
    if op == 0:
            break
    if op == 1:
        print("Cadastre-se")
        agencia1 = input("Agência: ")
        nome1 = input("Nome: ")
        conta2 = input("Conta: ")
        fone1 = input("Fone: ")
        cpf1 = input("CPF: ")
        conta1=Conta(agencia1,nome1,conta2,fone1,cpf1)
        print("Cadastro realizado!")
    elif op == 2:
        saque1=int(input("Valor do saque: "))
        conta1.sacar(saque1)
    elif op == 3:
        depo=int(input("Valor do depósito: "))
        conta1.depositar(depo)
    elif op == 4:
        conta1.extrato()