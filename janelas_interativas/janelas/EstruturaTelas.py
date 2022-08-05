# esta classe serve para pegar as dimensões e a posição da interface
# retirado desta aula: https://www.youtube.com/watch?v=rrfNCPMmayI

class EstruturaJanela:
    def __init__(self):
        self.tituloJanela = "HARMONIZAÇÃO AUTOMÁTICA DE MELODIAS FFCLRP_2022"

    def setDimensao(self, root):
        # todos esses selfs vêm da subclasse CriarTela
        largura = self.largura
        altura = self.altura
        posx = self.posx
        posy = self.posy

        # %d indica que um valor será substituído nesta exata região, no caso, as variaveis logo a frente.
        root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

        # impedindo que a janela seja redimencionada manualmente
        root.wm_resizable(width=False, height=False)

    def setTitulo(self,root):
        tituloRoot = self.tituloJanela
        root.title(tituloRoot)
