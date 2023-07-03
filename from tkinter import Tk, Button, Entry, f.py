from tkinter import Tk, Button, Entry, font


def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, 'end')
        entrada.insert('end', str(resultado))
    except Exception as e:
        entrada.delete(0, 'end')
        entrada.insert('end', 'Erro')

janela = Tk()
janela.title('Calculadora')
janela.configure(bg='#333333')
janela.geometry('300x400')
janela.resizable(0, 0)


fonte = font.Font(family='Arial', size=14)


entrada = Entry(janela, width=20, font=fonte, justify='right', bg='#333333', fg='white')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


botoes = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for i in range(len(botoes)):
    for j in range(len(botoes[i])):
        botao = Button(janela, text=botoes[i][j], width=5, font=fonte, bg='#222222', fg='white',
                       command=lambda x=botoes[i][j]: entrada.insert('end', x))
        botao.grid(row=i+1, column=j, padx=5, pady=5)


botao_calcular = Button(janela, text='Calcular', width=10, font=fonte, bg='#222222', fg='white',
                        command=calcular)
botao_calcular.grid(row=len(botoes)+1, column=0, columnspan=4, padx=10, pady=10)


janela.mainloop()
