import GUI as g

def login(valores, arquivo):
    global usuario

    userName = input("Digite o nome do usuário: ")
    userPassword = input("Digite o nome do usuário: ")
        
    for i in range(len(valores)):
        if valores[i][0] == userName:
            if valores[i][1] == userPassword:
                print("entrou")
                usuario = i
            else:
                print("senha incorreta")

def registrando(listaDeCadastro, valores, arquivo):
    global cadastrado

    listaDeCadastro.append(input("Digite o nome do usuário: "))
    listaDeCadastro.append(input("Digite a senha do usuário: "))

    valores.append(listaDeCadastro)
    with open(arquivo, 'w') as f:
        f.write(str(valores))

    cadastrado = len(valores)-1
