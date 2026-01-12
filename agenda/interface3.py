import tkinter as tk
from agenda import Agenda
from contato import Contato
from tkinter import messagebox

janela = tk.Tk()
janela.geometry("300x200")
janela.title("MENU PRINCIPAL")


def listar_contatos():
    contatos = Agenda.listar_contatos()
    if not contatos:
        messagebox.showerror("erro", "Não há contatos adicionados")
        return

    janela3 = tk.Toplevel()
    janela3.geometry("300x200")
    janela3.title("Lista de Contatos")

    rolamento = tk.Scrollbar(janela3, orient="vertical")
    rolamento.pack(side="right", fill="y")

    canvas = tk.Canvas(janela3, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand="True")

    rolamento.config(command=canvas.yview)
    canvas.config(yscrollcommand=rolamento.set)

    rolamento_frame = tk.Frame(canvas)

    canvas_window = canvas.create_window((0, 0), window=rolamento_frame, anchor="nw")

    def ajustar_largura(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind("<Configure>", ajustar_largura)

    rolamento_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    for contato in contatos:
        frame_contato = tk.Frame(rolamento_frame)
        frame_contato.pack(padx=10, pady = 5, fill='x')

        texto_exibido =f"Nome:  {contato.nome} \n Telefone: {contato.telefone}"

        contato_listado = tk.Label(frame_contato, text=texto_exibido,justify = "left" , anchor ='w')
        contato_listado.pack(fill='x', side = "left", expand = "True")

        def remover_contato (c= contato, f = frame_contato):
            if messagebox.askyesno("Confirmar",f"Deseja apagar o contato {c.nome}?"):
                Agenda.apagar_contatos(c)
                f.destroy()
            messagebox.showinfo("Sucesso", "Contato apagado")

        botao_remover = tk.Button(frame_contato, text="X", fg="white", bg="red", command=remover_contato)
        botao_remover.pack(side="right", padx='5')

        framelinha = tk.Frame(rolamento_frame, height = 1, bg = "grey")
        framelinha.pack(fill="x",padx=5)

def criar_contato():
    janela2 = tk.Toplevel(janela)
    janela2.geometry("300x200")
    janela2.title("Adicionar")

    frame_nome = tk.Frame(janela2)
    frame_nome.pack(padx=5, pady = 10, fill='x')

    label_nome = tk.Label(frame_nome, text="Nome",anchor='w')
    label_nome.pack()

    nome_contato = tk.Entry(frame_nome)
    nome_contato.pack()

    frame_tel = tk.Frame(janela2)
    frame_tel.pack(padx=5, pady = 10, fill='x')

    label_tel = tk.Label(frame_tel, text="Telefone",anchor='w')
    label_tel.pack()

    numero_contato = tk.Entry(frame_tel)
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
        messagebox.showinfo("Sucesso", "Contato Adicionado")
        botao2.config(state="disabled")  # desativa
        janela2.destroy()

    botao2 = tk.Button(janela2, text="confirmar", command=adicionar)
    botao2.pack()

botao = tk.Button(janela, text="Adicionar", command=criar_contato)
botao.pack()

botao_adicionar = tk.Button(janela, text="Listar contatos", command=listar_contatos)
botao_adicionar.pack()
janela.mainloop()