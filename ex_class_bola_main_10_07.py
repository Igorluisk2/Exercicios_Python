from ex_class_bola_conta_10_07 import *

def Menu():
    while True:
        op = int(input("1 - Cadastro da bola\n2 - Trocar cor \n3 - Mostrar cor\n"))
        if op == 1:
            cor=input("Cor da bola: ")
            circunferencia=input("Tamanho da bola: ")
            material=input("Material da bola: ")
            print("Cadastro concluido")
            b1=Bola(cor,circunferencia,material)
            if op ==2:
                b1.trocar_cor()
            if op==3:
                b1.mostrar_cor()
Menu()