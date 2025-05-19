from tkinter import *#Importa todas as funções do tkinter sem precisar se referir ao tkinter antes da função 
from Login import *
from Route import *

#cria o frame de login
def frame_login():
    global Entrada_nome_login, Entrada_senha_login, tela_login 

    tela_login = Tk()
    
    tela_login.title("Login")
    tela_login.geometry(f"400x200")

    label_nome = Label(tela_login,text="Nome: ")
    label_nome.place(x=100,y=50)

    label_senha = Label(tela_login,text="Senha: ")
    label_senha.place(x=100,y=75)

    Entrada_nome_login = Entry(tela_login)
    Entrada_nome_login.place(x=150,y=50)

    Entrada_senha_login = Entry(tela_login, show="*")
    Entrada_senha_login.place(x=150,y=75)

    Button(tela_login,text="Login", command=inputs_login).place(x=185,y=100)

    link = Label(tela_login, text="Não sou cadastrado", cursor="hand2")
    link.place(x=0,y=175)
    link.bind("<Button-1>", lambda e: frame_cadastro())

    tela_cadastro.destroy() 

    tela_login.mainloop()

#cria o frame de cadastro
def frame_cadastro():
    global tela_cadastro, Entrada_nome_cadastro, Entrada_senha_cadastro 

    tela_cadastro = Tk()

    tela_cadastro.title("cadastro")
    tela_cadastro.geometry("400x200")

    label_nome = Label(tela_cadastro,text="Nome: ")
    label_nome.place(x=100,y=50)

    label_senha = Label(tela_cadastro,text="Senha: ")
    label_senha.place(x=100,y=75)

    Entrada_nome_cadastro = Entry(tela_cadastro)#Cria o espaço de input para o nome do usuario ser cadastrado
    Entrada_nome_cadastro.place(x=150,y=50)#Posiciona o espaço de input do nome do usuario

    Entrada_senha_cadastro = Entry(tela_cadastro)#Cria o espaço de input para a senha do usuario ser cadastrada
    Entrada_senha_cadastro.place(x=150,y=75)#Posiona o espaço de input da senha do usurio

    Button(tela_cadastro,text="cadastro",command=inputs_cadastro).place(x=185,y=100)#Cria o botão para submeter os cadastros

    link = Label(tela_cadastro, text="Já tenho cadastro", cursor="hand2")#cria o texto para retornar ao frame de login
    link.place(x=0,y=175)#Posiciona esse botão
    link.bind("<Button-1>", lambda e: frame_login())#Transforma esse texto em botão

    tela_login.destroy()

    tela_cadastro.mainloop()#mantem o frame aberto

#controla os inputs
def inputs_login():
    global nome

    mensagem = Label(tela_login, text="")
    mensagem.place(x=140,y=125)

    nome = Entrada_nome_login.get()
    senha = Entrada_senha_login.get()

    if verificar_login(nome,senha) == True:
        frame_home()
    else:
        mensagem.config(text="Senha ou nome incorreto", fg="red")
        Entrada_nome_login.delete(0,END)
        Entrada_senha_login.delete(0,END)

def inputs_cadastro():

    mensagem = Label(tela_cadastro, text="")
    mensagem.place(x=150,y=125)

    nome = Entrada_nome_cadastro.get() 
    senha = Entrada_senha_cadastro.get()

    if usuario_existe(nome) == True:
        mensagem.config(text="Esse usuario ja existe", fg="red")
    else:
        cadastrar_usuario(nome,senha)
        frame_login()

#cria o frame inicial
def frame_home():
    global home

    home = Tk() 

    Label(home,text=f"Bem vindo {Entrada_nome_login.get()}, Oque você deseja fazer hoje?").pack()

    home.geometry("800x600")

    Button(home,text="Adicionar", command=frame_adicionar).place(x=50,y=50)
    Button(home,text="Visualizar", command=frame_visualizar).place(x=150,y=50)

    tela_login.destroy()
    tela_cadastro.destroy()

    home.mainloop()

