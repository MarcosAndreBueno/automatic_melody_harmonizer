from tkinter import Toplevel, PhotoImage, Label

from janelas_interativas.botoes_menu.botoes_start.BotoesStart import BotoesStart
from janelas_interativas.janelas.CriarTela import CriarTela


class TelaTonalidade:
    def inserir(self,root):
        # tentar criar subjanela, só deixar para fazer pack aqui
        newRoot = Toplevel()
        ct = CriarTela()
        ct.dimensaoGrande()
        ct.criarTelaCentralizada(newRoot)

        img = PhotoImage(file="arquivos/botao4.1.png")
        lbl = Label(newRoot, image=img)
        lbl.pack()

        # criar botões da aba inserir tonalidade e retornar tonalidade
        bs = BotoesStart(newRoot)
        imgBotao4 = PhotoImage(file="arquivos/botao4.2.png")
        # necessário salvar referência da imagem
        bs.setImg(imgBotao4)
        bs.criar()

        # impedir outras janelas enquanto esta não for fechada
        newRoot.transient(root)
        newRoot.grab_set()
        root.wait_window(newRoot)

        # Destrói a janela, caso ela tenha sido fechada por outro meio que não o botão "Ok"
        newRoot.destroy()