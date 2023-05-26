import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *

def tela_instrucoes(screen):
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

        
        # A cada loop, redesenha o fundo
        screen.blit(assets[INSTRUCOES], (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state