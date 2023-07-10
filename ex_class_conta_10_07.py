class Conta():
    def  __init__(self,agencia,nome,conta,fone,cpf):
        self.agencia = agencia
        self.nome = nome
        self.conta = conta
        self.fone = fone
        self.saldo= 0
        self.cpf = cpf


    def extrato(self):
        print(self.saldo)

    def depositar(self,deposito):
        self.saldo+=deposito
    
    def sacar(self,saque):
        self.saldo-=saque