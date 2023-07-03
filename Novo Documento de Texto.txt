import tkinter as tk
from datetime import datetime

# Função para obter a data e hora atual e exibir a mensagem
def exibir_mensagem():
    agora = datetime.now()
    dia = agora.day
    mes = agora.month
    ano = agora.year
    hora = agora.hour
    minuto = agora.minute
    mensagem = f"Olá amor! Hoje é {dia}/{mes}/{ano} e são {hora}:{minuto}. Quero aproveitar esse momento para dizer o quanto você é especial para mim. Te amo muito!"
    label["text"] = mensagem

# Criação da janela
janela = tk.Tk()
janela.title("Mensagem para minha namorada")

# Criação do rótulo para exibir a mensagem
label = tk.Label(janela, font=("Arial", 12))
label.pack(pady=20)

# Criação do botão para exibir a mensagem
botao = tk.Button(janela, text="Exibir mensagem", command=exibir_mensagem)
botao.pack()

# Execução da janela
janela.mainloop()