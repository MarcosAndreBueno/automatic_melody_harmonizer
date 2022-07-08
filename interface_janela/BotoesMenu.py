from tkinter import PhotoImage, Button

from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.Instrucoes import Instrucoes
from interface_janela.Sobre import Sobre
from interface_janela.StartHarmonizacaoPelaInterface import StartHarmonizacaoPelaInterface


class BotoesMenu:

    def criar(self,number, root,img):

        # Instruções
        if number == 1:
            fc = Instrucoes()
            botao = Button(root,
                            image=img,
                            command=lambda: fc.tela_instrucao(),  # lambda: botão só ativa com click
                            borderwidth=0)  # borda = 0

            botao.place(width=155,
                        height=30,
                        x=350,
                        y=205)
        # Inserir partitura
        if number == 2:
            fc = InserirPartitura()
            botao = Button(root,
                           image=img,
                           command=lambda: fc.inserindo(root),
                           borderwidth=0)
            botao.place(width=165,
                        height=35,
                        x=345,
                        y=280)
        # Start program
        if number == 3:
            fc = StartHarmonizacaoPelaInterface()
            botao = Button(root,
                           image=img,
                           command=lambda: fc.start_harmonizacao_interface(1, root),  # lambda: botão só ativa com click
                           borderwidth=0)  # borda = 0
            botao.place(width=150,
                        height=25,
                        x=355,
                        y=370)
        # Sobre nós
        if number == 4:
            fc = Sobre()
            imgTela = PhotoImage(file=r"arquivos\sobre.png") # img Tela
            botao = Button(root,
                            image=img,                      # img Button
                            command=lambda: fc.tela_sobre(imgTela, root),
                            borderwidth=0)

            botao.place(width=120,
                        height=30,
                        x=355,
                        y=450)
