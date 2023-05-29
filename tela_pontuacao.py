import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *
from tela_jogo import *
from tela_nome import *        

def tela_pontuacao(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Lendo de linha em linha (note o plural em readlines)
        with open('pontuacao.txt', 'r') as arquivo:
            # linhas é uma lista de strings, cada linha é uma string diferente
            linhas = arquivo.readlines()
            for linha in linhas:
                linha.strip()
                print (linha)

            lista_pontuacoes = linhas[::2]
            lista_nomes = linhas[1::2]


        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYDOWN:
                state = VENCEDOR
                running = False
            
        screen.blit(assets[BACKGROUND], (0,0))

        nome = assets['font_media'].render("NOME: ", True, BRANCO)
        text_rect = nome.get_rect()
        text_rect.x = 50
        text_rect.centery = 50
        screen.blit(nome, text_rect)

        nomes = assets['font_media'].render("{0} ".format(lista_nomes), True, BRANCO)
        text_rect = nomes.get_rect()
        text_rect.x = 50
        text_rect.centery = 100
        screen.blit(nomes, text_rect)

        pontuacao = assets['font_media'].render("TEMPO:", True, BRANCO)
        text_rect = pontuacao.get_rect()
        text_rect.centerx = (LARG / 2) + 100
        text_rect.centery = 50
        screen.blit(pontuacao, text_rect)

        pontuacoes = assets['font_media'].render("{0}".format(lista_pontuacoes), True, BRANCO)
        text_rect = pontuacoes.get_rect()
        text_rect.centerx = (LARG / 2) + 100
        text_rect.centery = 100
        screen.blit(pontuacoes, text_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state