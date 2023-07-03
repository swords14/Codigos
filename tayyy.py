import tkinter as tk
from tkinter import messagebox

def exibir_mensagem():
    mensagem = entrada.get()
    messagebox.showinfo("Mensagem Romântica", mensagem)

# Configurações da janela
janela = tk.Tk()
janela.title("Interface Romântica")
janela.geometry("400x200")

# Imagem de fundo
imagem_fundo = tk.PhotoImage(file="background.png")
fundo_label = tk.Label(janela, image=imagem_fundo)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configurações dos widgets
titulo_label = tk.Label(janela, text="Mensagem Romântica", font=("Arial", 16, "bold"), bg="pink")
titulo_label.pack(pady=10)

entrada = tk.Entry(janela, font=("Arial", 12))
entrada.pack(pady=10)

botao = tk.Button(janela, text="Exibir", font=("Arial", 12), command=exibir_mensagem, bg="lightpink")
botao.pack(pady=10)

# Execução da interface
janela.mainloop()
