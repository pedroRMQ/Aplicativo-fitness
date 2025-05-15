from tkinter import *#Importa todas as funções do tkinter sem precisar se referir ao tkinter antes da função 

def tela_login():
    global Entrada_nome_login, Entrada_senha_login, login #transforma as varaiveis do nome, senha e do frame de login em globais

    cadastro.destroy()#Apaga o frame do cadastro criado

    login = Tk()#Cria o frame de login 

    login.title("Login")#Defini o titulo da frame como login
    login.geometry("500x500")#Defini o tamanho do frame

    Entrada_nome_login = Entry(login)#Cria o input do nome do usuario
    Entrada_nome_login.pack(pady=10)#Defini a posição do input do nome 

    Entrada_senha_login = Entry(login, show="*")#cria o input da senha do usuario
    Entrada_senha_login.pack(pady=2)#Defini a posição do input da senha

    Button(login,text="Login", command=inputs_login).pack(pady=10)#Cria o botão para submeter os inputs

    link = Label(login, text="Não sou cadastrado", cursor="hand2")#cria o texto perguntado se é cadastrado
    link.pack()#defini a posição do texto
    link.bind("<Button-1>", lambda e: necessita_cadastro())#transforma o texto em um botão para redirecionar o usuario

    login.mainloop()#mantem a guia aberta 
    return cadastro

def necessita_cadastro():
    global cadastro#Transforma a variavel do frame em global

    login.destroy()#Destroi o frame de login

    cadastro = Tk()#Abre o frame transformando a varaivel cadastro em frame

    cadastro.title("cadastro")#Defini o titulo do frame como cadastro
    cadastro.geometry("500x500")#Defini o tamanho do frame 

    Entrada_nome_cadastro = Entry(cadastro)#Cria o espaço de input para o nome do usuario ser cadastrado
    Entrada_nome_cadastro.pack(pady=10)#Posiciona o espaço de input do nome do usuario

    Entrada_senha_cadastro = Entry(cadastro)#Cria o espaço de input para a senha do usuario ser cadastrada
    Entrada_senha_cadastro.pack(pady=2)#Posiona o espaço de input da senha do usurio

    Button(cadastro,text="cadastro").pack(pady=10)#Cria o botão para submeter os cadastros

    link = Label(cadastro, text="Ja tenho cadastro", cursor="hand2")#cria o texto para retornar ao frame de login
    link.pack()#Posiciona esse botão
    link.bind("<Button-1>", lambda e: tela_login())#Transforma esse texto em botão

    cadastro.mainloop()#mantem o frame aberto

def inputs_login():
    global password, nome#transforma em globais as varaiveis da senha e do nome

    nome = Entrada_nome_login.get() #Pega o nome colocado no login
    password = Entrada_senha_login.get() #Pega a senha colocada no login

    Entrada_nome_login.delete(0,END) #Apaga o texto escrito no nome
    Entrada_senha_login.delete(0,END) #Apaga o texto escrito no login
 
cadastro = Tk() #Cria um frame de cadastro para a variavel cadastro que vai ser apagada depois

tela_login() #Executa a função da tela de login