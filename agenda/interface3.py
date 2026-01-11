import tkinter as tk 
from tkinter import ttk

janela = tk.Tk()
janela.geometry("400x300")
janela.title("uso de label")

#criar label

label = ttk.Label(
      janela,
      text="aula de labels",
      font=("Helvetica", 18)
      )

label.pack(ipadx=10, ipady=30)


label2 = ttk.Label(
    janela, 
    text="texto 2",
    font=("Arial", 20),
    foreground="blue"

)

label2.pack(ipadx=10, ipady=60)

janela.mainloop()