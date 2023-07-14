class Contabanco():
    def __init__(self,nome,senha):
        self.nome = nome
        self.__senha = senha
        self.__saldo = 0

    def saque(self,valor,senha):
        if senha==self.__senha:
            self.__saldo=self.__saldo-valor
            print(f"Seu novo saldo é de {self.__saldo},parabéns")
        else:
            print("Senha inválida, tente novamente mais tarde")


    def deposito(self,valor,senha):
        if senha==self.__senha:
            self.__saldo=self.__saldo+valor
            print(f"Seu novo saldo é de {self.__saldo}, parabéns")
        else:
            print("Senha inválida, tente novamente mais tarde")

    
    def extrato(self,senha):
        if senha==self.__senha:
            print(f"Seu saldo atual é de {self.__saldo}")
        else:
            print("Senha inválida")