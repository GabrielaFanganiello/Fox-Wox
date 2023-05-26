import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *


def tela_gameover(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                state = GAME
                running = False
            
        screen.blit(assets[BACKGROUND], (0,0))

        tela_titulo = assets['font_media'].render("GAMEOVER:", True, BRANCO)
        text_rect = tela_titulo.get_rect()
        text_rect.centerx = LARG / 4
        text_rect.centery = 100
        screen.blit(tela_titulo, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state