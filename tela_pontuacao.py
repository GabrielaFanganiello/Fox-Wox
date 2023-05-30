import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *
from tela_jogo import *
from tela_nome import *

pontuados = {}
lista_nomes_final = []
lista_pontos_final = []

# Se os jogador quiser, ele pode ver a pontuação dos jogadores
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

            lista_das_pontuacoes = linhas[:-1:2]
            lista_dos_nomes = linhas[1::2]

            for i in range(len(lista_das_pontuacoes)):
                if lista_dos_nomes[i] not in pontuados.keys():
                    pontuados[lista_dos_nomes[i]] = int(lista_das_pontuacoes[i])

                else:
                    if pontuados[lista_dos_nomes[i]] > int(lista_das_pontuacoes[i]):
                        pontuados[lista_dos_nomes[i]] = int(lista_das_pontuacoes[i])

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
        screen.blit(assets[BACKGROUND], (0, 0))

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

        sorted_dict = sorted(pontuados.items(), key=lambda x: x[1])
        final = dict(sorted_dict)
        
        for nome, pontuacao in final.items():
            if nome not in lista_nomes_final:
                lista_nomes_final.append(nome)
                lista_pontos_final.append(pontuacao)
            else:
                if pontuacao < lista_pontos_final[lista_nomes_final.index(nome)]:
                    lista_pontos_final[lista_nomes_final.index(nome)] = pontuacao

        # Escreve os nomes e pontuaçOes dos jogadores
        for nome in lista_nomes_final:
            nomes = assets['font_media'].render(
                "{0} ".format(nome), True, BRANCO)
            text_rect = nomes.get_rect()
            text_rect.x = 50
            text_rect.centery = 100 + cont_nome
            screen.blit(nomes, text_rect)

            cont_nome += 60

        cont_pont = 0
        for pontuacao in lista_pontos_final:
            pontuacoes = assets['font_media'].render(
                "{0}".format(pontuacao), True, BRANCO)
            text_rect = pontuacoes.get_rect()
            text_rect.centerx = (LARG / 2) + 100
            text_rect.centery = 100 + cont_pont
            screen.blit(pontuacoes, text_rect)

            cont_pont += 60

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
