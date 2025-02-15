senha_correta = "1234"  
senha_digitada = ""
sair = False    

while sair == False: 
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == "":
        print("Senha vazia!. Acesso NEGADO , Tente novamente.") 

    elif senha_digitada == senha_correta:
        print("Senha correta! Acesso PERMITIDO.")
        sair = True  

    else: 
        print("Senha incorreta. Acesso NEGADO. Tente novamente.")