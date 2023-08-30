class Calculadora():
    def calcular(self,op):
        
        
        if op=='somar':
            result = self.__adicionar()
            return result
        
        elif op=='subtrair':
            result = self.__subtrair()
            return result
            
            
    def __adicionar(self):
        return 2 + 2
        
        
    def __subtrair(self):
        return 5 - 2
    
    
conta=Calculadora()
print(conta.calcular("subtrair"))
print(conta.calcular('somar'))
