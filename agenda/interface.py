import tkinter as tk 

#instanciar a janela 
janela = tk.Tk()
janela.title("AGENDA DE CONTATOS")
janela.geometry("500x400+200+200")
janela.config(bg="cadet blue")

#criar e posicionar um label com a mensagem

lblMsg = tk.Label(janela, text="Ola Pessoal")
lblMsg.pack()

#exibir a janela 
janela.mainloop()