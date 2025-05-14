

def treinoFormatado(valores,formatacao):
        if len(valores[formatacao]) == 1:
            print("Nenhum treino cadastrado.\n")
        
        for i in range(len(valores[formatacao])):
            if i > 1:
                print(f"{valores[formatacao][i][0]}/{valores[formatacao][i][1]}/{valores[formatacao][i][2]}")#data
                print("Tipo de treino:", end = " ")#tipo de treino

                if valores[formatacao][i][3] == 1:
                    print("AMRAP")

                elif valores[formatacao][i][3] == 2:
                    print("EMOM")

                elif valores[formatacao][i][3] == 3:
                    print("for time")

                else:
                    print("resposta inválida")
                print(f"tempo: {valores[formatacao][i][4]}\nMovimentos:")# duração do treino
                for j in range(len(valores[formatacao][i])):#movimentos do treino
                    if j >=5:
                        print(valores[formatacao][i][j])
                print()

def load(arquivo):
    with open(arquivo, 'r') as f:
        read = f.read()
    return read

def cadastro(valorInputado, arquivo):
    with open(arquivo, 'w') as f:
        f.write(valorInputado)