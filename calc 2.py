from tkinter import Tk, Button, Entry, font

# Função para realizar os cálculos
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, 'end')
        entrada.insert('end', str(resultado))
    except Exception as e:
        entrada.delete(0, 'end')
        entrada.insert('end', 'Erro')

# Função para apagar o último caractere
def apagar():
    expressao = entrada.get()
    expressao = expressao[:-1]
    entrada.delete(0, 'end')
    entrada.insert('end', expressao)

# Configurações da janela principal
janela = Tk()
janela.title('Calculadora')
janela.configure(bg='#303030')
janela.geometry('400x400')
janela.resizable(0, 0)

# Configurações da fonte
fonte = font.Font(family='Roboto', size=16)

# Configurações da entrada de texto
entrada = Entry(janela, width=20, font=fonte, justify='right', bg='#303030', fg='white')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Configurações dos botões
botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i in range(len(botoes)):
    for j in range(len(botoes[i])):
        botao = Button(janela, text=botoes[i][j], width=5, font=fonte, bg='#424242', fg='white',
                       activebackground='#FFCC00', activeforeground='#303030',
                       command=lambda x=botoes[i][j]: entrada.insert('end', x))
        botao.grid(row=i+1, column=j, padx=5, pady=5)

# Botão de apagar
botao_apagar = Button(janela, text='Apagar', width=10, font=fonte, bg='#424242', fg='white',
                      activebackground='#FFCC00', activeforeground='#303030',
                      command=apagar)
botao_apagar.grid(row=len(botoes)+1, column=0, padx=10, pady=10)

# Botão de calcular
botao_calcular = Button(janela, text='Calcular', width=10, font=fonte, bg='#FFCC00', fg='#303030',
                        activebackground='#FFCC00', activeforeground='#303030',
                        command=calcular)
botao_calcular.grid(row=len(botoes)+1, column=1, columnspan=3, padx=10, pady=10)

# Iniciar a janela
janela.mainloop()
