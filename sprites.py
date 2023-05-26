import random
import pygame
from pygame.sprite import Group
from config import *
from assets import *

# Possíveis estados dos jogadores
STILL = 2
JUMPING = 3
FALLING = 4

class Fox(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.state = STILL
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
        # Atualização da posição da raposa

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

    def jump(self):
        if self.state == STILL:
            self.speedy -= PULO
            self.state = JUMPING
        

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
        # Atualização da posição da raposa

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

    def jump(self):
        if self.state == STILL:
            self.speedy -= PULO
            self.state = JUMPING