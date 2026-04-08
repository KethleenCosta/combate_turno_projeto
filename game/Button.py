import pygame

class Button():
    def __init__(self, x, y, image, scale):
        self.original_image = image
        self.scale = scale

        width = image.get_width()
        height = image.get_height()

        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicado = False

    def centralizar(self, tela_largura, tela_altura, offset_y=0):
        self.rect.center = (tela_largura // 2, tela_altura // 2 + offset_y)

    def hover(self, zoom=1.1):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            scale = self.scale * zoom
        else:
            scale = self.scale

        width = self.original_image.get_width()
        height = self.original_image.get_height()

    
        center = self.rect.center

        self.image = pygame.transform.scale(
            self.original_image,
            (int(width * scale), int(height * scale))
        )

        self.rect = self.image.get_rect()
        self.rect.center = center  

    def clique(self):
        acao = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicado == False:
                self.clicado = True
                acao = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicado = False
        
        return acao

    def draw(self, tela):
        tela.blit(self.image, (self.rect.x, self.rect.y))

