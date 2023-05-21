#cadastro
while True:    
    email = input("Digite um email: ")
    senha = input("Digite uma senha ")
    print("-"*15)
    if "@gmail" in email or "@hotmail" in email:
        pass
        if len(senha) >= 6:
            print("Cadastro feito com sucesso")
            break
        else:
            print("Senha muito pequena")
            senha = input("Digite uma senha novamente ")
            if len(senha) >= 6:
                print("Cadastro feito com sucesso")
                print("-"*6)
                break
            else:
                print("-"*15)
                print("Senha pequena. Erro de aplicacao. Inicie novamente")
                exit()
             
    else:
        print("Digite um email valido")
        print("-"*15)
#login
email_login = email
senha_login = senha

def login():
    while True:
        email_login = str(input("Digite seu email "))
        senha_login = str(input("Digite sua senha "))

        if (email_login == email) and (senha_login == senha):
            print("Login efetuado com sucesso")
            print("-"*15)
            break
        else:
            print("Email ou senha invalido")
            print("-"*15)
login()

print("Bem Vindo")