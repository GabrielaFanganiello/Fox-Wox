import pygame
import random
from os import path
from config import *
from assets import *

def tela_gameover_teste(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Carrega o fundo da tela inicial
    gameover = assets[BACKGROUND]
    gameover_rect = gameover.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYUP:
                state = INIT
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(PRETO)
        screen.blit(gameover, gameover_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state