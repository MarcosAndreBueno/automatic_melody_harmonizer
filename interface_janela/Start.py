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
        bm = BotoesMenu()
        # Instruções
        img1 = PhotoImage(file=r"arquivos\botao1.png")
        botao1 = bm.criar(1,root,img1)

        # Inserir partitura
        img2 = PhotoImage(file=r"arquivos\botao2.png")
        botao2 = bm.criar(2,root,img2)

        # Start program
        img3 = PhotoImage(file=r"arquivos\botao3.png")
        botao3 = bm.criar(3,root,img3)

        # Sobre nós
        img4 = PhotoImage(file=r"arquivos\botao4.png")
        botao4 = bm.criar(4, root, img4)

        # ====================Manter janela=======================
        # mantém janela aberta
        root.mainloop()
