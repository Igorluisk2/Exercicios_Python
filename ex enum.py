import enum
#criando enumerações usando classe
class Animal(enum.Enum):
    cachorro = 1
    gato = 2 
    pantera = 2

#comparação usando "is"
if Animal.cachorro is Animal.gato:
    print("Cão e gato são os mesmos animais")
else:
    print("Cão e gato são animais diferentes")

# Comparação usando " !=(diferente)"
if Animal.pantera != Animal.gato:
    print("Leão e gatos são diferente")
else:
    print("Pantera e gatos são iguais")