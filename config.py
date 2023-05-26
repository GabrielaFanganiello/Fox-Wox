from os import path

# Estabelece a pasta que contem as figuras e sons.
PERSONAGENS = path.join(path.dirname(__file__), 'assets', 'img', 'characters')
SONS = path.join(path.dirname(__file__), 'assets', 'snd')
FONTES = path.join(path.dirname(__file__), 'assets', 'fonte')
FUNDO = path.join(path.dirname(__file__), 'assets', 'img')
BOTAO = path.join(path.dirname(__file__), 'assets', 'img', 'botao')

# Dados gerais do jogo.
LARG = 1200 # Largura da tela
ALT = 600 # Altura da tela
FPS = 60 # Frames por segundo
GRAVITY = 5 # Gravidade
BLOCO = 20 # ALTERAR TAMANHO DO BLOCO CONFORME MAPA
PULO = BLOCO # Altura do pulo do personagem
VELO_X = 8 # Velocidade no eixo x

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