from janelas_interativas.janelas.EstruturaTelas import EstruturaJanela


class CriarTela(EstruturaJanela):
    # todas variaveis que guardam self.AlgumaCoisa são utilizadas na super classe EstruturaJanela.py
    global largura, altura

    def dimensaoGrande(self):
        self.largura = 600
        self.altura = 600
    def dimensaoMedia(self):
        self.largura = 500
        self.altura = 500

    def criarTelaCentralizada(self,root): # telas no centro da screen do computador
        largura = self.largura
        altura = self.altura

        # retorna largura e altura da resolução do pc
        largura_screen = root.winfo_screenwidth()
        altura_screen = root.winfo_screenheight()

        # torna a posição do Tkinter o centro da resolução do pc
        posx = self.posx = largura_screen/2 - largura/2
        posy = self.posy = altura_screen/2-15 - altura/2

        self.setDimensao(root)
        self.setTitulo(root)

    def criarTelasPos0(self, root):        # telas no canto superior esquerdo da screen do computador
        largura = self.largura = 600
        altura = self.altura = 600

        # torna a posição do Tkinter o canto superior esquerdo do pc
        posx = self.posx = 0
        posy = self.posy = 0

        # criar a janela
        self.setDimensao(root)
        self.setTitulo(root)