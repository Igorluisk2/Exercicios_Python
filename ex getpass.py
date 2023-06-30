from getpass import getpass

senha=getpass("Digite sua senha: ")
confirmar_senha=getpass("Confirme a senha: ")

if senha == confirmar_senha:
    print("Senha correta")
else:
    print("Senha incorreta")