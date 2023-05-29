from os import path

# Estabelece a pasta que contem as figuras e sons.
PERSONAGENS = path.join(path.dirname(__file__), 'assets', 'img', 'characters')
SONS = path.join(path.dirname(__file__), 'assets', 'snd')
FONTES = path.join(path.dirname(__file__), 'assets', 'fonte')
FUNDO = path.join(path.dirname(__file__), 'assets', 'img')
BOTAO = path.join(path.dirname(__file__), 'assets', 'img', 'botao')

TILES = path.join(path.dirname(__file__), 'assets', 'img', 'tiles')

# Dados gerais do jogo.
LARG = 1215                 # Largura da tela
ALT = 600                   # Altura da tela
FPS = 120                   # Frames por segundo
GRAVITY = 0.2               # Gravidade
VELO_X = 3.0                # Velocidade no eixo x
TILE_SIZE = 32              # Tamanho do tile (cada tile é um quadrado de 32x32 pixels)


# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define os tipos de tiles
CHAO_V = 1
CHAO_A = 2
FUNDO_ESCURO = 3
WATER = 4
BOLHAS = 5
GRAMA_FUNDO = 6
GRAMA_L = 7
GRAMA_R = 8
GRAMA_T = 9
GRAMA_TL = 10
GRAMA_TR = 11
CHAO_A_QD = 12
CHAO_A_QE = 13
CHAO_V_QD = 14
CHAO_V_QE = 15
DIREITINHA_A = 16
DIREITINHA_V = 17
ESQUERDINHA_A = 18
ESQUERDINHA_V = 19
CHAOA_GRAMA_QD = 20
CHAOA_GRAMA_QE = 21
CHAOA_GRAMA = 22
CHAOA_GRAMA_D = 23
CHAOA_GRAMA_E = 24
CHAO_GRAMA_QD = 25
CHAO_GRAMA_QE = 26
CHAO_GRAMA = 27
CHAO_GRAMA_D = 28
CHAO_GRAMA_E = 29
GRAMINHA_1 = 30
GRAMINHA_2 = 31
GRAMINHA_CHAO = 32
FLOR_1 = 33
FLOR_2 = 34
FLOR_3 = 35
FLOR_4 = 36
PEDRA_1 = 37
PEDRA_2 = 38

# Define o mapa com os tipos de tiles
MAP = [
    [10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11],
    [7, 6, 31, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 30, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 31, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 31, 33, 6, 34, 38, 6, 6, 6, 6, 6, 36, 6, 6, 32, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 21, 22, 22, 22, 23, 2, 2, 24, 28, 1, 29, 27, 27, 28, 29, 25, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 31, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 30, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 13, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 14, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 30, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 31, 6, 6, 6, 6, 6, 6, 6, 1, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 30, 6, 6, 6, 6, 6, 30, 6, 6, 6, 6, 6, 6, 6, 32, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 21, 22, 20, 6, 30, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 26, 27, 25, 6, 6, 6, 6, 6, 8],
    [7, 35, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 13, 12, 6, 32, 37, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 38, 6, 15, 14, 8],
    [2, 2, 2, 2, 2, 2, 12, 6, 6, 6, 6, 6, 6, 6, 31, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 1, 1, 1, 1, 1, 1],
    [7, 6, 6, 6, 6, 31, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 31, 6, 6, 30, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 30, 6, 6, 6, 6, 6, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 32, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 32, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 21, 20, 6, 6, 6, 6, 6, 6, 30, 6, 6, 6, 15, 14, 6, 6, 6, 33, 6, 6, 6, 6, 6, 37, 6, 8],
    [24, 22, 22, 20, 4, 4, 4, 21, 22, 23, 2, 2, 2, 2, 12, 4, 4, 4, 4, 4, 4, 4, 4, 15, 1, 1, 1, 1, 29, 27, 25, 4, 4, 4, 26, 28, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 16, 3, 3, 5, 3, 3, 3, 5, 3, 19, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

# Estados para controle do fluxo da aplicação
INIT = 0
PLAYING = 1
GAME = 2
INSTRUCOES = 3
GAMEOVER = 4
PONTUACAO = 5
DONE = 6
NOME = 7
VENCEDOR = 8