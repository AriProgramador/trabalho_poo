import tkinter as tk

itens = ["arroz", "feijao", "macarrao"]

janela = tk.Tk()
janela.title("Exemplo de Listbox")

lista = tk.Listbox(
    janela,
    width=400,   # mais larga
    height=500   # mais alta
)
lista.pack(padx=10, pady=10)

# adicionando os itens na Listbox
for item in itens:
    lista.insert(tk.END, item)

janela.mainloop()
