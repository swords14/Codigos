import tkinter as tk
import time
import threading
import colorama
from colorama import init, Fore
from pyfiglet import Figlet

def animate_text():
    # Configurações da animação
    init(autoreset=True)
    f = Figlet(font='slant')
    message = "eu te amei muito antes de te beijar"

    # Animação das letras
    for char in message:
        print(Fore.RED + f.renderText(char))
        time.sleep(0.2)

def create_romantic_interface():
    # Configurações da janela
    window = tk.Tk()
    window.title("Aniversário de namoro")
    window.geometry("600x400")
    window.configure(bg="#FFC0CB")  # Cor de fundo rosa claro

    # Fonte personalizada
    custom_font = ('Segoe Script', 20, 'bold')

    # Rótulo com a mensagem romântica
    label = tk.Label(window, text="Feliz Aniversário de\n2 anos de namoro!", font=custom_font, bg="#FFC0CB", fg="#8B0000")
    label.pack(pady=50)

    # Thread para animação
    anim_thread = threading.Thread(target=animate_text)
    anim_thread.start()

    # Execução da janela
    window.mainloop()

# Chamada da função principal
create_romantic_interface()