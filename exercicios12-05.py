#17
'''p1=float(input("Digite o preço do primeiro produto: "))
p2=float(input("Digite o preço do segundo produto: "))
p3=float(input("Digite o preço do terceiro produto: "))

result1=(p1*2)*(p2/2)
print("\nO produto do dobro do primeiro com metade do segundo é ",result1)

result2=(p1*3)+p3
print("\nA soma do triplo do primeiro com o terceiro é ",result2)

result3=p3*p3*p3
print("\nO terceiro elevado ao cubo é ",result3,"\n\n\n\n")

#18
altura = float(input("Insira sua altura: "))
soma = (72.7*altura)-58
print ("Seu peso ideal é %.2f"% soma)

#listas

a = [10,20,30,40]
print(a)
print(type (a))

b = ["pyton",3.5,True,[1]]
print(b)
print(type(b))

c = [10,1,True,"a",[1,2,3]]
print (len(c))

lista = [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(lista[3][1])

animais = ["gato","cachorro"]
print ("gato" in animais)

animais = ["gato","cachorro"]
print ("arara" not in animais)

d = [1,2,3,4,5,6,7,8,9]
print(d)
print(max(d))
print(min(d))
print(sum(d))

print("\n")

e = [1,3,5]
f = [2,4,6]
print(e + f)

print("\n")

t = [1,2,3,4,5,6,7,8,9]
print(sum(t)/len(t))

print("\n")

uma_lista = ['a','b','c','d','e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

frutas = ["banana", "maçã","cereja"]

frutas[0] = "pera"
frutas[-1] = "laranja"
print(frutas)

lista = ["flor","azul",[1,"casa"]]
lista[2][1] = "escola"
print(lista)

uma_lista = ["a","b","c","d","e","f"]
uma_lista[1:3] = ["x","y"]
print(uma_lista)

uma_lista = ["a","b","c","d","e","f"]
uma_lista[1:3] = ["x","y"]
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3] = []
print(uma_lista)
print(len(uma_lista))

k = ["a","d","f"]
print(k)

k[1:1] = ["b","c"]
print(k)

k[4:4] = ["e"]
print(k)

uma_lista = [4,2,8,6,5]
uma_lista[2] = [True]
print(uma_lista)

a = ["um","dois","tres"]
del a[1]
print(a)

lista = ["a","b","c","d","e","f"]
del lista[1:5]
print(lista)

a = [81,82,83]
a.append(5)
print(a)

x=[8,5,4,3]
x.sort()
print(x)

z=[8,2,4,3]
z.sort(reverse=True)
print(z)

o = [1,2,3,"carro",5,6]
print(o.index("carro"))

ç = [1,2,3,4]
ç.insert(2,100)
print(ç)

l = [1,2,3,4,5,6,4]
print(l.count(4))'''

y = [1,2,3,4]
y.pop(2)
print(y)