# Verifica se o nome e a senha correspondem a um usuário existente no arquivo
def verificar_login(nome, senha): 
    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")
            
            # Confere se nome e senha estão corretos
            if dados[0] == nome and dados[1] == senha:
                return True  # Login válido

    return False  # Login inválido


# Cadastra um novo usuário no final do arquivo
def cadastrar_usuario(nome, senha):
    with open("valores.txt", "a") as f:
        f.write(f"{nome};{senha}\n")  # Adiciona o novo usuário no final do arquivo


# Verifica se um nome de usuário já existe no arquivo
def usuario_existe(nome):
    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")

            # Se o nome já estiver no arquivo, retorna True
            if nome == dados[0]:
                return True

    return False  # Nome de usuário ainda não cadastrado
