import pygame
import os
from config import *


BACKGROUND = 'background'
FOX_B = 'raposa_azul'
FOX_R = 'raposa_vermelha'
FOX_B_E = 'azul_esquerda'
FOX_B_D = 'azul_direita'
FOX_R_E  = 'vermelha_esquerda'
FOX_R_D = 'vermelha_direita'

# TILES
# Chao vermelho
CHAO_V = 'CHAO_V'
CHAO_V_QD = 'CHAO_V_QD'
CHAO_V_QE = 'CHAO_V_QE'
CHAO_GRAMA_D = 'CHAO_GRAMA_D'
CHAO_GRAMA_E = 'CHAO_GRAMA_E'
CHAO_GRAMA = 'CHAO_GRAMA'
CHAO_GRAMA_QD = 'CHAO_GRAMA_QD'
CHAO_GRAMA_QE = 'CHAO_GRAMA_QE'
PEDACIN_V = 'PEDACIN_V'
NEGOCINHO_V = 'NEGOCINHO_V'
TEXTURA_CHAO_V = 'TEXTURA_CHAO_V'
ESQUERDINHA_V = 'ESQUERDINHA_V'
DIREITINHA_V = 'DIREITINHA_V'

# Chao azul
CHAO_A = 'CHAO_A'
CHAO_A_QD = 'CHAO_A_QD'
CHAO_A_QE = 'CHAO_A_QE'
CHAOA_GRAMA_D = 'CHAOA_GRAMA_D'
CHAOA_GRAMA_E = 'CHAOA_GRAMA_E'
CHAOA_GRAMA = 'CHAOA_GRAMA'
CHAOA_GRAMA_QD = 'CHAOA_GRAMA_QD'
CHAOA_GRAMA_QE = 'CHAOA_GRAMA_QE'
PEDACIN_A = 'PEDACIN_A'
NEGOCINHO_A = 'NEGOCINHO_A'
TEXTURA_CHAO_A = 'TEXTURA_CHAO_A'
ESQUERDINHA_A = 'ESQUERDINHA_A'
DIREITINHA_A = 'DIREITINHA_A'

# Fundo
FUNDO_ESCURO = 'FUNDO_ESCURO'
GRAMA_FUNDO = 'GRAMA_FUNDO'
GRAMA_L = 'GRAMA_L'
GRAMA_R = 'GRAMA_R'
GRAMA_T = 'GRAMA_T'
GRAMA_TL = 'GRAMA_TL'
GRAMA_TR = 'GRAMA_TR'
GRAMINHA_1 = 'GRAMINHA_1'
GRAMINHA_2 = 'GRAMINHA_2'
GRAMINHA_CHAO = 'GRAMINHA_CHAO'

# Flores e pedras
FLOR_1 = 'FLOR_1'
FLOR_2 = 'FLOR_2'
FLOR_3 = 'FLOR_3'
FLOR_4 = 'FLOR_4'
PEDRA_1 = 'PEDRA_1'
PEDRA_2 = 'PEDRA_2'
PLACA_C = 'PLACA_C'
PLACA_E = 'PLACA_E'
WATER = 'WATER'
BOLHAS = 'BOLHAS'


def load_assets():
    assets = {}

    # Pegando imagem do botão normal
    assets['btn'] = pygame.image.load(os.path.join(BOTAO, 'btn1.png')).convert_alpha()
    
    # Mudando tamanho dos botões
    largura = assets['btn'].get_rect().width * .5
    altura = assets['btn'].get_rect().height * .25
    assets['btn'] = pygame.transform.scale(assets['btn'], (largura, altura))

    # Pegando imagem do botão com mouse em cima
    assets['btn_hover'] = pygame.image.load(os.path.join(BOTAO, 'btn1_hover.png')).convert_alpha()
    assets['btn_hover'] = pygame.transform.scale(assets['btn_hover'], (largura, altura))

    # Carregando Fonte
    assets['font'] = pygame.font.Font(os.path.join(FONTES,'PressStart2P.ttf'), 22)
    assets['font_media'] = pygame.font.Font(os.path.join(FONTES, 'PressStart2P.ttf'), 30)
    assets['font_tempo'] = pygame.font.Font(os.path.join(FONTES, 'PressStart2P.ttf'), 20)

    # Fundo
    assets[BACKGROUND] = pygame.image.load(os.path.join(FUNDO, 'background.png')).convert()
    assets[INSTRUCOES] = pygame.image.load(os.path.join(FUNDO, 'Instrucoes.png')).convert()


    # Carregando imagens da raposa azul
    assets[FOX_B] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_frente', 'tile000.png')).convert_alpha()
    assets[FOX_B] = pygame.transform.scale(assets['raposa_azul'], (100, 100))
    assets[FOX_B_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_B_E] = pygame.transform.scale(assets['azul_esquerda'], (100, 100))
    assets[FOX_B_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_a_direita', 'tile000.png')).convert_alpha()
    assets[FOX_B_D] = pygame.transform.scale(assets['azul_direita'], (100, 100))

    # Carregando imagens da raposa vermelha
    assets[FOX_R] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_frente', 'tile000.png')).convert_alpha()
    assets[FOX_R] = pygame.transform.scale(assets['raposa_vermelha'], (100, 100))
    assets[FOX_R_E] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_esquerda', 'tile000.png')).convert_alpha()
    assets[FOX_R_E] = pygame.transform.scale(assets['vermelha_esquerda'], (100, 100))
    assets[FOX_R_D] = pygame.image.load(os.path.join(PERSONAGENS, 'raposa_v_direita', 'tile000.png')).convert_alpha()
    assets[FOX_R_D] = pygame.transform.scale(assets['vermelha_direita'], (100, 100))

    # Carregando tiles
    assets[1] = pygame.image.load(path.join(TILES, 'CHAO_V.png')).convert()
    assets[2] = pygame.image.load(path.join(TILES, 'CHAO_A.png')).convert()
    assets[3] = pygame.image.load(path.join(TILES, 'FUNDO_ESCURO.png')).convert()
    assets[4] = pygame.image.load(path.join(TILES, 'WATER.png')).convert()
    assets[5] = pygame.image.load(path.join(TILES, 'BOLHAS.png')).convert()
    assets[6] = pygame.image.load(path.join(TILES, 'GRAMA_FUNDO.png')).convert()
    assets[7] = pygame.image.load(path.join(TILES, 'GRAMA_L.png')).convert()
    assets[8] = pygame.image.load(path.join(TILES, 'GRAMA_R.png')).convert()
    assets[9] = pygame.image.load(path.join(TILES, 'GRAMA_T.png')).convert()
    assets[10] = pygame.image.load(path.join(TILES, 'GRAMA_TL.png')).convert()
    assets[11] = pygame.image.load(path.join(TILES, 'GRAMA_TR.png')).convert()
    # assets[12] = pygame.image.load(path.join(TILES, '')).convert()

    
    return assets