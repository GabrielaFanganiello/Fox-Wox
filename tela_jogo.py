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

    # Cria um grupo de tiles.
    tiles = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            tile = Tile(assets[tile_type], row, column)
            tiles.add(tile)

    state = PLAYING
    keys_down = {}
    tempo_segundos = 0
    timer = 0

    # ===== Loop principal =====
    while state != DONE:
        
        clock.tick(FPS)

        if timer<60:
            timer += 1

        else:
            tempo_segundos += 1
            timer = 60

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
                    if event.key == pygame.K_w and wox.rect.bottom == ALT:
                        wox.speedy = -15
                    if event.key == pygame.K_a:
                        wox.speedx -= VELO_X
                    if event.key == pygame.K_d:
                        wox.speedx += VELO_X

                    # Verifica qual tecla foi apertada, comandos raposa vermelha.
                    elif event.key == pygame.K_UP and fox.rect.bottom == ALT:
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

        # Verifica se houve colisão entre personagens
        if state == PLAYING:

            hit = pygame.sprite.collide_rect(fox, wox)
            if hit:
                fox.kill()
                wox.kill()
                state = GAMEOVER


        # ----- Gera saídas
        screen.blit(assets[BACKGROUND], (0, 0))

        # Desenhando os personagens
        tiles.draw(screen)
        all_sprites.draw(screen)


        # ----- Posicionando o tempo na tela
        tempo = assets['font_tempo'].render("Tempo: "+str(tempo_segundos / 100), True, BRANCO)
        text_rect = tempo.get_rect()
        text_rect.x = 10
        text_rect.centery = 20
        screen.blit(tempo, text_rect)

        pygame.display.update()

        