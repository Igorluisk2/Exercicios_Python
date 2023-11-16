from bd import *



class Cadastro():
    def __init__(self):
        self.banco = BancoDados()
        
    def inserir_banco(self,nome, sobrenome,cpf,rg,telefone,sexo,cep,cnh,estado_civil,endereco):
        self.banco.insert_cadastro(nome, sobrenome,cpf,rg,telefone,sexo,cep,cnh,estado_civil,endereco)
