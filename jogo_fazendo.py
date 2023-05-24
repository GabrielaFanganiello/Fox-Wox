import pygame
from pygame.locals import *
from sys import exit
from random import randint
from config import *
from assets import *
from sprites import *

# Inicializando o PyGame
pygame.init()

# Criando a janela útil do jogo
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Fox & Wox')

# Clock para controlar o FPS
clock = pygame.time.Clock()

# Variáveis de controle dos personagens
fox_r_speed = 4
fox_r_gravity = 0

fox_b_speed = 4
fox_b_gravity = 0

#### IMAGENS DO JOGO ####

# Background
background = pygame.image.load('assets/sprites/background/background.png').convert()

# Sprites da raposa azul
fox_b = pygame.image.load('assets/sprites/characters/raposa_a_frente/tile000.png').convert_alpha()
fox_b = pygame.transform.scale(fox_b, (100, 100))
fox_b_rect = fox_b.get_rect(midbottom = (1400, 800))

# Sprites da raposa vermelha
fox_r = pygame.image.load('assets/sprites/characters/raposa_v_frente/tile000.png').convert_alpha()
fox_r = pygame.transform.scale(fox_r, (100, 100))
fox_r_rect = fox_r.get_rect(midbottom = (200, 800))



# Loop do jogo:
while True:
    # Verifica se o jogador fechou o jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and fox_b_rect.bottom >= 800:
                fox_b_gravity = -12
            if event.key == pygame.K_UP and fox_r_rect.bottom >= 800:
                fox_r_gravity = -12

    # Movimento da raposa azul
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_a]:
        fox_b_rect.x -= fox_b_speed
    if pressed_key[K_d]:
        fox_b_rect.x += fox_b_speed

    # Movimento da raposa vermelha
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_LEFT]:
        fox_r_rect.x -= fox_r_speed
    if pressed_key[K_RIGHT]:
        fox_r_rect.x += fox_r_speed

    # Desenha o background
    screen.blit(background, (0, 0))

    # Desenha a raposa azul
    fox_b_gravity += 0.5
    fox_b_rect.y += fox_b_gravity
    if fox_b_rect.bottom >= 800:
        fox_b_rect.bottom = 800

    screen.blit(fox_b, fox_b_rect)

    # Desenha a raposa vermelha
    fox_r_gravity += 0.5
    fox_r_rect.y += fox_r_gravity
    if fox_r_rect.bottom >= 800:
        fox_r_rect.bottom = 800

    screen.blit(fox_r, fox_r_rect)

    # Atualiza a tela
    pygame.display.update()
    clock.tick(60)