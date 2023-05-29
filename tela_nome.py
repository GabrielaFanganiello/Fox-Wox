import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *
from tela_pontuacao import *

jogadores = []

def tela_nome(screen):
    nome = ''

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    botoes_nome = pygame.sprite.Group()

    # Definindo se o botao foi ativado
    ativado = False

    # Criando primeira fileira com 1 botões
    for i in range(1):
        botao_nome = Botao(assets, "INSIRA OS NOMES")

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
                state = DONE
                done = True

            # Verifica se foi apertado o botão 
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Se o botao foi ativado, apaga o botao de inserir o nome 
                if botao_nome.rect.collidepoint(event.pos):
                    ativado = True
                    botao_nome.kill()

                else: 
                    ativado = False

            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão se o mouse passa por cima
                for btn in botoes_nome:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)

            if event.type == pygame.KEYDOWN:
                # Verifica o que está sendo digitado
                if ativado:
                    if event.key == pygame.K_RETURN:
                        # Se apertar o return armazena o nome do jogador e vai para prox tela
                        jogadores.append(nome)
                        with open('pontuacao.txt', 'a') as arquivo:
                            arquivo.write('{0} '.format(nome))
                        state = VENCEDOR
                        done = True
                        nome = ''

                    elif event.key == pygame.K_BACKSPACE:
                        # Garante que se houver erro de digitacao, pode apagar
                        nome = nome[:-1]

                    else:
                        # Escrevendo o nome com o teclado do computador 
                        nome += event.unicode
        jogadores.append(nome)

        screen.blit(assets[BACKGROUND], (0,0))

        # Escrevendo texto dos botões
        for btn in botoes_nome:
            btn_texto = assets['font'].render(f"{btn.nome_do_jogo}", True, BRANCO)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)

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