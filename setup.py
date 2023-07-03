import tkinter as tk
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

def mostrar_amor():
    messagebox.showinfo("Amor", "Eu te amo até o infinito mesmo você sendo chatinha!")

janela = tk.Tk()
janela.title("Cálculo de Amor")
janela.geometry("1000x600")
janela.configure(bg="#9900cc")

# Define uma fonte personalizada
fonte_personalizada = font.Font(family="Pacifico", size=40)

label_titulo = tk.Label(janela, text="Cálculo de Amor", font=fonte_personalizada, bg="#9900cc", fg="white")
label_titulo.pack(pady=50)

botao = tk.Button(janela, text="Mostrar Amor", command=mostrar_amor, bg="#660099", fg="white", font=("Arial", 24))
botao.pack(pady=100)

janela.mainloop()
def exibir_mensagem():
    agora = datetime.now()
    dia = agora.day
    mes = agora.month
    ano = agora.year
    hora = agora.hour
    minuto = agora.minute
    mensagem = f"Olá amor! Hoje é {dia}/{mes}/{ano} e são {hora}:{minuto}. Quero aproveitar esse momento para dizer o quanto você é especial para mim. Te amo muito!"
    label["text"] = mensagem

janela = tk.Tk()
janela.title("Mensagem para minha namorada")

label = tk.Label(janela, font=("Arial", 12))
label.pack(pady=20)

botao = tk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao.pack()

janela.mainloop()
