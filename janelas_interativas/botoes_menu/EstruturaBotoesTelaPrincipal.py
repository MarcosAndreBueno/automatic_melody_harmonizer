class EstruturaBotoesTelaPrincipal:
    global listaPosicao

    def setPlace(self,botao,pos):
        botao.place(width=self.getWidth(pos),
                     height=self.getHeight(pos),
                     x=self.getX(pos),
                     y=self.getY(pos))

    def getWidth(self,pos):
        width = listaPosicao[pos-1][0]
        return width

    def getHeight(self,pos):
        height = listaPosicao[pos-1][1]
        return height

    def getX(self,pos):
        x = listaPosicao[pos-1][2]
        return x

    def getY(self,pos):
        y = listaPosicao[pos-1][3]
        return y

listaPosicao = [[], [], [], []]  # lista das posições dos botões na tela
listaPosicao[0].extend([130, 30, 365, 210])     # lista botao 1
listaPosicao[1].extend([165, 35, 345, 280])     # lista botao 2
listaPosicao[2].extend([150, 25, 355, 370])     # lista botao 3
listaPosicao[3].extend([75, 25, 391, 455])      # lista botao 4
