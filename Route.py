def treinoFormatado(valores,formatacao):
        
        if len(valores[formatacao]) == 2:
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

def substituir(valores,formatacao,nomes):
    resposta = int(input("Qual treino você quer mudar(considere o treino no topo o treino 1): "))

    for i in range(5):

        if valores[formatacao][resposta+1][i] == 3:

            valores[formatacao][resposta+1][3] = int(input("Digite por qual tipo de treino você quer substituir \n[1]AMRAP \n[2]EMOM \n[3]for time\n"))
            continue

        valores[formatacao][resposta+1][i] = int(input(f"Digite {nomes[i]} você quer substituir: "))

        for j in range(len(valores[resposta+1])):#movimentos do treino

            if j >=5:
                valores[formatacao][resposta+1][j] = input("Digite por qual movimento você quer substituir: ")
    return valores

def deletar(valores,formatacao):

    resposta = int(input("Qual treino você quer deletar(considere o treino no topo o treino 1): "))

    valores[formatacao].pop(resposta+1)

    return valores