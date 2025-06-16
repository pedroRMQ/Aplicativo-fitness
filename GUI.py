from tkinter import *  # Importa todas as funções do tkinter
from Login import *
from Route import *

# Cria a interface de login
def frame_login():
    global Entrada_nome_login, Entrada_senha_login, tela_login 

    tela_login = Tk()
    tela_login.title("Login")
    tela_login.geometry("400x200")

    # Campos de entrada de nome e senha
    Entrada_nome_login = Entry(tela_login)
    Entrada_nome_login.place(x=150, y=50)

    Entrada_senha_login = Entry(tela_login, show="*")
    Entrada_senha_login.place(x=150, y=75)

    # Botão de login
    Button(tela_login, text="Login", command=inputs_login).place(x=185, y=100)

    # Link para tela de cadastro
    link = Label(tela_login, text="Não sou cadastrado", cursor="hand2")
    link.place(x=0, y=175)
    link.bind("<Button-1>", lambda e: frame_cadastro())

    tela_cadastro.destroy() 
    tela_login.mainloop()

# Cria a interface de cadastro
def frame_cadastro():
    global tela_cadastro, Entrada_nome_cadastro, Entrada_senha_cadastro 

    tela_cadastro = Tk()
    tela_cadastro.title("cadastro")
    tela_cadastro.geometry("400x200")

    # Campos de entrada de nome e senha
    Entrada_nome_cadastro = Entry(tela_cadastro)
    Entrada_nome_cadastro.place(x=150, y=50)

    Entrada_senha_cadastro = Entry(tela_cadastro)
    Entrada_senha_cadastro.place(x=150, y=75)

    # Botão de cadastro
    Button(tela_cadastro, text="cadastro", command=inputs_cadastro).place(x=185, y=100)

    # Link para tela de login
    link = Label(tela_cadastro, text="Já tenho cadastro", cursor="hand2")
    link.place(x=0, y=175)
    link.bind("<Button-1>", lambda e: frame_login())

    tela_login.destroy()
    tela_cadastro.mainloop()

# Recebe os inputs da tela de login
def inputs_login():
    global nome

    nome = Entrada_nome_login.get()
    senha = Entrada_senha_login.get()

    if verificar_login(nome, senha):
        frame_home()
    else:
        # Mensagem de erro se login falhar
        Label(tela_login, text="Senha ou nome incorreto", fg="red").place(x=140, y=125)
        Entrada_nome_login.delete(0, END)
        Entrada_senha_login.delete(0, END)

# Recebe os inputs da tela de cadastro
def inputs_cadastro():
    nome = Entrada_nome_cadastro.get()
    senha = Entrada_senha_cadastro.get()

    if usuario_existe(nome):
        Label(tela_cadastro, text="Esse usuario ja existe", fg="red").place(x=150, y=125)
    else:
        cadastrar_usuario(nome, senha)
        frame_login()

# Tela principal depois do login
def frame_home():
    global home, var1,var2,var3

    home = Tk()
    home.geometry("800x600")
    Label(home, text=f"Bem vindo {Entrada_nome_login.get()}, O que você deseja fazer hoje?").pack()

    # Botões principais
    Button(home, text="Adicionar", command=frame_adicionar).place(x=50, y=50)
    Button(home, text="Visualizar", command=frame_visualizar).place(x=150, y=50)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()

    # Tipos de treino
    Checkbutton(home, text="AMRAP", variable=var1, onvalue="AMRAP", offvalue="").place(x=80, y=80)
    Checkbutton(home, text="EMOM", variable=var2, onvalue="EMOM",offvalue="").place(x=150, y=80)
    Checkbutton(home, text="for time", variable=var3, onvalue="for time",offvalue="").place(x=200, y=80)

    tela_login.destroy()
    tela_cadastro.destroy()
    home.mainloop()

