
from Route import treinoFormatado, load, cadastro, substituir, deletar
from Login import login, registrando

treinos = []
listaDeCadastro = []
nomes = ["dia","mês","ano","\n[1]AMRAP \n[2]EMOM \n[3]for time\n","o tempo/duração do treino em minutos"]
arquivo = 'valores.txt'
contador = 0

try:
    valores = eval(load(arquivo))
    print(f"valores carregados: {valores}")
except:
    print("Criando arquivo novo...")
    valores = []

cadastroOuLogin = int(input("Você deseja se cadastrar[1] ou fazer o login[2]\n"))
if cadastroOuLogin == 1:
    cadastrado = registrando(listaDeCadastro, valores, arquivo)
elif cadastroOuLogin == 2:
    usuario = login(valores)

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
                treinoFormatado(valores,cadastrado)

                valores = substituir(valores,cadastrado,nomes)

                cadastro(str(valores), arquivo)

            elif cadastroOuLogin == 2:
                treinoFormatado(valores, usuario)

                valores = substituir(valores,usuario,nomes)

                cadastro(str(valores), arquivo)

        case 4:#deleta o treino
            if cadastroOuLogin == 1:

                treinoFormatado(valores,cadastrado)

                valores = deletar(valores,cadastrado)

                cadastro(str(valores), arquivo)
            
            elif cadastroOuLogin == 2:

                treinoFormatado(valores,usuario)

                valores = deletar(valores,usuario)

                cadastro(str(valores), arquivo)