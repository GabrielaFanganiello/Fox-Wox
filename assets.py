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
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMAGENS, 'background.png')).convert()
    assets[FOX_B] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_frente', 'tile000.png')).convert_alpha()
    assets[FOX_B] = pygame.transform.scale(assets['raposa_azul'], (100, 100))
    assets[FOX_B_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_B_E] = pygame.transform.scale(assets['azul_esquerda'], (100, 100))
    assets[FOX_B_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_direita', 'tile000.png')).convert_alpha()
    assets[FOX_B_D] = pygame.transform.scale(assets['azul_direita'], (100, 100))

    assets[FOX_R] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_frente', 'tile000.png')).convert_alpha()
    assets[FOX_R] = pygame.transform.scale(assets['raposa_vermelha'], (100, 100))
    assets[FOX_R_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_R_E] = pygame.transform.scale(assets['vermelha_esquerda'], (100, 100))
    assets[FOX_R_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_direita', 'tile000.png')).convert_alpha()
    assets[FOX_R_D] = pygame.transform.scale(assets['vermelha_direita'], (100, 100))

    return assets