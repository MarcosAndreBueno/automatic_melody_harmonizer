# esta classe serve para pegar as dimensões e a posição da interface
# retirado desta aula: https://www.youtube.com/watch?v=rrfNCPMmayI

class DimensoesJanela:
    def dimensoes(self, janela1, largura, altura):
        # dimensões da janela

        # resolução do nosso sistema
        largura_screen = janela1.winfo_screenwidth()
        altura_screen = janela1.winfo_screenheight()

        # posição da janela
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2-15 - altura/2

        print(posx, posy)
        # definindo a dimensão da janela
        # largura x altura + posição horizontal + posição vertical (lugar da tela que a tabela aparecerá)
        # %d indica que um valor será substituído nesta exata região, no caso os valores logo a frente.
        janela1.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

        # impedindo que a janela seja redimencionada manualmente
        janela1.wm_resizable(width=False, height=False)