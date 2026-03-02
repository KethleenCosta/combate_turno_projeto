#C:\Users\Kethleen\Documents\Kethleen\Exercicios\Python\Game> & C:/Users/Kethleen/.virtualenvs/storefront-f3Rv6dD9/Scripts/Activate.ps1
#C:\Users\Kethleen\.virtualenvs\storefront-f3Rv6dD9\Scripts\Activate.ps1

import pygame
import pygame_gui

from utils.constantes import *
from entities.personagem import Personagem
from systems.sistema_turno import SistemaDeTurno
from systems.inimigo_turno import TurnoInimigo
from systems.player_turno import TurnoPlayer
from ui.botoes import criar_botoes
from ui.layout import posicionar_botoes


pygame.init()

tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("RPG Turno")

clock = pygame.time.Clock()
tempo_loading = 3000
timer_fim_jogo = None
rodando = True

ui_manager = pygame_gui.UIManager((TELA_LARGURA, TELA_ALTURA))

# =========================
# ESTADO DO JOGO
# =========================
estado_jogo = MENU


# =========================
# MENU
# =========================
botao_iniciar_img = pygame.image.load("assets/start.png").convert_alpha()
botao_sair_img = pygame.image.load("assets/exit.png").convert_alpha()

botao_iniciar_img = pygame.transform.scale(
    botao_iniciar_img,
    (BOTAO_LARGURA, BOTAO_ALTURA)
)


botao_sair_img = pygame.transform.scale(
    botao_sair_img,
    (BOTAO_LARGURA, BOTAO_ALTURA)
)

rect_iniciar = botao_iniciar_img.get_rect(
    center=(TELA_LARGURA // 2, 350)
)

rect_sair = botao_sair_img.get_rect(
    center=(TELA_LARGURA // 2, 450)
)


# =========================
# PERSONAGENS
# =========================
player = Personagem("Frida", 60, 20, AZUL, "player")
inimigo = Personagem("Inimigo", 100, 30, VERMELHO, "inimigo")
aliado = Personagem("Fran", 60, 20, AMARELO, "aliado")

player.pos_esquerda()
inimigo.pos_meio()
aliado.pos_direita()


# =========================
# SISTEMA DE TURNO
# =========================
sistema_turno = SistemaDeTurno([player, aliado, inimigo])
turno_inimigo = TurnoInimigo(sistema_turno)


# =========================
# BOTÕES DO JOGO
# =========================
botoes = criar_botoes(ui_manager)

posicionar_botoes(
    botoes,
    TELA_LARGURA,
    TELA_ALTURA,
    BOTAO_LARGURA,
    BOTAO_ALTURA,
    ESPACAMENTO,
    MARGEM_INFERIOR
)

botoes["all_out_atk"].disable()

turno_player = TurnoPlayer(sistema_turno, botoes)

# Esconde botões do jogo inicialmente
for botao in botoes.values():
    botao.hide()


# =========================
# LOOP PRINCIPAL
# =========================
while rodando:

    dt = clock.tick(60) / 1000
    timer = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            rodando = False

        ui_manager.process_events(event)

        # ================= MENU =================
        if estado_jogo == MENU:

            if event.type == pygame.MOUSEBUTTONDOWN:

                if rect_iniciar.collidepoint(event.pos):
                    estado_jogo = JOGANDO

                    for botao in botoes.values():
                        botao.show()

                    sistema_turno.estado = sistema_turno.atual().tipo

                elif rect_sair.collidepoint(event.pos):
                    rodando = False

    # ================= JOGO =================
        elif estado_jogo == JOGANDO:

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    ator = sistema_turno.atual()

                    if sistema_turno.estado == ator.tipo:
                        if ator.tipo in ["player", "aliado"]:
                            turno_player.processar_evento(
                                ator,
                                inimigos=[inimigo],
                                event=event
                            )

    # =========================
    # LÓGICA DO JOGO
    # =========================
    if estado_jogo == JOGANDO:

        sistema_turno.update()

        if sistema_turno.jogo_terminou():
            if timer_fim_jogo is None:
                timer_fim_jogo = pygame.time.get_ticks()

            agora = pygame.time.get_ticks()

            if agora - timer_fim_jogo >= tempo_loading:
                estado_jogo = MENU
                timer_fim_jogo = None

            # Reset simples
            player.hp = player.hp_max
            aliado.hp = aliado.hp_max
            inimigo.hp = inimigo.hp_max

            player.vivo = True
            aliado.vivo = True
            inimigo.vivo = True

            sistema_turno.indice = 0
            sistema_turno.estado = None

            for botao in botoes.values():
                botao.hide()

        ator = sistema_turno.atual()

        if (
            sistema_turno.estado == ator.tipo
            and ator.tipo == "inimigo"
            and ator.vivo
        ):
            turno_inimigo.executar(
                inimigo=ator,
                alvos=[player, aliado]
            )
            sistema_turno.finalizar_turno()


    # =========================
    # UPDATE
    # =========================
    ui_manager.update(dt)

    # =========================
    # DRAW
    # =========================
    tela.fill((30, 50, 50))

    if estado_jogo == MENU:
        fonte = pygame.font.SysFont(None, 70)
        texto = fonte.render("RPG de Turno", True, (255, 255, 255))
        tela.blit(texto, (TELA_LARGURA//2 - 150, 150))
        tela.blit(botao_iniciar_img, rect_iniciar)
        tela.blit(botao_sair_img, rect_sair)

    elif estado_jogo == JOGANDO:
        player.draw(tela)
        aliado.draw(tela)
        inimigo.draw(tela)

    ui_manager.draw_ui(tela)
    pygame.display.flip()

pygame.quit()