import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *

jogadores = []

def tela_nome(screen):
    nome = ''

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    botoes_nome = pygame.sprite.Group()

    ativado = False

    # Criando primeira fileira com 1 botões
    for i in range(1):
        botao_nome = Botao(assets, "NOME")

        botao_nome.rect.centerx = LARG / 2
        botao_nome.rect.centery = ALT / 2
        botoes_nome.add(botao_nome)

    done = False
    while not done:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_nome.rect.collidepoint(event.pos):
                    ativado = not ativado

                else: 
                    ativado = False

            if event.type == pygame.KEYDOWN:
                if ativado:
                    botao_nome.mouse_over(True)

                    if event.key == pygame.K_RETURN:
                        jogadores.append(nome)
                        state = GAMEOVER
                        done = True
                        print(jogadores)
                        nome = ''

                    elif event.key == pygame.K_BACKSPACE:
                        nome = nome[:-1]

                    else:
                        nome += event.unicode


        screen.blit(assets[BACKGROUND], (0,0))

        txt_surface = assets['font_media'].render(nome, True, BRANCO)
        botoes_nome.draw(screen)
        screen.blit(txt_surface, botao_nome)


        tela_titulo = assets['font_media'].render("INSIRA O NOME DOS JOGADORES:", True, BRANCO)
        text_rect = tela_titulo.get_rect()
        text_rect.x = 0
        text_rect.centery = 100
        screen.blit(tela_titulo, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state