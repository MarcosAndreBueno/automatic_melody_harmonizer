from tkinter import Tk, PhotoImage, Label

from interface_janela.BotoesMenu import BotoesMenu
from interface_janela.DimensoesJanela import DimensoesJanela
from interface_janela.TelaAbertura import TelaAbertura
from interface_janela.Titulo import Titulo as t

class Start:
    global root
    def iniciando_janela1(self):
        # ====================dimensões e tela abertura====================
        TelaAbertura().tela_abertura()
        root = Tk() # criar a janela abertura (splash screen)
        t().titulo(root)

        # ====================imagem interface====================
        dp = DimensoesJanela()
        img = PhotoImage(file=r"arquivos\menu.png")
        Label(root, image=img).pack()                               # inserir imagem à janela
        dp.dimensoes(root, 600, 600)                                # chamar função dimensões e posição da janela

        # ====================criando os botões=======================
        bm = BotoesMenu

        # Instruções
        img1 = PhotoImage(file=r"arquivos\botao1.png")

        # Inserir partitura
        img2 = PhotoImage(file=r"arquivos\botao2.png")

        # Start program
        img3 = PhotoImage(file=r"arquivos\botao3.png")

        # Sobre nós
        img4 = PhotoImage(file=r"arquivos\botao4.png")

        botoes = bm(root,img1, img2, img3, img4)
        botoes.criar()

        # ====================Manter janela=======================
        # mantém janela aberta
        root.mainloop()
