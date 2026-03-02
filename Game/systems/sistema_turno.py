from utils.constantes import VITORIA, DEROTA, ESPERA
import pygame

class SistemaDeTurno:
    def __init__(self, personagens, delay_ms = 2000):
        self.personagens = personagens
        self.indice = 0
        self.estado = self.personagens[self.indice].tipo
        self.delay_ms = delay_ms
        self.timer_fim_turno = 0

    def atual(self):
        return self.personagens[self.indice]

    def proximo_turno(self):
        for _ in range(len(self.personagens)):
            self.indice = (self.indice + 1) % len(self.personagens)
            if self.personagens[self.indice].vivo:
                print("Proximo turno")
                break

    def atualizar_estado(self):

        vivos = [p for p in self.personagens if p.vivo]

        inimigos_vivos = [p for p in vivos if p.tipo == "inimigo"]
        aliados_vivos = [p for p in vivos if p.tipo != "inimigo"]

        if not inimigos_vivos:
            self.estado = VITORIA
            print(self.estado)
        elif not aliados_vivos:
            self.estado = DEROTA
            print(self.estado)

    def update(self):
        if self.estado == ESPERA:
            agora = pygame.time.get_ticks()
            if agora - self.timer_fim_turno >= self.delay_ms:
                self.proximo_turno()
                self.estado = self.atual().tipo

    def finalizar_turno(self):
        self.atualizar_estado()

        if self.estado in [VITORIA, DEROTA]:
            return
            
        self.timer_fim_turno = pygame.time.get_ticks()
        self.estado = ESPERA


    def jogo_terminou(self):
        # Se estado do jogo vitoria:
            # Jogo pausa
            # msg de vitoria
            # CHama MEnu com retry an quit 
        
        # Se estado do jogo vitoria:
            # Jogo pausa
            # msg de derrota
            # MEnu com retry an quit

    # sera q eu tera q fazer uma funçao desse menu com pygame gui,
    # q recena o 
        return self.estado in [VITORIA, DEROTA]

