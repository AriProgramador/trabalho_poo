import tkinter as tk
from tkinter import messagebox
from agenda import Agenda
agenda = None

def criar_agenda():
    nome_da_agenda = entry_agenda.get()
    if nome_da_agenda == "":
        messagebox.showerror("erro", "nome da agenda nao pode estar vazio")
        return 
    agenda = Agenda(nome_da_agenda)
    label.pack_forget()
    entry_agenda.pack_forget()
    botao.pack_forget()

    label_resultado.config(
        text=f"Agenda '{nome_da_agenda}' criada com sucesso!"
          )
def adicionar_evento():
    try:
        contato = Contato(
            entry_nome_contato.get(), entry_telefone.get()
        )

        evento = Evento(
            entry_nome_evento.get(), 
            entry_data.get(),
            entry_hora.get(), 
            contato
        )
        agenda.adicionar_evento(evento)
        listbox.insert(tk.END, evento)

    except Exception as erro:
        messagebox.showerror("erro", erro)

janela = tk.Tk()
janela.title("Criador de Agendas")
janela.geometry("800x600")
janela.resizable(False, False)


label = tk.Label(janela, text="BEM VINDO! DIGITE O NOME DA AGENDA")
label.pack()

entry_agenda = tk.Entry(janela)
entry_agenda.pack()

botao = tk.Button(janela, text="confirmar", command=criar_agenda)
botao.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()



janela.mainloop()