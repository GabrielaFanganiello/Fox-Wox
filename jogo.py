import pygame
from pygame.locals import *
from sys import exit
from random import randint
from config import *
from assets import *
from sprites import *

# # Inicializando o PyGame
# pygame.init()

# # Criando a janela útil do jogo
# screen = pygame.display.set_mode((1600, 800))
# pygame.display.set_caption('Fox & Wox')

# # Clock para controlar o FPS
# clock = pygame.time.Clock()

# # Variáveis de controle dos personagens
# fox_r_speed = 4
# fox_r_gravity = 0

# fox_b_speed = 4
# fox_b_gravity = 0

# #### IMAGENS DO JOGO ####

# # Background
# background = pygame.image.load('assets/sprites/background/background.png').convert()

# # Sprites da raposa azul
# fox_b = pygame.image.load('assets/sprites/characters/raposa_a_frente/tile000.png').convert_alpha()
# fox_b = pygame.transform.scale(fox_b, (100, 100))
# fox_b_rect = fox_b.get_rect(midbottom = (1400, 800))

# # Sprites da raposa vermelha
# fox_r = pygame.image.load('assets/sprites/characters/raposa_v_frente/tile000.png').convert_alpha()
# fox_r = pygame.transform.scale(fox_r, (100, 100))
# fox_r_rect = fox_r.get_rect(midbottom = (200, 800))



# # Loop do jogo:
# while True:
#     # Verifica se o jogador fechou o jogo
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w and fox_b_rect.bottom >= 800:
#                 fox_b_gravity = -12
#             if event.key == pygame.K_UP and fox_r_rect.bottom >= 800:
#                 fox_r_gravity = -12

#     # Movimento da raposa azul
#     pressed_key = pygame.key.get_pressed()
#     if pressed_key[K_a]:
#         fox_b_rect.x -= fox_b_speed
#     if pressed_key[K_d]:
#         fox_b_rect.x += fox_b_speed

#     # Movimento da raposa vermelha
#     pressed_key = pygame.key.get_pressed()
#     if pressed_key[K_LEFT]:
#         fox_r_rect.x -= fox_r_speed
#     if pressed_key[K_RIGHT]:
#         fox_r_rect.x += fox_r_speed

#     # Desenha o background
#     screen.blit(background, (0, 0))

#     # Desenha a raposa azul
#     fox_b_gravity += 0.5
#     fox_b_rect.y += fox_b_gravity
#     if fox_b_rect.bottom >= 800:
#         fox_b_rect.bottom = 800

#     screen.blit(fox_b, fox_b_rect)

#     # Desenha a raposa vermelha
#     fox_r_gravity += 0.5
#     fox_r_rect.y += fox_r_gravity
#     if fox_r_rect.bottom >= 800:
#         fox_r_rect.bottom = 800

#     screen.blit(fox_r, fox_r_rect)

#     # Atualiza a tela
#     pygame.display.update()
#     clock.tick(60)


def tela_jogo(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_raposas = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['raposas'] = all_raposas

    # Criando a raposa vermelha
    fox = Fox(groups, assets)
    all_sprites.add(fox)

    # Criando a raposa azul
    wox = Wox(groups, assets)
    all_sprites.add(wox)


    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3

    # # ===== Loop principal =====
    # pygame.mixer.music.play(loops=-1)
    # while state != DONE:
    #     clock.tick(FPS)

    #     # ----- Trata eventos
    #     for event in pygame.event.get():
    #         # ----- Verifica consequências
    #         if event.type == pygame.QUIT:
    #             state = DONE
    #         # Só verifica o teclado se está no estado de jogo
    #         if state == PLAYING:
    #             # Verifica se apertou alguma tecla.
    #             if event.type == pygame.KEYDOWN:
    #                 # Dependendo da tecla, altera a velocidade.
    #                 keys_down[event.key] = True
    #                 if event.key == pygame.K_LEFT:
    #                     player.speedx -= 8
    #                 if event.key == pygame.K_RIGHT:
    #                     player.speedx += 8
    #                 if event.key == pygame.K_SPACE:
    #                     player.shoot()
    #             # Verifica se soltou alguma tecla.
    #             if event.type == pygame.KEYUP:
    #                 # Dependendo da tecla, altera a velocidade.
    #                 if event.key in keys_down and keys_down[event.key]:
    #                     if event.key == pygame.K_LEFT:
    #                         player.speedx += 8
    #                     if event.key == pygame.K_RIGHT:
    #                         player.speedx -= 8

    #     # ----- Atualiza estado do jogo
    #     # Atualizando a posição dos meteoros
    #     all_sprites.update()

    #     if state == PLAYING:
    #         # Verifica se houve colisão entre tiro e meteoro
    #         hits = pygame.sprite.groupcollide(all_meteors, all_bullets, True, True, pygame.sprite.collide_mask)
    #         for meteor in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
    #             # O meteoro e destruido e precisa ser recriado
    #             assets[DESTROY_SOUND].play()
    #             m = Meteor(assets)
    #             all_sprites.add(m)
    #             all_meteors.add(m)

    #             # No lugar do meteoro antigo, adicionar uma explosão.
    #             explosao = Explosion(meteor.rect.center, assets)
    #             all_sprites.add(explosao)

    #             # Ganhou pontos!
    #             score += 100
    #             if score % 1000 == 0:
    #                 lives += 1

    #         # Verifica se houve colisão entre nave e meteoro
    #         hits = pygame.sprite.spritecollide(player, all_meteors, True, pygame.sprite.collide_mask)
    #         if len(hits) > 0:
    #             # Toca o som da colisão
    #             assets[BOOM_SOUND].play()
    #             player.kill()
    #             lives -= 1
    #             explosao = Explosion(player.rect.center, assets)
    #             all_sprites.add(explosao)
    #             state = EXPLODING
    #             keys_down = {}
    #             explosion_tick = pygame.time.get_ticks()
    #             explosion_duration = explosao.frame_ticks * len(explosao.explosion_anim) + 400
    #     elif state == EXPLODING:
    #         now = pygame.time.get_ticks()
    #         if now - explosion_tick > explosion_duration:
    #             if lives == 0:
    #                 state = DONE
    #             else:
    #                 state = PLAYING
    #                 player = Ship(groups, assets)
    #                 all_sprites.add(player)

    #     # ----- Gera saídas
    #     window.fill(BLACK)  # Preenche com a cor branca
    #     window.blit(assets[BACKGROUND], (0, 0))
    #     # Desenhando meteoros
    #     all_sprites.draw(window)

    #     # Desenhando o score
    #     text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop = (WIDTH / 2,  10)
    #     window.blit(text_surface, text_rect)

    #     # Desenhando as vidas
    #     text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
    #     text_rect = text_surface.get_rect()
    #     text_rect.bottomleft = (10, HEIGHT - 10)
    #     window.blit(text_surface, text_rect)

    #     pygame.display.update()  # Mostra o novo frame para o jogador