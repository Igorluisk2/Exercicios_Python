#1 Crie duas matrizes A e B de tamanho fixo e calcule a matriz resultante

'''a = [[1,2,3],
     [4,5,6]]

b = [[7,8,9],
     [10,11,12]]
    
soma = a[1][1]+ b [1][1]
print(soma)'''

#2 Crie uma matriz A e passe os valores para uma Matriz B em ordem invertida

'''matriz_A = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

# Obtendo as dimensões da matriz A
linhas = len(matriz_A)
colunas = len(matriz_A[0])

# Inicializando a matriz B com zeros e com as mesmas dimensões que A
matriz_B = [[0 for _ in range(colunas)] for _ in range(linhas)]

# Passando os valores de A para B em ordem invertida
for i in range(linhas):
    for j in range(colunas):
        matriz_B[i][j] = matriz_A[linhas - 1 - i][colunas - 1 - j]

# Imprimindo a matriz B
for linha in matriz_B:
    print(linha)'''



#3 Crie uma matriz encontre e exiba o seu maior elemento.

'''matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 11, 9]
]

# Inicializando a variável para armazenar o maior elemento com o primeiro valor da matriz
maior_elemento = matriz[0][0]

# Percorrendo a matriz para encontrar o maior elemento
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento

# Exibindo o maior elemento
print(f"O maior elemento da matriz é: {maior_elemento}")'''



#4 Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma.

# Função para calcular a soma de uma linha
'''def soma_linha(matriz, linha):
    return sum(matriz[linha])

# Criando a matriz 3x3 e lendo os valores
matriz = []
for i in range(3):
    linha = [int(x) for x in input(f"Digite os valores da linha {i + 1} (separados por espaço): ").split()]
    matriz.append(linha)

# Inicializando a variável para a linha de maior soma
linha_maior_soma = 0
maior_soma = soma_linha(matriz, linha_maior_soma)

# Encontrando a linha de maior soma
for i in range(1, 3):
    soma_atual = soma_linha(matriz, i)
    if soma_atual > maior_soma:
        linha_maior_soma = i
        maior_soma = soma_atual

# Exibindo a linha de maior soma
print(f"A linha com a maior soma é a linha {linha_maior_soma + 1}: {matriz[linha_maior_soma]}")'''



#5 Crie uma matriz 3x3 e calcule sua diagonal principal e sua diagonal secundária

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculando a diagonal principal
diagonal_principal = [matriz[i][i] for i in range(3)]

# Calculando a diagonal secundária
diagonal_secundaria = [matriz[i][2 - i] for i in range(3)]

# Exibindo as diagonais
print("Diagonal Principal:", diagonal_principal)
print("Diagonal Secundária:", diagonal_secundaria)
