from tkinter import PhotoImage, Button

from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.Instrucoes import Instrucoes
from interface_janela.SobreNos import SobreNos
from interface_janela.StartHarmonizacaoPelaInterface import StartHarmonizacaoPelaInterface


class BotoesMenu:
    def criar(self,number, root,fc,img):
        # Instruções
        if number == 1:
            botao = Button(root,
                            image=img,
                            command=lambda: fc.tela_instrucao(),  # lambda: botão só ativa com click
                            borderwidth=0)  # borda = 0

            botao.place(width=155,
                        height=30,
                        x=350,
                        y=205)

        if number == 2:
            botao = Button(root,
                           image=img,
                           command=lambda: fc.inserindo(root),
                           borderwidth=0)
            botao.place(width=165,
                        height=35,
                        x=345,
                        y=280)

        if number == 3:
            botao = Button(root,
                           image=img,
                           command=lambda: fc.start_harmonizacao_interface(1),  # lambda: botão só ativa com click
                           borderwidth=0)  # borda = 0
            botao.place(width=150,
                        height=25,
                        x=355,
                        y=370)

        # Sobre nós
        if number == 4:
            botao = Button(root,
                            image=img,
                            command=lambda: fc.tela_sobre_nos(),
                            borderwidth=0)

            botao.place(width=150,
                        height=30,
                        x=355,
                        y=450)

        return botao
