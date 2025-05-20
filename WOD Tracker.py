# Importa funções de outros arquivos (módulos):
from Route import treinoFormatado, load, cadastro 
from Login import login, registrando

# Inicialização de variáveis principais
treinos = []  # Lista temporária para armazenar dados de um treino
listaDeCadastro = []  # Lista de cadastros
nomes = ["dia", "mês", "ano", "\n[1]AMRAP \n[2]EMOM \n[3]for time\n", "o tempo/duração do treino em minutos"]
arquivo = 'valores.txt'  # Nome do arquivo onde os dados serão salvos
contador = 0  # Contador
logado = 0  # Usuário logado
cadastrado = 0  # Usuário cadastrado

# Tenta carregar os dados salvos no arquivo, ou cria um novo se falhar
try:
    valores = eval(load(arquivo))  # Converte string salva de volta para lista
    print(f"valores carregados: {valores}")
except:
    print("Criando arquivo novo...")
    valores = []

# Escolhe entre cadastro ou login
cadastroOuLogin = int(input("Você deseja se cadastrar[1] ou fazer o login[2]\n"))
if cadastroOuLogin == 1:
    registrando(listaDeCadastro, valores, arquivo)  # Realiza o cadastro
elif cadastroOuLogin == 2:
    login(valores, arquivo)  # Realiza o login

# Loop principal do programa
while True:
    valores = eval(load(arquivo))  # Atualiza os valores a cada ciclo
    resposta = int(input("Digite \n[1]adicionar \n[2]visualizar \n[3]editar \n[4]exclui\n"))

    # Escolha baseada na resposta do usuário
    match resposta:
        case 1:
            # Adiciona um novo treino
            for i in range(5):
                treinos.append(int(input(f"Digite {nomes[i]}: ")))  # Recebe data, tipo e duração

            # Recebe os movimentos feitos no treino até o usuário digitar "sair"
            while True:
                movimento = input("Qual movimento foi feito no treino ?(digite sair para parar o programa)")
                if movimento.lower().strip() == "sair":
                    break
                treinos.append(movimento)

            # Adiciona o treino à lista de treinos do usuário
            if cadastroOuLogin == 1:
                valores[cadastrado].append(treinos)
                cadastro(str(valores), arquivo)
            elif cadastroOuLogin == 2:
                valores[logado].append(treinos)
                cadastro(str(valores), arquivo)

            treinos.clear()  # Limpa a lista temporária para o próximo treino

        case 2:
            # Visualiza os treinos salvos
            if cadastroOuLogin == 1:
                treinoFormatado(valores, cadastrado)
            elif cadastroOuLogin == 2:
                treinoFormatado(valores, logado)

        case 3:
            # Edita um treino existente
            if cadastroOuLogin == 1:
                if len(valores[cadastrado]) == 2:
                    continue  # Evita editar se não houver treinos
                treinoFormatado(valores, cadastrado)
            elif cadastroOuLogin == 2:
                if len(valores[logado]) == 2:
                    continue
                treinoFormatado(valores, logado)

            resposta = int(input("Qual treino você quer mudar(considere o treino no topo o treino 1): "))

            if cadastroOuLogin == 1:
                for i in range(len(valores[cadastrado])):
                    if valores[cadastrado] == 3:
                        # Troca o tipo do treino
                        treinos[resposta - 1][3] = int(input("Qual tipo de treino você quer substituir \n[1]AMRAP \n[2]EMOM \n[3]for time\n"))
                        continue
                    # Substitui data e duração
                    treinos[resposta - 1][i] = int(input(f"Qual {nomes[i]} você quer substituir: "))

                # Substitui os movimentos
                for j in range(len(treinos[resposta - 1])):
                    if j >= 5:
                        treinos[resposta - 1][j] = input("Por qual movimento você quer substituir ")

        case 4:
            # Deleta um treino existente
            treinoFormatado(len(treinos), treinos)  # Mostra os treinos com índice
            if not treinos:
                continue  # Se não houver treinos, volta ao menu

            resposta = int(input("Qual treino você quer deletar(considere o treino no topo o treino 1): "))
            treinos.pop(resposta - 1)  # Remove o treino escolhido
            print('Treino deletado\n ')
            contador -= 1  # Atualiza o contador
