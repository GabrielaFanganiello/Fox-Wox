import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *

# ---------- Tela Inicial ----------

def tela_inicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega as imagens
    assets = load_assets()

    # Criando botões
    all_buttons = pygame.sprite.Group()

    # Criando primeira fileira com 2 botões
    for i in range(2):
        # Botão de JOGO
        if i == 0:
            botao_jogo = Botao(assets, "Jogo")

            botao_jogo.rect.centerx = 3*LARG / 10
            botao_jogo.rect.centery = 2* ALT/3
            all_buttons.add(botao_jogo)

        # Botão de INSTRUÇÕES
        else:
            botao_instrucoes = Botao(assets, "Instruções")

            botao_instrucoes.rect.centerx = 7* LARG / 10
            botao_instrucoes.rect.centery = 2*ALT/3
            all_buttons.add(botao_instrucoes)
    
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            # Verifica se algum botão foi clicado
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in all_buttons:
                    if btn == botao_jogo:                           # Se o botão de JOGO for clicado, vai para a tela do jogo
                        if btn.rect.collidepoint(event.pos):
                                state = GAME
                                running = False
                    if btn == botao_instrucoes:                     # Se o botão de INSTRUÇÕES for clicado, vai para a tela de Instruções
                        if btn.rect.collidepoint(event.pos):  
                                state = INSTRUCOES
                                running = False

            # Verifica se o mouse está em cima de algum botão
            elif event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for btn in all_buttons:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)
            

        # A cada loop, redesenha o fundo e os botões
        screen.blit(assets[BACKGROUND], (0,0))
        all_buttons.draw(screen)


        # Escrevendo texto dos botões
        for btn in all_buttons:
            btn_texto = assets['font'].render(f"{btn.nome_do_jogo}", True, BRANCO)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)


        # Escrevendo o texto da tela
        tela_texto = assets['font_media'].render("FOX & WOX", True, BRANCO)
        text_rect = tela_texto.get_rect()
        text_rect.centerx = LARG / 2
        text_rect.centery = 200
        screen.blit(tela_texto, text_rect)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state