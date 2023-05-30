#importando bibliotecas e pastas importantes
import pygame
from random import randint
from config import *
from assets import *
from sprites import *

tempo_total = []

def tela_jogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    #importando os assets criados 
    assets = load_assets()

    #importando os sprites criados 
    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    # Cria um grupo de tiles.
    tipos_blocks = [1, 2, 3, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
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

    # Variáveis criadas para definição de segundos conforme os FPS do jogo
    tempo_ponto = 0

    # ===== Loop principal =====
    # Carrega música de fundo
    pygame.mixer.music.play(loops=-1) 

    while state != DONE and state != PONTUACAO and state != GAMEOVER and state != NOME:
        
        clock.tick(FPS)

        # A cada FPS, conta 1 ponto
        tempo_ponto += 1

        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica se fechou o jogo
            if event.type == pygame.QUIT:
                state = DONE

            # Só verifica ações caso estiver no jogo
            if state == PLAYING:
                # Verifica colisões entre as raposas ou água
                hit_water_f = pygame.sprite.spritecollide(fox, water, False)
                hit_water_w = pygame.sprite.spritecollide(wox, water, False)
                hit = pygame.sprite.collide_rect(fox, wox)
                # Verifica se as raposas se encontraram
                if hit:
                    fox.kill()
                    wox.kill
                    tempo_total.append(tempo_ponto)                     # Guarda o tempo que levou para ganhar

                    # Escreve o tempo no arquivo
                    with open('pontuacao.txt', 'a') as arquivo:
                        arquivo.write('{0} '.format(tempo_ponto))
                    state = NOME

                # Verifica se as raposas colidiram com a água
                elif hit_water_f:                      
                    fox.kill()
                    wox.kill()
                    explosao_r = Explosion_red(fox.rect.center, assets)
                    all_sprites.add(explosao_r)
                    state = DYING
                    explosion_tick = pygame.time.get_ticks()
                    explosion_duration = explosao_r.frame_ticks * len(explosao_r.explosion_red) 

                elif hit_water_w:
                    fox.kill()
                    wox.kill()
                    explosao_b = Explosion_blue(wox.rect.center, assets)
                    all_sprites.add(explosao_b)
                    state = DYING
                    explosion_tick = pygame.time.get_ticks()
                    explosion_duration = explosao_b.frame_ticks * len(explosao_b.explosion_blue) 


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

            elif state == DYING:
                    now = pygame.time.get_ticks()
                    if now - explosion_tick > explosion_duration:
                        state = GAMEOVER 
        
        # ----- Atualiza estado do jogo
        all_sprites.update()

        # ----- Gera saídas
        # Desenhando os tiles, os personagens e o fundo
        screen.fill('#382c54')
        tiles.draw(screen)
        all_sprites.draw(screen)

        # ----- Posicionando a pontuação na tela
        tempo = assets['font_tempo'].render("Pontuação: "+str(tempo_ponto/100), True, BRANCO)
        text_rect = tempo.get_rect()
        text_rect.x = 10
        text_rect.centery = 20
        screen.blit(tempo, text_rect)

        pygame.display.update()

    return state