#meia noite eu te conto
import secrets
import os 
a = "a"
sorteio = []
while a != '0':
    a = input("Digite algo para colocar no sorteador: ")
    sorteio.append(a)
    os.system("cls")

sorteio.pop(-1)
print(sorteio)
os.system("pause")
os.system("cls")
print(secrets.choice(sorteio))