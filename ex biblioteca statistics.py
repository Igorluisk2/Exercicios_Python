import statistics
lista=[]
while True:
    x=float(input("Digite um número (0 para parar): "))
    if x==0:
        break
    else:
        lista.append(x)
    
print("Lista:",lista)
print("Média:",statistics.mean(lista))
print("Mediana:",statistics.median(lista))
print("Moda:",statistics.mode(lista))
print("Mulimoda:",statistics.multimode(lista))  