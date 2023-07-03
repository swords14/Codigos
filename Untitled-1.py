import tkinter as tk
from tkinter import messagebox

def mostrar_amor():
    messagebox.showinfo("Amor", "Eu amo minha namorada Tainara em 100%!")

janela = tk.Tk()
janela.title("Cálculo de Amor")
janela.geometry("800x600")
janela.configure(bg="#9900cc")

label_titulo = tk.Label(janela, text="Cálculo de Amor", font=("Arial", 40), bg="#9900cc", fg="white")
label_titulo.pack(pady=50)

botao = tk.Button(janela, text="Mostrar Amor", command=mostrar_amor, bg="#660099", fg="white", font=("Arial", 24))
botao.pack(pady=100)

janela.mainloop()
