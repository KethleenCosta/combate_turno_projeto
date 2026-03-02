import pygame
from utils.constantes import *
from ui.barra_vida import desenhar_barra_hp

class Personagem:
    def __init__(self, nome, hp, atk, cor, tipo):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.atk = atk
        self.cor = cor
        self.tipo = tipo

        self.rect = pygame.Rect(0, 0, PER_LARGURA, PER_ALTURA)
        self.all_out_atk = False
        self.vivo = True
        self.defendendo = False

    # Aplica o dano sofrido ao personagem
    def dano_sofrido(self, dano):
        if not self.vivo:
            return
        
        if self.defendendo:
            dano = dano // 2
            self.defendendo = False
        
        self.hp -= dano

        if self.hp <=0:
            self.hp = 0
            self.morte()

    def atacar(self, alvo):
        if self.vivo and alvo.vivo:
            alvo.dano_sofrido(self.atk)
            print(f'{self.nome} atacou!')

    def defender(self):
        self.defendendo =  True
        print(f'{self.nome} se defendeu!')

    def all_out_attack(self, alvos):
        if self.all_out_atk:
            return 
        
        for alvo in alvos:
            if alvo.vivo:
                alvo.dano_sofrido(self.atk * 2)
        self.all_out_atk = True
        print("It's time for an all out atk!")

    # burn my dread parça
    def morte(self):
        self.vivo = False
        print(f"{self.nome} died and Yuna dances.")


    def pos_esquerda(self):
        self.rect.topleft = (50, CHAO)

    def pos_direita(self):
        self.rect.topright = (TELA_LARGURA - 50, CHAO)

    def pos_meio(self):
        self.rect.midbottom = (TELA_LARGURA // 2, CHAO + PER_ALTURA)

    def draw(self, surface):
        pygame.draw.rect(surface, self.cor, self.rect)

         # barra de vida
        barra_largura = self.rect.width
        barra_altura = 10
        barra_x = self.rect.x
        barra_y = self.rect.y - 15

        desenhar_barra_hp(
            surface,
            barra_x,
            barra_y,
            barra_largura,
            barra_altura,
            self.hp,
            self.hp_max
        )
