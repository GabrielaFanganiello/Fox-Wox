import random
import pygame
from pygame.sprite import Group
from config import *
from assets import *

# Possíveis estados dos jogadores
STILL = 6
JUMPING = 7
FALLING = 8

class Fox(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FOX_R]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARG - 100
        self.rect.bottom = ALT
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        ## Atualização da posição da raposa

        # Tentando saltar / andar no eixo y
        self.speedy += GRAVITY

        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy 

        # Andando no eixo x
        self.rect.x += self.speedx


        # Mantem dentro da tela
        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > ALT:
            self.rect.bottom = ALT
        if self.rect.top < 0:
            self.rect.top = 0
        

class Wox(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FOX_B]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.bottom = ALT
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        ## Atualização da posição da raposa

        # Tentando saltar / andar no eixo y
        self.speedy += GRAVITY

        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy 

        # Andando no eixo x
        self.rect.x += self.speedx


        # Mantem dentro da tela
        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > ALT:
            self.rect.bottom = ALT
        if self.rect.top < 0:
            self.rect.top = 0


class Botao(pygame.sprite.Sprite):
    def __init__(self, assets, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['btn'] # assets é um dicionário de imagens, sons e fonts 
        self.mask = pygame.mask.from_surface(self.image)
        # Todo objeto precisa de um rect
        # Rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # É preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        if over:
            self.image = self.assets['btn_hover']
        else:
            self.image = self.assets['btn']
        if self.rect.bottom > ALT:
            self.rect.bottom = ALT
        if self.rect.top < 0:
            self.rect.top = 0
