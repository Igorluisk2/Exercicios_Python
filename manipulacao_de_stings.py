a = "igor luis"
b = "Luís"
c = "Segunda-Feira"
s = "Olá, mundo"
print(a.capitalize()) #deixa a primeira letra em maiusculo
print(a.casefold()) #deixa tudo em minisculo 
print(a.lower()) #deixa tudo em minusculo 
print(a.upper()) #deixa tudo em maiusculo
print(a.islower()) #testa se o texto é minusculo (boleana)
print(a.isupper()) #testa se o texto é maiusculo 
print(a.isdigit()) #testa se o texto é número
print(a.replace("luis","Teixeira")) #troca o primeiro texto pelo segundo
print(c.split("-")) #Divide 
print(a.find("luis")) #localiza da esq
print(a.rfind("luis")) #localiza da dir
print("luis" in a ) #testa se existe a palavra procurada (booleana)
print(a.count("i")) #conta quandos caracteres tem (independente de maiusculo e minusculo)
print(s[2]) #imprime somente a tecla da posição (sempre começa no 0)
print(s[0:3]) #imprime somente o espaço determinado entre [] se nada for determinado no inicio ele pega desde o começo
print(s[:3]) #msm coisa (quando não é declarado, pega desde o começo)
print(s[:]) #imprime tudo, já que não está declado o inicio e o final

#exercicios

txt = input("Digite um texto: ")
print(len(txt))
print(txt)
 #2
txt1 = input("Digite um texto1: ")
print(len(txt1))
print(txt1)

txt2 = input("Digite um texto1: ")
print(len(txt2))
print(txt2)
#3
nome = input("Digite seu nome: ")
print(nome[0:4])