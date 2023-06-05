#exercícios de tratamento de exceção:
#criar um software de venda de passagem aérea, que terá os seguintes dados de cadastro: 
#cadastro cliente, nome, sobrenome, rg, cpf, endereço, fone, idade
#cadastro passagem: destino, origem, duração, valor passagem, desconto 5%
#cadastro avião: modelo, ano, horas de voo, cor, quantidade de passageiros
#cadastro tripulação: nome, cargo, idade, data de admissao e fone
#o algoritmo deve ter a opção de cadastrar, imprimir relatorio, encerrar. utilizar while, for, try, if, else, jesus cristo,
import os

lnome=[]
lsobrenome=[]
lrg=[]
lcpf=[]
lendereço=[]
lfone=[]
lidade=[]
lcadastro_cliente=[lnome,lsobrenome,lrg,lcpf,lendereço,lfone,lidade]

ldestino=[]
lorigem=[]
lduracao=[]
lvalorpassagem=[]
ldesconto=[]
lcadastro_passagem=[ldestino,lorigem,lduracao,lvalorpassagem,ldesconto]

lmodelo=[]
lano=[]
lhorasvoo=[]
lcor=[]
lnumpassageiros=[]
lcadastro_aviao=[lmodelo,lano,lhorasvoo,lcor,lnumpassageiros]

lnometrip=[]
lcargo=[]
lidadetrip=[]
ladmissao=[]
lfonetrip=[]
lcadastro_trip=[lnometrip,lcargo,lidadetrip,ladmissao,lfonetrip]

while True:
    try:
        op=str(input("Bem vindo ao menu do Tia Leila Airways!\nDigite 1 - Cadastro de Cliente\nDigite 2 - Cadastro Passagem\nDigite 3 - Cadastro avião\nDigite 4 - Cadastro Tripulação\nDigite X - Sair\nDigite M - Mostrar Cadastros\n- "))
        os.system("pause")
        os.system("cls")
        if op=='X' or op=='x':
            print("Obrigado por usar o programa do Tia Leila Airways!")
            break
        if op=='M' or op=='m':
            try:
                print(f"cadastro de cliente: {lcadastro_cliente}\n")
                print(f"cadastro de passagem: {lcadastro_passagem}\n")
                print(f"cadastro de aviao: {lcadastro_aviao}\n")
                print(f"cadastro de tripulação: {lcadastro_trip}\n")
                os.system("pause")
                os.system("cls")
            except:
                print("Dados insuficientes, preencha pelo menos um cadastro completo!")
        op=int(op)
        if op==1:
            try:
                print("\nTELA DE CADASTRO DE CLIENTE")
                nome=str(input("Nome: "))
                sobrenome=str(input("Sobrenome: ")) 
                rg=int(input("RG: "))             
                cpf=int(input("CPF: "))               
                endereço=str(input("Endereço: "))                
                fone=int(input("Fone: "))                
                idade=int(input("Idade: "))
                os.system("pause")
                os.system("cls")
            except ValueError:
                print("Erro, tente novamente.")
                continue
            except:
                print("erro desconhecido, tente novamente")
            else:
                print("Cadastro de cliente realizado com sucesso!!!")
                lnome.append(nome)
                lsobrenome.append(sobrenome)
                lrg.append(rg)
                lcpf.append(cpf)
                lendereço.append(endereço)
                lfone.append(fone)
                lidade.append(idade)
            finally:
                print("\nVocê será redirecionado ao menu...")
                os.system("pause")
                os.system("cls")
        if op==2:
            try:
                print("\nTELA DE CADASTRO DE PASSAGEM")
                origem=input("Origem: ")
                destino=input("Destino: ")
                duracao=float(input("Duração do voo: "))
                valorpassagem=float(input("Valor da Passagem: "))
                desconto=int(input("Desconto: "))
                os.system("pause")
                os.system("cls")
            except ValueError:
                print("Erro, tente novamente.")
                continue
            except:
                print("erro desconhecido, tente novamente")
                continue
            else:
                print("Cadastro de passagem realizado com sucesso!!!")
                lorigem.append(origem)
                ldestino.append(destino)
                lduracao.append(duracao)
                lvalorpassagem.append(valorpassagem)
                ldesconto.append(desconto)
            finally:
                print("\nVocê será redirecionado ao menu...")
                os.system("pause")
                os.system("cls")
        if op==3:
            try:
                print("\nTELA DE CADASTRO DE AVIÃO")
                modelo=str(input("Modelo: "))
                ano=int(input("Ano: "))
                horasvoo=int(input("Horas de voo: "))
                cor=str(input("Cor: "))
                numpassageiros=int(input("Número de passageiros: "))
            except ValueError:
                print("Erro, tente novamente")
                continue
            except:
                print("Erro desconhecido, voltando ao menu...")
            else:
                print("Cadastro de avião realizado com sucesso!!!")
                lmodelo.append(modelo)
                lano.append(ano)
                lhorasvoo.append(horasvoo)
                lcor.append(cor)
                lnumpassageiros.append(numpassageiros)
            finally:
                print("Você será redirecionado ao menu...")
                os.system("pause")
                os.system("cls")
        if op==4:
            try:
                print("\nTELA DE CADASTRO DE TRIPULAÇÃO")
                nometrip=str(input("Nome do tripulante: "))
                cargo=str(input("Cargo: "))
                idadetrip=int(input("Idade do tripulante: "))
                admissao=str(input("Data de admissão: "))
                fonetrip=int(input("Telefone: "))
            except ValueError:
                print("Erro de valor, tente novamente")
            except:
                print("Erro desconhecido, tente novamente")
            else:
                print("Cadastro de tripulação realizado com sucesso!!!")
                lnometrip.append(nometrip)
                lcargo.append(cargo)
                lidadetrip.append(idadetrip)
                ladmissao.append(admissao)
                lfonetrip.append(fonetrip)
            finally:
                print("Você será redirecionado ao menu...")
                os.system("pause")
                os.system("cls")
    except:
        print("ferrou")

