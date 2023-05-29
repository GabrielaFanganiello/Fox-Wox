import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *
from tela_jogo import *
from tela_nome import *        

pontuados = {}
lista_nomes = []
lista_pontos = []

def tela_pontuacao(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    running = True

    # Carrega música de fundo
    pygame.mixer.music.play(loops=-1)


    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Lendo de linha em linha (note o plural em readlines)
        with open('pontuacao.txt', 'r') as arquivo:
            # linhas é uma lista de strings, cada linha é uma string diferente
            linhas = arquivo.read()
            linhas = linhas.split(' ')

            lista_pontuacoes = linhas[:-1:2]
            lista_nome = linhas[1::2]

            for i in range(len(lista_pontuacoes)):
                pontuados[lista_nome[i]] = int(lista_pontuacoes[i])

            for i in sorted(pontuados, key = pontuados.get):
                if i not in lista_nomes:
                    lista_nomes.append(i)
                    lista_pontos.append(pontuados[i])
                else:
                    continue

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYDOWN:
                state = VENCEDOR
                running = False
        
        # Carrega imagem de fundo
        screen.blit(assets[BACKGROUND], (0,0))

        # Desenha as colunas de nome e pontuacao na tela 
        nome = assets['font_media'].render("NOME: ", True, BRANCO)
        text_rect = nome.get_rect()
        text_rect.x = 50
        text_rect.centery = 50
        screen.blit(nome, text_rect)

        pontuacao = assets['font_media'].render("PONTUAÇÃO:", True, BRANCO)
        text_rect = pontuacao.get_rect()
        text_rect.centerx = (LARG / 2) + 100
        text_rect.centery = 50
        screen.blit(pontuacao, text_rect)

        cont_nome = 0

        # Escreve os nomes e pontuaçOes dos jogadores
        for nome in lista_nomes:
            nomes = assets['font_media'].render("{0} ".format(nome), True, BRANCO)
            text_rect = nomes.get_rect()
            text_rect.x = 50
            text_rect.centery = 100 + cont_nome
            screen.blit(nomes, text_rect)

            cont_nome += 60

        cont_pont = 0
        for pontuacao in lista_pontos:
            pontuacoes = assets['font_media'].render("{0}".format(pontuacao), True, BRANCO)
            text_rect = pontuacoes.get_rect()
            text_rect.centerx = (LARG / 2) + 100
            text_rect.centery = 100 + cont_pont
            screen.blit(pontuacoes, text_rect)

            cont_pont += 60
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state