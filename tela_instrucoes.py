import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *

def tela_inicial(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()
    