# Tela para adicionar novo treino
def frame_adicionar():
    global entry_dia, entry_mes, entry_ano, var, entry_movimento, entry_tempo,entry_metas, adicionar

    adicionar = Tk()
    adicionar.title("adicionar")
    adicionar.geometry("500x600")

    # Entradas de data, tipo de treino,metas e tempo
    entry_dia = Entry(adicionar, width=3); entry_dia.place(x=180, y=30)
    entry_mes = Entry(adicionar, width=3); entry_mes.place(x=210, y=30)
    entry_ano = Entry(adicionar, width=5); entry_ano.place(x=240, y=30)

    Label(adicionar, text="data: ").place(x=145, y=30)

    var = StringVar(); var.set("AMRAP")

    # Tipos de treino
    Radiobutton(adicionar, text="AMRAP", variable=var, value="teste1", command=lambda: set(1)).place(x=145, y=80)
    Radiobutton(adicionar, text="EMOM", variable=var, value="teste2", command=lambda: set(2)).place(x=210, y=80)
    Radiobutton(adicionar, text="for time", variable=var, value="teste3", command=lambda: set(3)).place(x=270, y=80)
    
    Label(adicionar, text="Tipo de treino: ").place(x=65,y=82)

    entry_metas = Entry(adicionar); entry_metas.place(x=150, y=120)
    entry_tempo = Entry(adicionar); entry_tempo.place(x=150, y=170)
    entry_movimento = Entry(adicionar); entry_movimento.place(x=150, y=220)

    Label(adicionar, text="Meta: ").place(x=110,y=120)
    Label(adicionar, text="Tempo: ").place(x=100,y=170)
    Label(adicionar, text="Movimentos: ").place(x=70,y=220)

    treino = treinos_usuario(nome)
    if len(treino) == 1:
        Label(adicionar, text="Sugestão de treino: ").place(x=80,y=300)
        Label(adicionar, text="Tipo: AMRAP ").place(x=110,y=330)
        Label(adicionar, text="Tempo: 10 minutos ").place(x=110,y=360)
        Label(adicionar, text="Movimentos: ").place(x=110,y=390)
        Label(adicionar, text="10 burpees").place(x=150,y=420)
        Label(adicionar, text="20 air squats").place(x=150,y=450)
        Label(adicionar, text="15 sit-ups").place(x=150,y=480)
    elif len(treino) == 2:
        Label(adicionar, text="Sugestão de treino: ").place(x=80,y=300)
        Label(adicionar, text="Tipo: EMOM ").place(x=110,y=330)
        Label(adicionar, text="Tempo: 12 minutos ").place(x=110,y=360)
        Label(adicionar, text="Movimentos: Repetir").place(x=110,y=390)
        Label(adicionar, text="10 push-ups").place(x=150,y=420)
        Label(adicionar, text="12 kettlebell swings").place(x=150,y=450)
        Label(adicionar, text="15 jumping jacks").place(x=150,y=480)
    elif len(treino) == 3:
        Label(adicionar, text="Sugestão de treino: ").place(x=80,y=300)
        Label(adicionar, text="Tipo: AMRAP ").place(x=110,y=330)
        Label(adicionar, text="Tempo: 10 minutos ").place(x=110,y=360)
        Label(adicionar, text="Movimentos: ").place(x=110,y=390)
        Label(adicionar, text="10 burpees").place(x=150,y=420)
        Label(adicionar, text="20 air squats").place(x=150,y=450)
        Label(adicionar, text="15 sit-ups").place(x=150,y=480)
    elif len(treino) > 3:
        Label(adicionar, text="Sugestão de treino: ").place(x=80,y=300)
        Label(adicionar, text="Tipo: For time: ").place(x=110,y=330)
        Label(adicionar, text="Tempo: O mais rapido possivel ").place(x=110,y=360)
        Label(adicionar, text="Movimentos: 21-15-9 reps de: ").place(x=110,y=390)
        Label(adicionar, text="Pull-ups").place(x=150,y=420)
        Label(adicionar, text="Thrusters").place(x=150,y=450)

    Button(adicionar, text="adicionar movimento", command=adicao_movimentos).place(x=350, y=215)
    Button(adicionar, text="Concluir", command=input_adicionar).place(x=200, y=270)

# Define tipo de treino
def set(choose):
    match choose:
        case 1: var.set("AMRAP")
        case 2: var.set("EMOM")
        case 3: var.set("for time")

# Adiciona movimentos ao treino
def adicao_movimentos():
    global movimento
    try:
        movimento += "," + entry_movimento.get()
        entry_movimento.delete(0, END)
    except:
        movimento += "," + entry_movimento_editando.get()
        entry_movimento_editando.delete(0, END)
    return movimento

# Processa entrada de treino novo
def input_adicionar():
    global movimento
    data = entry_dia.get() + "/" + entry_mes.get() + "/" + entry_ano.get()
    pratica = var.get()
    tempo = entry_tempo.get()
    metas = entry_metas.get()
    movimento = adicao_movimentos()
    treino = data + "," + pratica + "," + tempo + "," +metas + movimento

    movimento = ""
    substituir(nome, treino)
    adicionar.destroy()

