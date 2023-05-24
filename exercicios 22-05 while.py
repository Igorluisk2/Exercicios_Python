'''lnome = []
lsobrenome = []
lendereco = []
lbairro = []
lcidade = []
lestado = []
lpais = []
lfone = []
lcpf = []
lpeso = []
laltura = []
lidade = []
ln_do_cartao = []
lemail = []
lcep = []
lnota1 = []
lnota2 = []
lnota3 = []
lnota4 = []
lserie = []
lclasse = []
lsexo = []
lcor = []
lmedia = []
lcont = []
cont = 0


while True:
  
    c = int(input("Digite 1 cadastro\nDigite 2 para consulta: "))
    if c == 1:
        nome = (input("Digite seu nome: "))
        lnome.append(nome)
        sobrenome = input("Digite seu sobrenome: ")
        lsobrenome.append(sobrenome)
        idade = input("Digite seu idade: ")
        lidade.append(idade)
        endereco = input("Digite seu endereço: ")
        lendereco.append(endereco)
        bairro = input("Digite seu bairro: ")
        lbairro.append(bairro)
        cidade = input("Digite seu cidade: ")
        lcidade.append(cidade)
        estado = input("Digite seu estado: ")
        lestado.append(estado)
        pais = input("Digite seu pais: ")
        lpais.append(pais)
        fone = input("Digite seu fone: ")
        lfone.append(fone)
        cpf = input("Digite seu CPF: ")
        lcpf.append(cpf)
        peso = input("Digite seu peso: ")
        lpeso.append(peso)
        altura = input("Digite seu altura: ")
        laltura.append(altura)
        n_do_cartao = input("Digite seu numero do cartão: ")
        ln_do_cartao.append(n_do_cartao)
        email = input("Digite seu email: ")
        lemail.append(email)
        cep = input("Digite seu CEP: ")
        lcep.append(cep)
        serie = input("Digite sua serie: ")
        lserie.append(serie)
        classe = input("Digite sua classe: ")
        lclasse.append(classe)
        sexo = input("Digite seu sexo: ")
        lsexo.append(sexo)
        cor = input("Digite sua cor: ")
        lcor.append(cor)
        nota1 = float(input("Digite a primeira nota: "))
        lnota1.append(nota1)
        nota2 = float(input("Digite a segunda nota: "))
        lnota2.append(nota2)
        nota3 = float(input("Digite a terceira nota: "))
        lnota3.append(nota3)
        nota4 = float(input("Digite a quarta nota: "))
        lnota4.append(nota4)
        media = ((nota1+nota2+nota3+nota4)/4)
        lmedia.append(media)
        print(lmedia)
        cont = cont + 1
        lcont.append(cont)
        c = int(input("Digite 1 para continuar\nDigite 2 para consulta\nDigite 0 para sair:  "))
        
    elif c == 2:
        busca = int(input("Digite o numero da matricula: "))
        print(lcont,lnome[busca-1],lsobrenome[busca-1],lidade[busca-1],lendereco[busca-1],lbairro[busca-1],lcidade[busca-1]\
        ,lestado[busca-1],lpais[busca-1],lfone[busca-1],lcpf[busca-1],lpeso[busca-1],laltura[busca-1],lidade[busca-1]\
        ,ln_do_cartao[busca-1],lemail[busca-1],lcep[busca-1],lnota1[busca-1],lnota2[busca-1],lnota3[busca-1],lnota4[busca-1]\
        ,lserie[busca-1],lclasse[busca-1],lsexo[busca-1],lcor[busca-1],lmedia[busca-1])
        c = int(input("Digite 1 para continuar o cadastro\nDigite 2 para continuar a consulta\nDigite 0 para sair: "))
    elif c == 3:
        delete=int(input("Dogote a matricula a ser excluida"))
        del(lnome[delete-1],lsobrenome[delete-1],lidade[delete-1],lendereco[delete-1],lbairro[delete-1],lcidade[delete-1]\
        ,lestado[delete-1],lpais[delete-1],lfone[delete-1],lcpf[delete-1],lpeso[delete-1],laltura[delete-1],lidade[delete-1]\
        ,ln_do_cartao[delete-1],lemail[delete-1],lcep[delete-1],lnota1[delete-1],lnota2[delete-1],lnota3[delete-1],lnota4[delete-1]\
        ,lserie[delete-1],lclasse[delete-1],lsexo[delete-1],lcor[delete-1],lmedia[delete-1])
       
    elif c == 0:
        print("Obrigado volte sempre...")
        break
    else:
        print("\nNumero invalido\n-----Tente Novamente-----\n")'''

nomes = ["pedro","João","Leticia",[1]]
sub = nomes [-1]
for n in sub:
    print(n)

nomes = ["pedro","João","Leticia",[1]]
for n in nomes:
    print(n)

sem_lista= ("Olá,mundo ")
for sl in sem_lista:
    print(sl)

nome = ["pedro","João","Leticia"]
for na in nome:
    print(na)
    if na == "João":
        break

n1 = ["pedro","João","Leticia"]
for a in n1:
    if a == "João":
        continue
    print(a)

    for x in range(6):
        print(x)

for x in range(2,6):
    print(x)

for x in range(2,10,2):
    print(x)

    for x in range(100,0,-1):
        print(x)

for i in range(10):
    for j in range(10):
        print(i,j)

for num in range (1,10):
    for num1 in range (1,11):
        print(f"{num} * {num1} = {num*num1}")

#1

for z2 in range(0,102,2):
    print(z2)

#2

n1=int(input("Digite um numero: "))
n2=int(input("Digite outro numero: "))
for b in range(n1,n2+1):
    print(b)