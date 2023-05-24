import random
import pygame
from pygame.sprite import _Group
from config import *
from assets import *

class Fox(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FOX_R]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARG - 200
        self.rect.bottom = ALT
        self.speedx = 4
        self.gravity = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0

class Wox(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FOX_B]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = LARG - 200
        self.rect.bottom = ALT
        self.speedx = 4
        self.gravity = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0