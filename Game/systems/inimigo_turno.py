import random

class TurnoInimigo:
    def __init__(self, sistema_turno):
        self.sistema_turno = sistema_turno

    def executar(self, inimigo, alvos):
        if not inimigo.vivo:
            return

        alvos_vivos = [a for a in alvos if a.vivo]
        if not alvos_vivos:
            return

        acao = random.choice(["atacar", "defender", "all_out_atk"])
        alvo = random.choice(alvos_vivos)

        if acao == "atacar":
            inimigo.atacar(alvo)
            print(f"HP da {alvo.nome}: {alvo.hp}")

        elif acao == "defender":
            inimigo.defender()
            print(f"{inimigo.nome} está defendendo")

        elif acao == "all_out_atk":
            if inimigo.hp <= 30 and not inimigo.all_out_atk:
                inimigo.all_out_attack(alvos_vivos)
            else:
                inimigo.atacar(alvo)

        self.sistema_turno.finalizar_turno()