#cria o frame da opção de adicionar treino
def frame_adicionar():
    global entry_dia,entry_mes,entry_ano,var,entry_movimento,entry_tempo, adicionar

    adicionar = Tk()

    adicionar.title("adicionar")
    adicionar.geometry("500x500")
    
    label_data = Label(adicionar,text="Dia/mês/ano: ")
    label_data.place(x=100,y=30)

    label_tempo = Label(adicionar,text="tempo: ")
    label_tempo.place(x=100,y=200)

    label_movimento = Label(adicionar,text="movimentos: ")
    label_movimento.place(x=70,y=250)

    entry_dia = Entry(adicionar, width=3)
    entry_dia.place(x=180,y=30)
    Label(adicionar, text="/").place(x=200,y=30)

    entry_mes = Entry(adicionar, width=3)
    entry_mes.place(x=210,y=30)
    Label(adicionar, text="/").place(x=230,y=30)

    entry_ano = Entry(adicionar, width=5)
    entry_ano.place(x=240,y=30)
    
    var = StringVar()
    var.set("AMRAP")

    r1 = Radiobutton(adicionar, text="AMRAP", variable=var, value = "teste1", command=lambda: set(1))
    r2 = Radiobutton(adicionar, text="EMOM", variable=var, value = "teste2", command=lambda: set(2))
    r3 = Radiobutton(adicionar, text="for time", variable=var, value="teste3", command=lambda: set(3) )

    r1.place(x=80,y=80)
    r2.place(x=150,y=80)
    r3.place(x=200,y=80)

    entry_tempo = Entry(adicionar)
    entry_tempo.place(x=150,y=200)

    entry_movimento = Entry(adicionar)
    entry_movimento.place(x=150,y=250)

    Button(adicionar,text="adicionar movimento",command=adicao_movimentos).place(x=350,y=245)
    Button(adicionar,text="Concluir",command=input_adicionar).place(x=200,y=300)

def set(choose):
    var = StringVar()

    match choose:
        case 1:
            var.set("AMRAP")
        case 2:
            var.set("EMOM")
        case 3:
            var.set("for time")

def adicao_movimentos():
    movimento = ""

    try:
        movimento =  movimento + "," + entry_movimento.get()
        entry_movimento.delete(0,END)
    except:
        movimento =  movimento + "," + entry_movimento_editando.get() 
        entry_movimento_editando.delete(0,END)  

    return movimento

def input_adicionar():

    data = entry_dia.get() + "/" + entry_mes.get() + "/" + entry_ano.get()
    pratica = var.get()
    tempo = entry_tempo.get()

    movimento = adicao_movimentos()

    treino = data + "," + pratica + "," + tempo + movimento

    movimento = ""

    substituir(nome,treino)

    adicionar.destroy()

#cria o frame de visualizar os treinos
def frame_visualizar():
    global visualizar

    visualizar = Tk()
    visualizar.geometry("400x400")
    visualizar.title("Seus treinos")

    canvas = Canvas(visualizar)
    scrollbar = Scrollbar(visualizar, orient="vertical",command=canvas.yview)
    scroll_frame = Frame(visualizar)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0,0),window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    treinos = treinos_usuario(nome)

    for i in range(len(treinos)):

        info = treinos[i].split(",")

        if info == ['']:
            break

        Label(scroll_frame, text=f"Treino {i+1}º: ", font=("Arial", 10)).pack(pady=20, side="top")
    
        label_data = Label(scroll_frame, text=f"Data: {info[0]}")
        label_data.pack(side="top")

        label_tipo = Label(scroll_frame, text=f"Tipo: {info[1]}")
        label_tipo.pack(side="top")

        label_tempo = Label(scroll_frame, text=f"Tempo: {info[2]}")
        label_tempo.pack(side="top")

        label_movimentos = Label(scroll_frame, text=f"Movimentos: {','.join(info[3:])}")
        label_movimentos.pack(side="top")

        Button(scroll_frame,text="editar",command=lambda i=i: frame_editar(i)).pack(side="top")
        Button(scroll_frame,text="excluir  ",command=lambda i=i: excluir(i)).pack(side="top")

