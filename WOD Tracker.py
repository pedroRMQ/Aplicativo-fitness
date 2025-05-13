treinos = []
listaDeCadastro = []
nomes = ["dia","mês","ano","\n[1]AMRAP \n[2]EMOM \n[3]for time\n","o tempo/duração do treino em minutos"]
arquivo = 'valores.txt'
contador = 0

def login(valores):
    global logado
    with open(arquivo, 'r') as f:
        userName = input("Digite o nome do usuário: ")
        userPassword = input("Digite o nome do usuário: ")
        
        for i in range(len(valores)):
            if valores[i][0] == userName:
                if valores[i][1] == userPassword:
                    print("entrou")
                    logado = i
                else:
                    print("senha incorreta")
        
def registrando(listaDeCadastro, valores):
    global cadastrado

    listaDeCadastro.append(input("Digite o nome do usuário: "))
    listaDeCadastro.append(input("Digite a senha do usuário: "))

    valores.append(listaDeCadastro)
    cadastro(str(valores),arquivo)

    cadastrado = len(valores)-1

def cadastro(valorInputado, arquivo):
    with open(arquivo, 'w') as f:
        f.write(valorInputado)

def load(arquivo):
    with open(arquivo, 'r') as f:
        read = f.read()
    return read

def treinoFormatado(valores,formatacao):
        if len(valores[formatacao]) == 1:
            print("Nenhum treino cadastrado.\n")
            return
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

try:
    valores = eval(load(arquivo))
    print(f"valores carregados: {valores}")
except:
    print("Criando arquivo novo...")
    valores = []

cadastroOuLogin = int(input("Você deseja se cadastrar[1] ou fazer o login[2]\n"))
if cadastroOuLogin == 1:
    registrando(listaDeCadastro, valores)
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
                valores[logado].append(treinos)
                cadastro(str(valores), arquivo)
            treinos.clear()

        case 2:#mostra todos os treinos
            if cadastroOuLogin == 1:
                treinoFormatado(valores,cadastrado)
            elif cadastroOuLogin == 2:
                treinoFormatado(valores, logado)

        case 3:#edita o treino escolhido
            if cadastroOuLogin == 1:
                if len(valores[cadastrado]) == 2:
                    continue
                treinoFormatado(valores,cadastrado)

            elif cadastroOuLogin == 2:
                if len(valores[logado]) == 2:
                    continue
                treinoFormatado(valores, logado)

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