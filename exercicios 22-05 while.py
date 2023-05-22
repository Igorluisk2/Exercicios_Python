lnome = []
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
lmatricu = []
lmedia = []
lmatricula = []
lnom1 = []
lida = []
lcont = []
cont = 0
matricula = 0
c = 3

while True:
    if c == 3:
        c = int(input("Digite 1 para realizar a matricula ou digite 2 para informar seus dados: "))
    elif c == 2:
        nome = str(input("Digite seu nome: "))
        lnome.append(nome)
        sobrenome = input("Digite seu sobrenome: ")
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

        c = int(input("\nDigite '0' para sair\n'1' para Matricula\n'2' para continuar\n'3' para voltar ao menu:  "))

    
    elif c == 1:
            
            nom1 = input("Digite seu nome: ")
            ida = input("Digite sua idade: ")
            lnom1.append(nom1)
            lida.append(ida)
            cont = cont + 1
            lcont.append(cont)
            print(lnom1, lida, lcont)
            
            if cont == 10:
                 break
                
    elif c == 0:
        break
    



