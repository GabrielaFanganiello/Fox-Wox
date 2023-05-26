import pygame
import os
from config import *


BACKGROUND = 'background'
FOX_B = 'raposa_azul'
FOX_R = 'raposa_vermelha'
FOX_B_E = 'azul_esquerda'
FOX_B_D = 'azul_direita'
FOX_R_E  = 'vermelha_esquerda'
FOX_R_D = 'vermelha_direita'


def load_assets():
    assets = {}

    # Pegando imagem do botão normal
    assets['btn'] = pygame.image.load(os.path.join(BOTAO, 'btn1.png')).convert_alpha()
    
    # Mudando tamanho dos botões
    largura = assets['btn'].get_rect().width * .5
    altura = assets['btn'].get_rect().height * .25
    assets['btn'] = pygame.transform.scale(assets['btn'], (largura, altura))

    # Pegando imagem do botão com mouse em cima
    assets['btn_hover'] = pygame.image.load(os.path.join(BOTAO, 'btn1_hover.png')).convert_alpha()
    assets['btn_hover'] = pygame.transform.scale(assets['btn_hover'], (largura, altura))

    # Carregando Fonte
    assets['font'] = pygame.font.Font(os.path.join(FONTES,'PressStart2P.ttf'), 22)
    assets['font_media'] = pygame.font.Font(os.path.join(FONTES, 'PressStart2P.ttf'), 30)
    assets['font_tempo'] = pygame.font.Font(os.path.join(FONTES, 'PressStart2P.ttf'), 20)

    # Fundo
    assets[BACKGROUND] = pygame.image.load(os.path.join(FUNDO, 'background.png')).convert()
    assets[INSTRUCOES] = pygame.image.load(os.path.join(FUNDO, 'Instrucoes.png')).convert()


    # Carregando imagens da raposa azul
    assets[FOX_B] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_frente', 'tile000.png')).convert_alpha()
    assets[FOX_B] = pygame.transform.scale(assets['raposa_azul'], (100, 100))
    assets[FOX_B_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_B_E] = pygame.transform.scale(assets['azul_esquerda'], (100, 100))
    assets[FOX_B_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_direita', 'tile000.png')).convert_alpha()
    assets[FOX_B_D] = pygame.transform.scale(assets['azul_direita'], (100, 100))

    # Carregando imagens da raposa vermelha
    assets[FOX_R] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_frente', 'tile000.png')).convert_alpha()
    assets[FOX_R] = pygame.transform.scale(assets['raposa_vermelha'], (100, 100))
    assets[FOX_R_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_R_E] = pygame.transform.scale(assets['vermelha_esquerda'], (100, 100))
    assets[FOX_R_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_direita', 'tile000.png')).convert_alpha()
    assets[FOX_R_D] = pygame.transform.scale(assets['vermelha_direita'], (100, 100))

    return assets