#cria o frame de edição
def frame_editar(treino_editado):
    global entry_dia_editando, entry_mes_editando, entry_ano_editando,entry_tempo_editando,entry_movimento_editando,editar,var_editando

    treinos = treinos_usuario(nome)

    info = treinos[treino_editado].split(",")

    data_lista = info[0].split("/")

    editar = Tk()

    editar.geometry("400x600")
    editar.title("editando")
    
    label_data_editado = Label(editar,text="Dia/mês/ano: ")
    label_data_editado.place(x=100,y=30)

    label_tempo_editando = Label(editar,text="tempo: ")
    label_tempo_editando.place(x=100,y=200)

    label_movimento_editando = Label(editar,text="movimentos: ")
    label_movimento_editando.place(x=70,y=250)

    entry_dia_editando = Entry(editar, width=3)
    entry_dia_editando.place(x=180,y=30)
    entry_dia_editando.insert(0,data_lista[0])
    Label(editar, text="/").place(x=200,y=30)

    entry_mes_editando = Entry(editar, width=3)
    entry_mes_editando.place(x=210,y=30)
    entry_mes_editando.insert(0,data_lista[1])
    Label(editar, text="/").place(x=230,y=30)

    entry_ano_editando = Entry(editar, width=5)
    entry_ano_editando.place(x=240,y=30)
    entry_ano_editando.insert(0,data_lista[2])
    
    var_editando = StringVar()
    var_editando.set("AMRAP")

    r1 = Radiobutton(editar, text="AMRAP", variable=var_editando, value = "teste1", command=lambda: set_editando(1))
    r2 = Radiobutton(editar, text="EMOM", variable=var_editando, value = "teste2", command=lambda: set_editando(2))
    r3 = Radiobutton(editar, text="for time", variable=var_editando, value="teste3", command=lambda: set_editando(3))

    if info[2] == "AMRAP":
        set_editando(1)
    elif info[2] == "EMOM":
        set_editando(2)
    elif info [3] == "for time":
        set_editando(3)

    r1.place(x=80,y=80)
    r2.place(x=150,y=80)
    r3.place(x=200,y=80)

    entry_tempo_editando = Entry(editar)
    entry_tempo_editando.place(x=150,y=200)
    entry_tempo_editando.insert(0,info[2])

    entry_movimento_editando = Entry(editar)
    entry_movimento_editando.place(x=150,y=250)

    Button(editar,text="editar movimento",command=adicao_movimentos).place(x=350,y=245)
    Button(editar,text="editar",command=lambda: editando(treino_editado)).place(x=200,y=300)

def set_editando(choose):

    match choose:
        case 1:
            var_editando.set("AMRAP")
        case 2:
            var_editando.set("EMOM")
        case 3:
            var_editando.set("for time")

def editando(treino_editado):
    
    linhas_novas = []
    
    data = entry_dia_editando.get() + "/" + entry_mes_editando.get() + "/" + entry_ano_editando.get()
    pratica = var_editando.get()
    tempo = entry_tempo_editando.get()

    movimento = adicao_movimentos()

    treino = data + "," + pratica + "," + tempo + movimento

    movimento = ""

    with open("valores.txt", "r") as f:

        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == nome:
               dados[treino_editado + 2] = treino
             
            linha =  ";".join(dados) + "\n"

        linhas_novas.append(linha)

    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)

    editar.destroy()
    visualizar.destroy()
    frame_visualizar()
    
#cria frame de exlusão
def excluir(i):

    linhas_novas = []

    with open("valores.txt", "r") as f:

        for linha in f:
            dados = linha.strip().split(";")

            if dados[0] == nome:
               dados.pop(i+2)
             
            linha =  ";".join(dados) + "\n"

        linhas_novas.append(linha)

    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)

    visualizar.destroy()
    frame_visualizar()



with open("valores.txt", "a") as f:
    pass

tela_cadastro = Tk() #Cria um frame de cadastro para a variavel cadastro que vai ser apagado depois

frame_login() #Executa a função da tela de login