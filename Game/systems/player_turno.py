import pygame
import pygame_gui

class TurnoPlayer:
    def __init__(self, sistema_turno, botoes):
        self.sistema_turno = sistema_turno
        self.botao_atacar = botoes["atacar"]
        self.botao_defender = botoes["defender"]
        self.botao_all_out_atk = botoes["all_out_atk"]

    def processar_evento(self, ator, inimigos, event):
        if event.type != pygame.USEREVENT:
            return
        
        if event.user_type != pygame_gui.UI_BUTTON_PRESSED:
            return

        if event.ui_element == self.botao_atacar:
            alvo = next((i for i in inimigos if i.vivo), None)
            
            if alvo:
                ator.atacar(alvo)
                print(f"HP do inimigo: {alvo.hp}")
                self.sistema_turno.finalizar_turno()

        elif event.ui_element == self.botao_defender:
            ator.defender()
            print(f"HP da {ator.nome}: {ator.hp}")
            self.sistema_turno.finalizar_turno()

        elif event.ui_element == self.botao_all_out_atk:
            ator.all_out_attack(inimigos)
            self.botao_all_out_atk.disable()
            print(f"All-out atk usado por {ator.nome}")
            self.sistema_turno.finalizar_turno()

        # Liberação do botão especial
        if ator.hp <= 20 and not ator.all_out_atk:
            self.botao_all_out_atk.enable()
