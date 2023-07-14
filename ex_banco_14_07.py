from ex_contabanco_14_07 import *

while True:
    op=int(input("1- Cadastro\n2- Depósito\n3- Saque\n4- Extrato\n"))
    if op==1:
        name=input("Digite seu nome: ")
        password=int(input("Digite sua senha de 4 digitos: "))
        c1=Contabanco(name,password)
    if op==2:
        valor=float(input("Depositar: "))
        senha=int(input("Digite o código PIN: "))
        c1.deposito(valor,senha)
    if op==3:
        valor=float(input("Sacar: "))
        senha=int(input("Digite o Código Pin: "))
        c1.saque(valor,senha)

    if op==4:
        senha=int(input("Digite o código PIN: "))
        c1.extrato(senha)