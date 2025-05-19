
def treinos_usuario(nome):
    
    treinos = []

    with open("valores.txt", "r") as f:

        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == nome:
                for i in range(len(dados)-2):
                    treinos.append(dados[i+2])
    return treinos

def substituir(nome,treino):

    linhas_novas = []

    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == nome:
                dados.append(treino)

            linha =  ";".join(dados) + "\n"

        linhas_novas.append(linha)
    
    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)




def deletar(valores,formatacao):

    resposta = int(input("Qual treino você quer deletar(considere o treino no topo o treino 1): "))

    valores[formatacao].pop(resposta+1)

    return valores