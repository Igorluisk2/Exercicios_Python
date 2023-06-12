'''tradutor = {}
tradutor ["pineapple"] = "abacaxi"
tradutor ["apple"] = "maça"
tradutor ["orange"] = "laranja"
print(type(tradutor))
print(tradutor)
print(tradutor["apple"])'''

#fazer um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a idade como valor
'''people = {"Igor":27, "Nicholas":23, "Bruno":18,"Larissa":17,"Thiago":30}
print(people.values())'''

#criar um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor
#uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?)
'''semana = {"Segunda":'Ederson',"Terça":'Maurício',"Quarta":'Ederson',"Quinta":'Maurício',"Sexta":'Ederson',"Sábado":[],"Domingo":[]}
print(semana.keys()) #mostra apenas as chaves
print(semana.values()) #mostra apenas os valores
print(semana.items()) #mostra tudo que tem no dicionário'''

#criar um dicionário que é uma agenda e coloque nele os seguintes dados dentro de um outro dicionário: chave(cpf),nome,idade,telefone. O programa
#deve ler um número indeterminado de dados, criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-fone
dados = {'cpf':{"nome":'Igor Luís',"Idade":27,"Telefone":67992913452}}
print(dados['cpf'])