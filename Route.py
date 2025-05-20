# Função para exibir os treinos de forma formatada na tela
def treinoFormatado(valores, formatacao): 
    # Verifica se o usuário tem apenas a entrada de dados cadastrais
    if len(valores[formatacao]) == 1:
        print("Nenhum treino cadastrado.\n")
    
    # Percorre todos os treinos do usuário
    for i in range(len(valores[formatacao])):
        if i > 1:
            treino = valores[formatacao][i]

            # Exibe a data do treino
            print(f"{treino[0]}/{treino[1]}/{treino[2]}")

            # Exibe o tipo do treino
            print("Tipo de treino:", end=" ")
            if treino[3] == 1:
                print("AMRAP")
            elif treino[3] == 2:
                print("EMOM")
            elif treino[3] == 3:
                print("for time")
            else:
                print("resposta inválida")

            # Exibe a duração do treino
            print(f"tempo: {treino[4]} minutos")
            print("Movimentos:")

            # Exibe os movimentos realizados no treino
            for j in range(len(treino)):
                if j >= 5:
                    print(treino[j])
            print()  # Linha em branco após cada treino


# Função para carregar os dados salvos no arquivo
def load(arquivo):
    with open(arquivo, 'r') as f:
        read = f.read()  # Lê todo o conteúdo do arquivo como string
    return read


# Função para sobrescrever o conteúdo do arquivo com novos dados
def cadastro(valorInputado, arquivo):
    with open(arquivo, 'w') as f:
        f.write(valorInputado)  # Escreve os dados no arquivo, substituindo o anterior
