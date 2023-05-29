import random
import pygame
from pygame.sprite import Group
from config import *
from assets import *

# Possíveis estados dos jogadores
STILL = 6
JUMPING = 7
RUNNING = 8
FALLING = 9

class Fox(pygame.sprite.Sprite):
    def __init__(self, groups, assets, blocks):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.state = STILL

        # Imagens da raposa
        self.image = assets[FOX_R]
        self.rect = self.image.get_rect()

        # Grupo para tratar colisões:
        self.blocks = blocks

        # Posiciona a raposa
        self.rect.centerx = 1100
        self.rect.bottom = ALT

        # Velocidade da raposa
        self.speedx = 0
        self.speedy = 0

        self.groups = groups
        self.assets = assets

    def update(self):
        ## Atualização da posição da raposa

        # Atualiza a velocidade aplicando a aceleração da gravidade

        if self.speedy > 0:
            self.state = FALLING

        self.speedy += GRAVITY
        self.rect.y += self.speedy 

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)

        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Andando no eixo x
        self.rect.x += self.speedx

        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARG:
            self.rect.right = LARG

        elif self.rect.bottom > ALT:
            self.rect.bottom = ALT
        elif self.rect.top < 0:
            self.rect.top = 0

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)

        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 6.3
            self.state = JUMPING

class Wox(pygame.sprite.Sprite):
    def __init__(self, groups, assets, blocks):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.state = STILL

        # Imagens da raposa
        self.image = assets[FOX_B]
        self.rect = self.image.get_rect()

        # Grupo para tratar colisões:
        self.blocks = blocks

        # Posiciona a raposa
        self.rect.centerx = 100
        self.rect.bottom = ALT

        # Velocidade da raposa
        self.speedx = 0
        self.speedy = 0

        self.groups = groups
        self.assets = assets

    def update(self):
        ## Atualização da posição da raposa

        # Atualiza a velocidade aplicando a aceleração da gravidade

        if self.speedy > 0:
            self.state = FALLING

        self.speedy += GRAVITY
        self.rect.y += self.speedy 

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)

        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Andando no eixo x
        self.rect.x += self.speedx

        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > LARG:
            self.rect.right = LARG

        elif self.rect.bottom > ALT:
            self.rect.bottom = ALT
        elif self.rect.top < 0:
            self.rect.top = 0

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)

        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 6.3
            self.state = JUMPING


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

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row
