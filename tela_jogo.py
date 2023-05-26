#importando bibliotecas e pastas importantes
import pygame
from random import randint
from config import *
from assets import *
from sprites import *


def tela_jogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #importando os assets criados 
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    # Criando a raposa vermelha
    fox = Fox(groups, assets)
    all_sprites.add(fox)

    # Criando a raposa azul
    wox = Wox(groups, assets)
    all_sprites.add(wox)

    # Definindo possíveis estados dos jogadores
    DONE = 0
    PLAYING = 1
    DYING = 2

    state = PLAYING

    keys_down = {}
    score = 0

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica se fechou o jogo
            if event.type == pygame.QUIT:
                state = DONE

            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:

                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:

                    keys_down[event.key] = True

                    # Verifica qual tecla foi apertada, comandos raposa azul.
                    if event.key == pygame.K_w:
                        wox.speedy = -15
                    if event.key == pygame.K_a:
                        wox.speedx -= VELO_X
                    if event.key == pygame.K_d:
                        wox.speedx += VELO_X

                    # Verifica qual tecla foi apertada, comandos raposa vermelha.
                    elif event.key == pygame.K_UP:
                        fox.speedy = -15
                    if event.key == pygame.K_LEFT:
                        fox.speedx -= VELO_X
                    if event.key == pygame.K_RIGHT:
                        fox.speedx += VELO_X
                    

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:

                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:

                        if event.key == pygame.K_LEFT:
                            fox.speedx += VELO_X
                        if event.key == pygame.K_RIGHT:
                            fox.speedx -= VELO_X
                             
                        if event.key == pygame.K_a:
                            wox.speedx += VELO_X
                        if event.key == pygame.K_d:
                            wox.speedx -= VELO_X


        # ----- Atualiza estado do jogo
        all_sprites.update()

        # ----- Gera saídas
        screen.fill(PRETO)  # Preenche com a cor preto
        screen.blit(assets[BACKGROUND], (0, 0))

        # Desenhando os personagens
        all_sprites.draw(screen)

        pygame.display.update()


