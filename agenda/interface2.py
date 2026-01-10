import tkinter as tk 

def abrir_segunda_janela():
    segunda_janela = tk.Toplevel()
    segunda_janela.title("SEGUNDA JANELA")
    segunda_janela.config(bg="black")

    #tamanho da janela
    largura_janela = 300
    altura_janela = 200

    #obter as dimensoes da tela do monitor

    largura_tela = segunda_janela.winfo_screenwidth()
    altura_tela = segunda_janela.winfo_screenwidth()

    #calcular as coordenadas para centralizar a janela 2
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2


    #definir a geometria da janela 2
    segunda_janela.geometry(f"{largura_janela} x {altura_janela} + {x} + {y}")


#criar janela principal

janela_principal = tk.Tk()
janela_principal.title("janela principal")
janela_principal.geometry("600x500")
#configurar evento de clique na janela principal

janela_principal.bind("<Button-1>", lambda event: abrir_segunda_janela())

janela_principal.mainloop()