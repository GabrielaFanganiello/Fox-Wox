import pygame
import os
from config import *

BACKGROUND = 'background'
FOX_B = 'raposa_azul'
FOX_R = 'raposa_vermelha'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMAGENS, 'background')).convert()
    assets[FOX_B] = pygame.image.load('assets/sprites/characters/raposa_a_frente/tile000.png').convert_alpha()
    assets[FOX_B] = pygame.transform.scale(assets['raposa_azul'], (100, 100))
    assets[FOX_R] = pygame.image.load('assets/sprites/characters/raposa_v_frente/tile000.png').convert_alpha()
    assets[FOX_R] = pygame.transform.scale(assets['raposa_vermelha'], (100, 100))