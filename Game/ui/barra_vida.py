import pygame

def desenhar_barra_hp(surface, x, y, largura, altura, hp, hp_max):
    pygame.draw.rect(surface, (120, 0, 0), (x, y, largura, altura))

    # porcentagem de vida
    proporcao = hp /  hp_max if hp_max > 0 else 0

    # barra atual
    pygame.draw.rect(
        surface,
        (0, 200, 0),
        (x, y, int(largura * proporcao), altura)
    )

    # borda
    pygame.draw.rect(surface, (255, 255, 255), (x, y, largura, altura), 2)