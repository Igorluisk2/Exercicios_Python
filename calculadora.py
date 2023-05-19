'''print("*",70*"-","*")
print("|",70*" ","|")
print(("|"+13*" "+"Bem Vindo a Calculadora!                      "+13*" "+"|")) # seja bem vindo
print("|",70*" ","|")
print("*",70*"-","*")

print()

print("* ",70*"="," *\n")
print(("|"+37*" "+" "+36*" "+"|\n")*5)  # aqui tem que mostrar o calulo 
print("* ",70*"="," *")

print()

print("* ",68*"="," *\n")
print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*5)
print("* ",68*"-"," *")
print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*5) # aqui vai ser os numeros e os numeros etc
print("* ",68*"-"," *")
print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*5)
print("* ",68*"-"," *")
print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*5)
print("* ",68*"-"," *")
print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*5)
print("* ",68*"="," *")'''

print("\n\n\n====================================================")
print("=== BEM VINDO A PIOR CALCULADORA DA FÁBRICA 108 ====")
print("====================================================")
menu = 55555555555555555555555555
while menu !=1999:
    menu=int(input("\n0-Encerrar Progama\n1-Multiplicação\n2-Divisão\n3-Adição\n4-Subtração\n5-Volume de um cubo\n6-Exponenciação\n7-Raiz Quadrada\n8-Área de um quadrado\n9-Média de 4 notas\n10-Fatorial\n\nEscolha sua operação: "))
    if menu==0: #encerra o programa
        print("Programa encerrado")
        break
    if menu==1: #multiplicador
        print("\nBem vindo à MULTIPLICAÇÃO, escolha seus valores")
        num1=int(input("Valor 1: "))
        num2=int(input("Valor 2: "))
        result=num1*num2
        print(f"{num1} X {num2} = {result}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==2: #divisor
        print("\nBem vindo à DIVISÃO, escolha seus valores")
        num1=int(input("Valor 1: "))
        num2=int(input("Valor 2: "))
        result=num1/num2
        print(f"{num1} / {num2} = {result}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==3: #somador
        print("\nBem vindo à ADIÇÃO, escolha seus valores")
        num1=int(input("Valor 1: "))
        num2=int(input("Valor 2: "))
        result=num1+num2
        print(f"{num1} + {num2} = {result}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==4: #subtrair
        print("\nBem vindo à SUBTRAÇÃO, escolha os valores")
        num1=int(input("Valor 1: "))
        num2=int(input("Valor 2: "))
        result=num1-num2
        print(f"{num1} - {num2} = {result}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==5: #volume em cubo
        print("\nBem vindo ao cálculo do volume de um cubo")
        arestas=(int(input("Digite o tamanho das arestas: ")))
        volume=arestas*arestas*arestas
        print(f"O volume do cubo é de {volume}m³")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==6: #exponenciação
        print("\nBem vindo à EXPONENCIAÇÃO")
        base=int(input("Digite a base: "))
        expo=int(input("Digite o expoente: "))
        result=base**expo
        print(f"A exponenciação é de {result}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==7: #raiz quadrada
        print("\nBem vindo à RAIZ QUADRADA")
        num1=int(input("Digite o valor: "))
        raiz=num1**(1/2)
        print(f"A raiz quadrada de {num1} é {raiz}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==8: #área de um quadrado
        print("\nBem vindo ao cálculo da AREÁ DE UM QUADRADO")
        lado=int(input("Digite o tamanho do lado: "))
        area=lado*lado
        print(f"A área do quadrado com lados de {lado}m é de {area}m")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==9: #media
        print("\nBem vindo à MEDIA DE 4 NOTAS")
        nota1=int(input("Digite a Nota 1: "))
        nota2=int(input("Digite a Nota 2: "))
        nota3=int(input("Digite a Nota 3: "))
        nota4=int(input("Digite a Nota 4: "))
        media=(nota1+nota2+nota3+nota4)/4
        print(f"Você tirou {nota1}, {nota2}, {nota3} e {nota4}, sua média é de {media}")
        print("\n\nVocê será redirecinado ao menu\n\n")
    if menu==10: #fatorial
        print("\nBem vindo à FATORIAL")
        num = int(input("Fatorial de: ") )
        result=1
        count=1
        while count <= num:
            result = result * count
            count = count + 1
            print(f"o fatorial de {num} é {result}")
            print("\n\nVocê será redirecinado ao menu\n\n")


