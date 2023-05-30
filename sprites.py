import random
import pygame
from pygame.sprite import Group
from config import *
from assets import *

# Cria a classe da Raposa Vermelha
class Fox(pygame.sprite.Sprite):
    def __init__(self, groups, assets, blocks):
        # Construtor da classe mãe.
        pygame.sprite.Sprite.__init__(self)

        # Define o estado inicial como parado
        self.state = STILL

        # Imagens da raposa
        self.image = assets[FOX_R]
        self.rect = self.image.get_rect()

        # Grupo para tratar colisões:
        self.blocks = blocks

        # Posiciona a raposa
        self.rect.centerx = 1150
        self.rect.bottom = ALT

        # Define a velocidade inicial da raposa
        self.speedx = 0
        self.speedy = 0

        self.groups = groups
        self.assets = assets


    # Função que atualiza a posição da raposa

    def update(self):
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        self.rect.y += self.speedy


        # --- Líogica de colisões ---
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


    # Função que faz a raposa pular
    def jump(self):
        # Só pode pular se não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 6.3
            self.state = JUMPING


# Cria a classe da Raposa Azul
class Wox(pygame.sprite.Sprite):
    def __init__(self, groups, assets, blocks):
        # Construtor da classe mãe.
        pygame.sprite.Sprite.__init__(self)

        # Define o estado inicial como parado
        self.state = STILL

        # Imagens da raposa
        self.image = assets[FOX_B]
        self.rect = self.image.get_rect()

        # Grupo para tratar colisões:
        self.blocks = blocks

        # Posiciona a raposa
        self.rect.centerx = 65
        self.rect.bottom = ALT

        # Define a velocidade inicial da raposa
        self.speedx = 0
        self.speedy = 0

        self.groups = groups
        self.assets = assets


    # Função que atualiza a posição da raposa

    def update(self):
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        self.rect.y += self.speedy


        # --- Líogica de colisões ---
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


    # Função que faz a raposa pular
    def jump(self):
        # Só pode pular se não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= 6.3
            self.state = JUMPING


# Cria a classe dos botões
class Botao(pygame.sprite.Sprite):
    def __init__(self, assets, nome_do_jogo):
        # Construtor da classe mãe.
        pygame.sprite.Sprite.__init__(self)

        # Assets é um dicionário de imagens, sons e fontes.
        self.assets = assets

        # Imagem do botão
        self.image = assets['btn']
        self.mask = pygame.mask.from_surface(self.image)

        # Todo objeto precisa de um rect (a representação de retangulo feita pelo pygame)
        self.rect = self.image.get_rect()

        # É preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    # Função que atualiza a imagem do botão caso o mouse esteja em cima dele
    def mouse_over(self, over):
        # Se o mouse estiver em cima do botão, a imagem muda
        if over:
            self.image = self.assets['btn_hover']
        else:
            self.image = self.assets['btn']
        
        # Atualiza o rect
        if self.rect.bottom > ALT:
            self.rect.bottom = ALT
        if self.rect.top < 0:
            self.rect.top = 0


# Cria a classe dos blocos e tiles
class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile
        self.image = tile_img

        # Define o rect do tile
        self.rect = self.image.get_rect()

        # Posiciona o tile com base na linha e coluna passada no "MAP"
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Classe que representa a morte da raposa vermelha
class Explosion_red(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação
        self.explosion_red = assets[MORTE_VERMELHA]

        # Inicia com a primeira imagem
        self.frame = 1                                   # Índice da animação
        self.image = self.explosion_red[self.frame]      # Define a imagem do frame atual
        self.rect = self.image.get_rect()                # Define o retângulo da imagem
        self.rect.center = center                        # Posiciona o centro do retângulo

        # momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 50

    # Atualiza a animação da explosão
    def update(self):
        # Verifica o tick atual
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:
            # Tick da nova imagem e avança um quadro
            self.last_update = now
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_red):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_red[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Classe que representa a morte da raposa azul
class Explosion_blue(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação
        self.explosion_blue = assets[MORTE_AZUL]

        # Inicia com a primeira imagem
        self.frame = 1                                   # Índice da animação
        self.image = self.explosion_blue[self.frame]     # Define a imagem do frame atual
        self.rect = self.image.get_rect()                # Define o retângulo da imagem
        self.rect.center = center                        # Posiciona o centro do retângulo

        # Momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 50

    # Atualiza a animação da explosão
    def update(self):
        # Verifica o tick atual
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem
        if elapsed_ticks > self.frame_ticks:
            # Tick da nova imagem e avança um quadro
            self.last_update = now
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_blue):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_blue[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


