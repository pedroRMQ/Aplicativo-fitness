import tkinter as tk

cadastro = tk.Tk()

def tela_login():
    global Entrada_nome_login, Entrada_senha_login, login


    login = tk.Tk()

    cadastro.destroy()

    login.title("Login")
    login.geometry("500x500")

    Entrada_nome_login = tk.Entry(login)
    Entrada_nome_login.pack(pady=10)

    Entrada_senha_login = tk.Entry(login, show="*")
    Entrada_senha_login.pack(pady=2)

    tk.Button(login,text="Login", command=inputs_login).pack(pady=10)

    link = tk.Label(login, text="Não sou cadastrado", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: necessita_cadastro())

    login.mainloop()

def necessita_cadastro():

    login.destroy()

    cadastro = tk.Tk()
    cadastro.title("cadastro")
    cadastro.geometry("500x500")

    Entrada_nome_cadastro = tk.Entry(cadastro)
    Entrada_nome_cadastro.pack(pady=10)

    Entrada_senha_cadastro = tk.Entry(cadastro)
    Entrada_senha_cadastro.pack(pady=2)

    tk.Button(cadastro,text="cadastro").pack(pady=10)

    link = tk.Label(cadastro, text="Ja tenho cadastro", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: tela_login())

    cadastro.mainloop()

def inputs_login():
    global password, nome

    nome = Entrada_nome_login.get()
    password = Entrada_senha_login.get()
    Entrada_nome_login.delete(0,tk.END)
    Entrada_senha_login.delete(0,tk.END)

tela_login()