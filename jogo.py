# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import LARG, ALT, INIT, QUIT, GAME
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption('FOX & WOX')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicial(window)
    elif state == GAME:
        state = tela_jogo(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados