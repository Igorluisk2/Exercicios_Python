'''6 - Faça uma função que informe a quantidade de digitos de um determinado número inteiro informado.'''

def contador(n):
    contagem = len(n)
    return contagem
numero = str(input("Informe um numero inteiro: "))
print(contador(numero))