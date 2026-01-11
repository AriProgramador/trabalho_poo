import tkinter as tk 
from agenda import Agenda
from contato import Contato
from tkinter import messagebox


janela = tk.Tk()
janela.geometry("300x200")
janela.title("MENU PRINCIPAL")

def listar_contatos():
    janela3 = tk.Toplevel()
    janela3.geometry("300x200")
    janela3.title("Lista de Contatos")

 
def criar_contato():

    janela2 = tk.Toplevel(janela)
    janela2.geometry("300x200")
    janela2.title("Adicionar")

    nome_contato = tk.Entry(janela2)
    nome_contato.pack()

    numero_contato = tk.Entry(janela2)
    numero_contato.pack()

    def adicionar():
        nome_pego = nome_contato.get()
        numero_pego = numero_contato.get()

        if nome_pego == "":
            messagebox.showerror("erro", "nome do contato nao pode estar vazio!")
            return
    
        if len(numero_pego) != 8:
            messagebox.showerror("erro", "o numero deve conter 8 digitos") 
            return
    
        
        Agenda.adicionar_contato(Contato(nome_pego, numero_pego))
        messagebox.showinfo("Sucesso","Contato Adicionado")
        botao2.config(state="disabled")  # desativa

    botao2 = tk.Button(janela2, text="confirmar", command=adicionar)  
    botao2.pack()

botao = tk.Button(janela, text="adicionar", command=criar_contato)
botao.pack()

botao_adicionar = tk.Button(janela, text="listar contatos", command=listar_contatos )
botao_adicionar.pack()
janela.mainloop()