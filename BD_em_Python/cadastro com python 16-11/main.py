from cadastro import * 

while True:
    print(10*"=+","Cadastro","+="*10)
    
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")
    cpf = input("Digite o seu cpf: ")
    rg = input("Digite o seu rg: ")
    telefone = input("Digite o seu telefone: ")
    sexo = input("Digite o seu sexo: ")
    cep = input("Digite o seu cep: ") 
    cnh = input("Digite a sua cnh: ")
    estado_civil = input("Digite o seu estado civil: ")
    endereco = input("Digite o seu endereco: ")
    
       
    cad = Cadastro()
    cad.inserir_banco(nome,sobrenome,cpf,rg,telefone,sexo,cep,cnh,estado_civil,endereco)
    print(10*"=+","Cadastro concluido com sucesso","+="*10,"\n"*2)        
        
        