# Tela de visualização dos treinos
def frame_visualizar():
    global visualizar

    visualizar = Tk()
    visualizar.geometry("400x400")
    visualizar.title("Seus treinos")

    # Scroll
    canvas = Canvas(visualizar)
    scrollbar = Scrollbar(visualizar, orient="vertical", command=canvas.yview)
    scroll_frame = Frame(visualizar)
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    treinos = treinos_usuario(nome)

    filtro = [var1.get(),var2.get(),var3.get()]

    for i, treino in enumerate(treinos):
        print(var1.get(),var2.get(),var3.get())
        info = treino.split(",")
        if info == ['']: break

        if info[1] not in filtro:
            continue
        
        Label(scroll_frame, text=f"Treino {i+1}: ", font=("Arial", 10)).pack(pady=20)
        Label(scroll_frame, text=f"Data: {info[0]}").pack()
        Label(scroll_frame, text=f"Tipo: {info[1]}").pack()
        Label(scroll_frame, text=f"Tempo: {info[2]}").pack()
        Label(scroll_frame, text=f"Metas: {info[3]}").pack()
        Label(scroll_frame, text=f"Movimentos: {','.join(info[4:])}").pack()

        Button(scroll_frame, text="editar", command=lambda i=i: frame_editar(i)).pack()
        Button(scroll_frame, text="excluir", command=lambda i=i: excluir(i)).pack()

# Tela de edição de treino
def frame_editar(treino_editado):
    global entry_dia_editando, entry_mes_editando, entry_ano_editando, entry_tempo_editando, entry_meta_editando, entry_movimento_editando, editar, var_editando

    treinos = treinos_usuario(nome)
    info = treinos[treino_editado].split(",")
    data_lista = info[0].split("/")

    editar = Tk()
    editar.geometry("500x500")
    editar.title("editando")

    entry_dia_editando = Entry(editar, width=3); entry_dia_editando.place(x=180, y=30); entry_dia_editando.insert(0, data_lista[0])
    entry_mes_editando = Entry(editar, width=3); entry_mes_editando.place(x=210, y=30); entry_mes_editando.insert(0, data_lista[1])
    entry_ano_editando = Entry(editar, width=5); entry_ano_editando.place(x=240, y=30); entry_ano_editando.insert(0, data_lista[2])

    Label(editar, text="data: ").place(x=145, y=30)

    var_editando = StringVar(); var_editando.set("AMRAP")

    Radiobutton(editar, text="AMRAP", variable=var_editando, value="teste1", command=lambda: set_editando(1)).place(x=145, y=80)
    Radiobutton(editar, text="EMOM", variable=var_editando, value="teste2", command=lambda: set_editando(2)).place(x=210, y=80)
    Radiobutton(editar, text="for time", variable=var_editando, value="teste3", command=lambda: set_editando(3)).place(x=270, y=80)

    Label(editar, text="Tipo de treino: ").place(x=65,y=82)

    entry_meta_editando = Entry(editar); entry_meta_editando.place(x=150,y=120)
    entry_tempo_editando = Entry(editar); entry_tempo_editando.place(x=150, y=170); entry_tempo_editando.insert(0, info[2])
    entry_movimento_editando = Entry(editar); entry_movimento_editando.place(x=150, y=220)

    Label(editar, text="Meta: ").place(x=110,y=120)
    Label(editar, text="Tempo: ").place(x=100,y=170)
    Label(editar, text="Movimentos: ").place(x=70,y=220)

    Button(editar, text="editar movimento", command=adicao_movimentos).place(x=350, y=215)
    Button(editar, text="editar", command=lambda: editando(treino_editado)).place(x=200, y=270)

def set_editando(choose):
    match choose:
        case 1: var_editando.set("AMRAP")
        case 2: var_editando.set("EMOM")
        case 3: var_editando.set("for time")

# Atualiza um treino já existente
def editando(treino_editado):
    global movimento
    data = entry_dia_editando.get() + "/" + entry_mes_editando.get() + "/" + entry_ano_editando.get()
    pratica = var_editando.get()
    tempo = entry_tempo_editando.get()
    meta = entry_meta_editando.get()
    movimento = adicao_movimentos()
    treino = data + "," + pratica + "," + tempo + "," + meta +movimento
    movimento = ""

    linhas_novas = []
    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")
            if dados[0] == nome:
                dados[treino_editado + 2] = treino
            linhas_novas.append(";".join(dados) + "\n")

    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)

    editar.destroy()
    visualizar.destroy()
    frame_visualizar()

# Exclui um treino
def excluir(i):
    linhas_novas = []

    with open("valores.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(";")
            if dados[0] == nome:
                dados.pop(i+2)
            linhas_novas.append(";".join(dados) + "\n")

    with open("valores.txt", "w") as f:
        f.writelines(linhas_novas)

    visualizar.destroy()
    frame_visualizar()

# Garante que o arquivo exista
with open("valores.txt", "a") as f:
    pass

movimento = ""
tela_cadastro = Tk()  # Tela inicial apagada de propósito
frame_login()  # Inicia a interface de login