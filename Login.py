
def verificar_login(nome,senha):

    with open("valores.txt", "r")  as f:

        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == nome and dados[1] == senha:
                return True
            
    return False

def cadastrar_usuario(nome,senha):
  
    with open("valores.txt", "a") as f:
        f.write(f"{nome};{senha}\n")

def usuario_existe(nome):
    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")

            if nome == dados[0]:
                return True
            
    return False
