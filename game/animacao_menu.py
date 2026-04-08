import pygame

class AnimacaoFundo():
    def __init__(self, imagens, velocidade=1000):
        self.frames = imagens
        self.index = 0
        self.tempo_atual = pygame.time.get_ticks()
        self.velocidade = velocidade

    def update(self):
        agora = pygame.time.get_ticks()

        if agora - self.tempo_atual >= self.velocidade:
            self.index += 1
            self.tempo_atual = agora

            if self.index >= len(self.frames):
                self.index = 0

    def draw(self, tela):
        tela.blit(self.frames[self.index], (0, 0))