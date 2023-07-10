class Bola():
    def  __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    
    def trocar_cor(self):
        trocar=input("Nova cor: ")
        self.cor=trocar
        print(f"A cor da bola foi alterada para {trocar} ")


    def mostrar_cor(self):
        print(f"A bola tem a cor {self.cor}")        