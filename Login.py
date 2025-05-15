
def login(valores):

    userName = input("Digite o nome do usuário: ")
    userPassword = input("Digite o nome do usuário: ")
        
    for i in range(len(valores)):
        if valores[i][0] == userName:
            if valores[i][1] == userPassword:
                print("entrou")
                usuario = i
                return usuario
            else:
                print("senha incorreta")

def registrando(listaDeCadastro, valores, arquivo):
    
    listaDeCadastro.append(input("Digite o nome do usuário: "))
    listaDeCadastro.append(input("Digite a senha do usuário: "))

    valores.append(listaDeCadastro)
    with open(arquivo, 'w') as f:
        f.write(str(valores))

    cadastrado = len(valores)-1
    return cadastrado