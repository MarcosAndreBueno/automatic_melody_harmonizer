from tkinter import Tk, PhotoImage, Label
from janelas_interativas.botoes_menu.BotoesMenu import BotoesMenu
from janelas_interativas.janelas.CriarTela import CriarTela
from janelas_interativas.botoes_menu.ImagensBotoesTelaPrincipal import ImagensBotaoTelaPrincipal


class TelaPrincipal:
    def criar(self):

        root = Tk()
        ct = CriarTela()
        ct.dimensaoGrande()
        ct.criarTelaCentralizada(root)


        # ====================imagem interface====================
        img = PhotoImage(file=r"arquivos\menu.png")
        Label(root, image=img).pack()                               # inserir imagem à janela

        # ====================criando os botões=======================
        bm = BotoesMenu
        ibtp = ImagensBotaoTelaPrincipal()

        # Instruções - guardar imagem
        img1 = PhotoImage(file=r"arquivos\botao1.png")
        ibtp.set(img1)

        # Inserir partitura - guardar imagem
        img2 = PhotoImage(file=r"arquivos\botao2.png")
        ibtp.set(img2)

        # Start program - guardar imagem
        img3 = PhotoImage(file=r"arquivos\botao3.png")
        ibtp.set(img3)

        # Sobre nós - guardar imagem
        img4 = PhotoImage(file=r"arquivos\botao4.png")
        ibtp.set(img4)

        botoes = bm(root)
        botoes.criar()

        # ====================Manter janela=======================
        # mantém janela aberta
        root.mainloop()
