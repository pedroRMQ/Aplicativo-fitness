# Retorna todos os treinos cadastrados para um usuário específico
def treinos_usuario(nome): 
    treinos = []

    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")

            # Verifica se o nome da linha corresponde ao usuário buscado
            if dados[0] == nome:
                # Coleta os treinos a partir da terceira posição da linha
                for i in range(len(dados)-2):
                    treinos.append(dados[i+2])
    return treinos


# Adiciona um novo treino ao final da linha do usuário no arquivo
def substituir(nome, treino):
    linhas_novas = []

    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")

            # Quando encontra o usuário, adiciona o novo treino no final da linha
            if dados[0] == nome:
                dados.append(treino)

            # Reconstrói a linha atualizada
            linha =  ";".join(dados) + "\n"
            linhas_novas.append(linha)
    
    # Reescreve o arquivo inteiro com a linha atualizada
    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)
