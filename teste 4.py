import pygame
import sys
from pygame.locals import *

# Configurações da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animação de um Coração com Mensagem")
clock = pygame.time.Clock()

# Cores
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)

# Inicia o Pygame
pygame.init()

# Função para desenhar um arco de círculo
def draw_arc():
    for _ in range(90):
        pygame.draw.line(screen, PURPLE, (heart_x, heart_y), (heart_x + 2, heart_y + 2))
        pygame.display.flip()
        heart_x += 2
        heart_y += 2

# Desenha o coração
def draw_heart():
    draw_arc()
    pygame.display.flip()
    pygame.time.wait(300)
    heart_x, heart_y = 0, 0
    draw_arc()
    pygame.display.flip()
    pygame.time.wait(300)
    heart_x, heart_y = 0, 0
    draw_arc()
    pygame.display.flip()

# Exibe a mensagem
def display_message():
    font = pygame.font.Font(None, 32)
    text = font.render("Posso jogar um LoLzin hoje?", True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# Loop principal do jogo
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        draw_heart()
        display_message()

        pygame.time.wait(3000)  # Tempo para exibir a mensagem

        running = False

        pygame.display.flip()
        clock.tick(60)

# Inicia o jogo
game_loop()
turtle.mainloop()