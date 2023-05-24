import random
import pygame
from pygame.sprite import Group
from config import *
from assets import *

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
        self.gravity = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx
        self.rect.y += self.speedy 
        self.rect.y += self.gravity

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
        self.rect.centerx = LARG - 100
        self.rect.bottom = ALT
        self.speedx = 0
        self.speedy = 0
        self.gravity = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição da raposa
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rect.y += self.gravity

        # Mantem dentro da tela
        if self.rect.right > LARG:
            self.rect.right = LARG
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > ALT:
            self.rect.bottom = ALT
            
        if self.rect.top < 0:
                self.rect.top = 0