import math
import datetime as dt #biblioteca de horas, AS dt funciona como apelido para chamar a biblioteca 
import time #
x = 3.5
math.ceil(x) #arredonda pra cima
print(math.ceil(x))

s = 6.8
math.floor(s) #arredonda pra baixo
print(math.floor(s))

a = -3
math.fabs(a) #retorna o valor inteiro
print(math.fabs(a))

n = 3
math.factorial(n) #retorna o fatorial com um inteiro (gera valueError se não for um inteiro ou for negativo)
print(math.factorial(n))


z = 81
math.isqrt(z) #retorna a raiz quadrada inteira do inteiro não negativo z. este é o piso da raiz qiadrada exata de n. SQRT retorna float
print(math.isqrt(z))


v = 2 
c = 10
math.pow #retorna v elevado a potencia de c (x e y) necessita de 2 parametros
print(math.pow(v,c))

#datetime
print(dt.date.today()) #retorna a data de hj do computador no padrão gringo (ano-mes-dia)
print(dt.date.today().strftime('%d/%m/%Y')) #retorna a data de hj do computador no padrão brasileiro (dia-mes-ano)
print(dt.datetime.now()) #retorna a data e hora de agora no padrao gringo
print(dt.datetime.now().strftime('%d/%m/%Y/%H:%M:%S')) #retorna a data e hora de agora no padrao br

#time
u = 0
i = time.perf_counter()
while u <10000:
    print(u)
    u+=1
o = time.perf_counter()
print(u-i)


