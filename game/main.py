import pygame
from utensils import TELA_LARGURA,TELA_ALTURA
from Button import Button
from animacao_menu import AnimacaoFundo

# ------ Setup
pygame.init()
relogio = pygame.time.Clock()

# ------ Tela
tela  = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Good Kids")

# ------ Variaveis
# Botoes menu
comecar_btn_igm = pygame.image.load('assets/comecar_btn.png').convert_alpha()
sair_btn_img = pygame.image.load('assets/sair_btn.png').convert_alpha()

#Animcao menu
frames = []
for i in range(3):
    img = pygame.image.load(f'assets/menu/{i}.jpg').convert()
    frames.append(img)

fundo = AnimacaoFundo(frames)

# ------ Buttons
comecar_btn = Button(100, 200, comecar_btn_igm, 0.8)
sair_btn = Button(100, 200, sair_btn_img, 0.8)
#centralizar
comecar_btn.centralizar(TELA_LARGURA, TELA_ALTURA, - 100)
sair_btn.centralizar(TELA_LARGURA, TELA_ALTURA, 100)

rodando = True

while rodando:
    relogio.tick(60)

    fundo.update()
    fundo.draw(tela)

    comecar_btn.draw(tela)
    sair_btn.draw(tela)

    comecar_btn.hover()
    sair_btn.hover()

    acao_comecar = comecar_btn.clique()
    acao_sair = sair_btn.clique()

    if acao_comecar:
        print('Começar')

    if acao_sair:
        print('Sair')
        rodando = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # tela.fill((255,255,255))

    pygame.display.update()
pygame.quit()