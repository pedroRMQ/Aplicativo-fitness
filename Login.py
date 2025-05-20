# Função para login do usuário
def login(valores, arquivo): 
    global logado  # Usuário logado

    # Solicita os dados de login ao usuário
    userName = input("Digite o nome do usuário: ")
    userPassword = input("Digite a senha do usuário: ")

    # Percorre a lista de usuários salvos para verificar o login
    for i in range(len(valores)):
        if valores[i][0] == userName:
            if valores[i][1] == userPassword:
                print("Login bem-sucedido!")
                logado = i  # Armazena o índice do usuário logado
                return logado
            else:
                print("Senha incorreta.")
                return None

    print("Usuário não encontrado.")
    return None


# Função para registrar um novo usuário
def registrando(listaDeCadastro, valores, arquivo):
    global cadastrado  # Usuário cadastrado

    # Solicita os dados de cadastro ao usuário
    nome = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")

    # Adiciona os dados à lista temporária de cadastro
    listaDeCadastro.append(nome)
    listaDeCadastro.append(senha)

    # Adiciona a nova conta à lista completa de valores
    valores.append(listaDeCadastro)

    # Salva os dados atualizados no arquivo
    with open(arquivo, 'w') as f:
        f.write(str(valores))

    # Armazena o índice do novo usuário cadastrado
    cadastrado = len(valores) - 1
    return cadastrado
