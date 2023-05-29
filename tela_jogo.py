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

    # Cria um grupo de tiles.
    tipos_blocks = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19]
    tiles = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    water = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            tile = Tile(assets[tile_type], row, column)
            tiles.add(tile)
            if tile_type in tipos_blocks:
                blocks.add(tile)
            elif tile_type == 4:
                water.add(tile)

    # Criando a raposa vermelha
    fox = Fox(groups, assets, blocks)
    all_sprites.add(fox)

    # Criando a raposa azul
    wox = Wox(groups, assets, blocks)
    all_sprites.add(wox)

    state = PLAYING
    keys_down = {}
    tempo_segundos = 0
    timer = 0
    tempo_total = 0

    # ===== Loop principal =====
    while state != DONE and state != PONTUACAO and state != GAMEOVER and state != NOME:
        
        clock.tick(FPS)

        if timer < 60:
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
                hit_water_f = pygame.sprite.spritecollide(fox, water, False)
                hit_water_w = pygame.sprite.spritecollide(wox, water, False)
                hit = pygame.sprite.collide_rect(fox, wox)
                if hit or hit_water_f or hit_water_w:
                    fox.kill()
                    wox.kill()
                    tempo_total = tempo_segundos
                    state = NOME

                # Verifica se apertou alguma tecla.
                elif event.type == pygame.KEYDOWN:

                    keys_down[event.key] = True


                    # Verifica qual tecla foi apertada, comandos raposa vermelha.
                    if event.key == pygame.K_UP:
                        fox.jump()
                    if event.key == pygame.K_LEFT:
                        fox.speedx -= VELO_X
                    if event.key == pygame.K_RIGHT:
                        fox.speedx += VELO_X
                    
                    # Verifica qual tecla foi apertada, comandos raposa azul.
                    if event.key == pygame.K_w:
                        wox.jump()
                    if event.key == pygame.K_a:
                        wox.speedx -= VELO_X
                    if event.key == pygame.K_d:
                        wox.speedx += VELO_X

                # Verifica se soltou alguma tecla.
                elif event.type == pygame.KEYUP:

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

        # Desenhando os tiles e os personagens
        screen.fill('#382c54')
        tiles.draw(screen)
        all_sprites.draw(screen)


        # ----- Posicionando o tempo na tela
        tempo = assets['font_tempo'].render("Tempo: "+str(tempo_segundos / 100), True, BRANCO)
        text_rect = tempo.get_rect()
        text_rect.x = 10
        text_rect.centery = 20
        screen.blit(tempo, text_rect)

        pygame.display.update()

    return state
        