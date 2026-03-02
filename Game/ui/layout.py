def posicionar_botoes(
    botoes,
    largura_tela,
    altura_tela,
    botao_largura,
    botao_altura,
    espacamento,
    margem_inferior
):
    ordem = ["atacar", "defender", "all_out_atk"]

    largura_grupo = botao_largura * len(ordem) + espacamento * (len(ordem) - 1)
    inicio_x = (largura_tela - largura_grupo) // 2
    pos_y = altura_tela - botao_altura - margem_inferior

    for i, chave in enumerate(ordem):
        botoes[chave].set_relative_position(
            (inicio_x + i * (botao_largura + espacamento), pos_y)
        )
