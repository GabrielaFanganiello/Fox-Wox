from os import path

# Estabelece a pasta que contem as figuras e sons.
IMAGENS = path.join(path.dirname(__file__), 'assets', 'img')
PERSONAGENS = path.join(path.dirname(__file__), 'assets', 'img', 'characters')
SONS = path.join(path.dirname(__file__), 'assets', 'snd')
FONTES = path.join(path.dirname(__file__), 'assets', 'font')

# Dados gerais do jogo.
LARG = 1600 # Largura da tela
ALT = 800 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
