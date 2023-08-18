#O fatorial de um número é o produto dele pelos seus antecessores maiores que 0. 
#O fatorial de um número é a multiplicação desse número por todos os seus antecessores maiores que zero.

'''def fatorial(x):
    if x==1:
        return 1
    else:
        return x * fatorial(x-1)

while True:
    x = int(input("Fatorial de: "))
    print("Fatorial: ",fatorial(x) )'''
    
    
'''def soma(n):                  #msm coisa que acima
    if n == 1:
        return 1
    else:
        return n * soma(n - 1)
numero = 5 
result = soma(numero)
print(f"O fatorial do {numero} é {result}")    ''' 


#torre de hanoi
def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return 1
    movimentos = 0
    movimentos += torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    movimentos += 1
    movimentos += torre_hanoi(n - 1, auxiliar, destino, origem)
    return movimentos

num_discos = 10 
total_movimentos = torre_hanoi(num_discos, 'A', 'C', 'B')
print(f"Total de movimentos necessários: {total_movimentos}")