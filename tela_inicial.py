import pygame

def desenha_texto_no_centro(window, fonte, texto, cor, delta_y=0):
    img_texto = fonte.render(texto, True, cor)
    # Queremos centralizar o texto e sabemos as dimensões da janela e do texto
    texto_x = int(window.get_width() / 2 - img_texto.get_width() / 2)
    texto_y = int(window.get_height() / 2 - img_texto.get_height() / 2)

    window.blit(img_texto, (texto_x, texto_y))

class TelaInicial:
    def __init__(self):
        default_font_name = pygame.font.get_default_font()
        self.font = pygame.font.Font(default_font_name, 24)

        # Poderíamos ter um self.state com um dicionário
        # Mas vamos utilizar somente uma variável
        self.texto_dy = 0
        self.texto_vy = 20  # pixels/segundo

    # Agora a função atualiza devolve uma string com o nome da próxima tela.
    # Se não for mudar de tela, devolve o nome da própria tela.
    def atualiza(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Devolve None para sair
            elif event.type == pygame.KEYDOWN:
                return Tela1()

        self.texto_dy += self.texto_vy * dt
        if abs(self.texto_dy) > 20:
            self.texto_vy *= -1
            # Truque para garantir que nunca vai sair do intervalo [-20, 20]
            sinal = self.texto_dy / abs(self.texto_dy)
            self.texto_dy = sinal * 20

        # Devolve a própria tela para continuar nela
        return self

    def desenha(self, window):
        background = pygame.image.load('assets/sprites/background/background.png').convert()
        background_rect = background.get_rect()
        window.fill((255, 255, 255))
        window.blit(background, background_rect)
        desenha_texto_no_centro(window, self.font, 'FOX WOX', (255, 255, 255), self.texto_dy)
        # Note que não chamamos o pygame.display.update aqui. Deixamos ele para ser chamado fora da função.

# Classe do jogo
class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1600, 800))
        pygame.display.set_caption('Telas com classes')

        self.tela_atual = TelaInicial()
        self.last_updated = pygame.time.get_ticks()

    # Devolve True se é para continuar rodando o jogo, False caso contrário
    def atualiza(self):
        # Atualiza tempo e calcula delta_t
        now = pygame.time.get_ticks()
        delta_t = (now - self.last_updated) / 1000
        self.last_updated = now

        # O método atualiza de todas as telas precisam receber um argumento delta_t
        self.tela_atual = self.tela_atual.atualiza(delta_t)

        # Atualiza tela atual
        if self.tela_atual is None:
            return False
        return True

    def game_loop(self):
        # Note que aqui não precisamos saber qual é a tela_atual
        while self.atualiza():
            self.tela_atual.desenha(self.window)
            pygame.display.update()

    def finaliza(self):
        pygame.quit()


if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()