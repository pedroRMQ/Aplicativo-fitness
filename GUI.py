from tkinter import *#Importa todas as funções do tkinter sem precisar se referir ao tkinter antes da função 

#cria o frame de login
def frame_login():
    global Entrada_nome_login, Entrada_senha_login, login 

    cadastro.destroy() 

    login = Tk()
    
    login.title("Login")
    login.geometry(f"400x200")

    label_nome = Label(login,text="Nome: ")
    label_nome.place(x=100,y=50)

    label_senha = Label(login,text="Senha: ")
    label_senha.place(x=100,y=75)

    Entrada_nome_login = Entry(login)
    Entrada_nome_login.place(x=150,y=50)

    Entrada_senha_login = Entry(login, show="*")
    Entrada_senha_login.place(x=150,y=75)

    Button(login,text="Login", command=inputs_login).place(x=185,y=100)

    link = Label(login, text="Não sou cadastrado", cursor="hand2")
    link.place(x=0,y=175)
    link.bind("<Button-1>", lambda e: tela_cadastro())

    login.mainloop()

#cria o frame de cadastro
def tela_cadastro():
    global cadastro

    login.destroy()

    cadastro = Tk()

    cadastro.title("cadastro")
    cadastro.geometry("400x200")

    label_nome = Label(cadastro,text="Nome: ")
    label_nome.place(x=100,y=50)

    label_senha = Label(cadastro,text="Senha: ")
    label_senha.place(x=100,y=75)

    Entrada_nome_cadastro = Entry(cadastro)#Cria o espaço de input para o nome do usuario ser cadastrado
    Entrada_nome_cadastro.place(x=150,y=50)#Posiciona o espaço de input do nome do usuario

    Entrada_senha_cadastro = Entry(cadastro)#Cria o espaço de input para a senha do usuario ser cadastrada
    Entrada_senha_cadastro.place(x=150,y=75)#Posiona o espaço de input da senha do usurio

    Button(cadastro,text="cadastro").place(x=185,y=100)#Cria o botão para submeter os cadastros

    link = Label(cadastro, text="Já tenho cadastro", cursor="hand2")#cria o texto para retornar ao frame de login
    link.place(x=0,y=175)#Posiciona esse botão
    link.bind("<Button-1>", lambda e: frame_home())#Transforma esse texto em botão

    cadastro.mainloop()#mantem o frame aberto

#controla os inputs
def inputs_login():
    global password, nome#transforma em globais as varaiveis da senha e do nome

    nome = Entrada_nome_login.get() #Pega o nome colocado no login
    password = Entrada_senha_login.get() #Pega a senha colocada no login

    Entrada_nome_login.delete(0,END) #Apaga o texto escrito no nome
    Entrada_senha_login.delete(0,END) #Apaga o texto escrito no login

#cria o frame inicial
def frame_home():
    global home

    home = Tk() 

    Label(home,text="Bem vindo usuario, Oque você deseja fazer hoje?").pack()

    home.geometry("800x600")

    Button(home,text="Adicionar", command=frame_adicionar).place(x=50,y=50)
    Button(home,text="Visualizar", command=frame_visualizar).place(x=150,y=50)
    Button(home,text="Editar", command=frame_editar).place(x=250,y=50)
    Button(home,text="Excluir",command=frame_excluir).place(x=350,y=50)

    cadastro.destroy()
    login.destroy()

#cria o frame da opção de adicionar treino
def frame_adicionar():

    adicionar = Tk()

    adicionar.title("adicionar")
    adicionar.geometry("500x500")
    
    label_dia = Label(adicionar,text="Dia: ")
    label_dia.place(x=100,y=0)

    label_mes = Label(adicionar,text="mês: ")
    label_mes.place(x=100,y=50)

    label_ano = Label(adicionar,text="ano: ")
    label_ano.place(x=100,y=100)

    label_tempo = Label(adicionar,text="tempo: ")
    label_tempo.place(x=100,y=200)

    label_movimento = Label(adicionar,text="movimentos: ")
    label_movimento.place(x=70,y=250)

    dia = Entry(adicionar)
    dia.place(x=150,y=0)

    mes = Entry(adicionar)
    mes.place(x=150,y=50)

    ano = Entry(adicionar)
    ano.place(x=150,y=100)
    
    op1 = IntVar()
    op2 = IntVar()
    op3 = IntVar()

    check1 = Checkbutton(adicionar, text="AMRAP", variable=op1)
    check2 = Checkbutton(adicionar, text="EMOM", variable=op2)
    check3 = Checkbutton(adicionar, text="for time", variable=op3)

    check1.place(x=100,y=150)
    check2.place(x=150,y=150)
    check3.place(x=200,y=150)

    tempo = Entry(adicionar)
    tempo.place(x=150,y=200)

    movimento = Entry(adicionar)
    movimento.place(x=150,y=250)

    Button(adicionar,text="adicionar movimento").place(x=350,y=245)
    Button(adicionar,text="Concluir").place(x=200,y=300)

#cria o frame de visualizar os treinos
def frame_visualizar():

    visualizar = Tk()

    visualizar.geometry("400x600")

#cria o frame de edição
def frame_editar():

    editar = Tk()

    editar.geometry("400x600")

#cria frame de exlusão
def frame_excluir():

    excluir = Tk()

    excluir.geometry("400x600")


cadastro = Tk() #Cria um frame de cadastro para a variavel cadastro que vai ser apagado depois

frame_login() #Executa a função da tela de login