#controle tv

class ControleTV:
    def __init__(self,liga=False):
        self.liga=liga
         
    

    def ligou(self):
        print(f"A TV ligou")


    def desligou(self):
        print(f"A TV desligou")


acao1=ControleTV()
acao1.ligou()
acao1.desligou()