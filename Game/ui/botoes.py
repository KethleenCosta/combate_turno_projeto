import pygame
import pygame_gui
from utils.constantes import BOTAO_LARGURA, BOTAO_ALTURA

class Botoes():
    def __init__(self, x, y, imagem, escala):
        largura = imagem.get_width()
        altura = imagem.get_height()
        self.imagem = pygame.transform.scale(imagem, (int(largura * escala)), int(altura * escala))
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.clicado = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:
                self.clicado = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False
        
        surface.blit(self.imagem, (self.rect.x, self.rect.y))

        return action


def criar_botoes(ui_manager):
    botoes = {
        "atacar": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 0, BOTAO_LARGURA, BOTAO_ALTURA),
            text="Atacar",
            manager=ui_manager
        ),
        "defender": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 0, BOTAO_LARGURA, BOTAO_ALTURA),
            text="Defender",
            manager=ui_manager
        ),
        "all_out_atk": pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 0, BOTAO_LARGURA, BOTAO_ALTURA),
            text="All-Out",
            manager=ui_manager
        )
    }
    return botoes

