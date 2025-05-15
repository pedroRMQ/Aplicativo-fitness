
from Route import *
from Login import *

treinos = []
listaDeCadastro = []
nomes = ["dia","mês","ano","\n[1]AMRAP \n[2]EMOM \n[3]for time\n","o tempo/duração do treino em minutos"]
arquivo = 'valores.txt'
usuario = 0
cadastrado = 0

try:
    valores = eval(load(arquivo))
    print(f"valores carregados: {valores}")
except:
    print("Criando arquivo novo...")
    valores = []

cadastroOuLogin = int(input("Você deseja se cadastrar[1] ou fazer o login[2]\n"))
if cadastroOuLogin == 1:
    registrando(listaDeCadastro, valores, arquivo)
elif cadastroOuLogin == 2:
    login(valores)

while True:
    valores = eval(load(arquivo))
    resposta = int(input("Digite \n[1]adicionar \n[2]visualizar \n[3]editar \n[4]exclui\n"))
    match resposta:
        case 1:

            for i in range(5):
                treinos.append(int(input(f"Digite {nomes[i]}: ")))#adicionando treinos 

            while True:
                movimento = input("Qual movimento foi feito no treino ?(digite sair para parar o programa)")#adicionando os movimentos feitos no treino

                if movimento.lower().strip() == "sair":
                    break

                treinos.append(movimento)

            if cadastroOuLogin == 1:
                valores[cadastrado].append(treinos)
                cadastro(str(valores), arquivo)

            elif cadastroOuLogin == 2:
                valores[usuario].append(treinos)
                cadastro(str(valores), arquivo)

            treinos.clear()

        case 2:#mostra todos os treinos

            if cadastroOuLogin == 1:
                treinoFormatado(valores,cadastrado)

            elif cadastroOuLogin == 2:
                treinoFormatado(valores, usuario)

        case 3:#edita o treino escolhido
            if cadastroOuLogin == 1:
                if len(valores[cadastrado]) == 2:
                    continue
                treinoFormatado(valores,cadastrado)

            elif cadastroOuLogin == 2:
                if len(valores[usuario]) == 2:
                    continue
                treinoFormatado(valores, usuario)

            resposta = int(input("Qual treino você quer mudar(considere o treino no topo o treino 1): "))
            if cadastroOuLogin == 1:

                for i in range(len(valores[cadastrado])):
                    if valores[cadastrado] == 3:
                        treinos[resposta-1][3] = int(input("Qual tipo de treino você quer substituir \n[1]AMRAP \n[2]EMOM \n[3]for time\n"))
                        continue

                    treinos[resposta-1][i] = int(input(f"Qual {nomes[i]} você quer substituir: "))

                for j in range(len(treinos[resposta-1])):#movimentos do treino
                    if j >=5:
                        treinos[resposta-1][j] = input("Por qual movimento você quer substituir ")

        case 4:#deleta o treino

            treinoFormatado(len(treinos),treinos)
            if not treinos:
                continue

            resposta = int(input("Qual treino você quer deletar(considere o treino no topo o treino 1): "))
            treinos.pop(resposta - 1)
            print('Treino deletado\n ')
            contador -= 1