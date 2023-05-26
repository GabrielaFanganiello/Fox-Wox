# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from sprites import *
from tela_inicial import tela_inicial
from tela_jogo import tela_jogo
from tela_instrucoes import tela_instrucoes
from tela_gameover_teste import tela_gameover_teste
from tela_pontuacao import tela_pontuacao

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARG, ALT))
pygame.display.set_caption('FOX & WOX')

state = INIT
while state != DONE:
    if state == INIT:
        state = tela_inicial(window)
    elif state == GAME:
        state = tela_jogo(window)
    elif state == INSTRUCOES:
        state = tela_instrucoes(window)
    elif state == GAMEOVER:
        state = tela_gameover_teste(window)
    elif state == PONTUACAO:
        state = tela_pontuacao(window)
    else:
        state = DONE

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados