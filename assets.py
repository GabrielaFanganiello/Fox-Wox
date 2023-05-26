import pygame
import os
from config import *

BACKGROUND = 'background'
FOX_B = 'raposa_azul'
FOX_R = 'raposa_vermelha'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMAGENS, 'background', 'background.png')).convert()
    assets[FOX_B] = pygame.image.load(os.path.join(IMAGENS, 'characters', 'raposa_a_frente', 'tile000.png')).convert_alpha()
    assets[FOX_B] = pygame.transform.scale(assets['raposa_azul'], (100, 100))
    assets[FOX_R] = pygame.image.load(os.path.join(IMAGENS, 'characters', 'raposa_v_frente', 'tile000.png')).convert_alpha()
    assets[FOX_R] = pygame.transform.scale(assets['raposa_vermelha'], (100, 100))

    #pegando imagem do botão normal
    assets['btn'] = pygame.image.load(os.path.join(IMAGENS, 'botao', 'btn1.png')).convert()
    
    #mudando tamanho das imagens
    largura = assets['btn'].get_rect().width * .5
    altura = assets['btn'].get_rect().height * .25
    assets['btn'] = pygame.transform.scale(assets['btn'], (largura, altura))

    #pegando imagem do botão com mouse em cima
    assets['btn_hover'] = pygame.image.load(os.path.join(IMAGENS, 'botao', 'btn1_hover.png')).convert()
    assets['btn_hover'] = pygame.transform.scale(assets['btn_hover'], (largura, altura))

    #carregando Fonte
    assets['font'] = pygame.font.Font(os.path.join(FONTE,'PressStart2P.ttf'), 22)
    assets['font_media'] = pygame.font.Font(os.path.join(FONTE, 'PressStart2P.ttf'), 30)
    return assets