# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *
from tela_jogo import tela_jogo

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
screen = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption('FOX & WOX')

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_jogo(screen)
        with open('dados_pontuacao.txt', 'a') as arquivo:
            arquivo.write('{0}\n'.format(score))
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados