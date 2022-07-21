from tkinter import PhotoImage, Button, Label

import interface_janela.CongelarMenu as cm
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.Instrucoes import Instrucoes
from interface_janela.Sobre import Sobre
from interface_janela.Harmonizar import Harmonizar


class BotoesMenu:
    def __init__(self, root, img1,img2,img3,img4):
        self.root = root
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4

    def criar(self):
        root = self.root
        img1 = self.img1
        img2 = self.img2
        img3 = self.img3
        img4 = self.img4

        # Instruções
        listaBotoes = []
        botao1 = Button(root,
                       image=img1,
                       command=lambda: self.ativar_botao1(listaBotoes),
                       borderwidth=0)   # borda = 0
        listaBotoes.append(botao1)      # guarda uma referência do botao
        botao1.place(width=130,
                    height=30,
                    x=365,
                    y=210)

        # Inserir partitura
        fc2 = InserirPartitura()
        botao2 = Button(root,
                       image=img2,
                       command=lambda: fc2.inserindo(),  # lambda: botão só ativa com click
                       borderwidth=0)
        botao2.place(width=165,
                    height=35,
                    x=345,
                    y=280)

        # Start program
        fc3 = Harmonizar()
        botao3 = Button(root,
                       image=img3,
                       command=lambda: fc3.start_harmonizacao(1, root),  # lambda: botão só ativa com click
                       borderwidth=0)  # borda = 0
        botao3.place(width=150,
                    height=25,
                    x=355,
                    y=370)

        # Sobre nós
        fc4 = Sobre()
        botao4 = Button(root,
                        image=img4,    # img Button
                        command=lambda: fc4.tela_sobre(root),
                        borderwidth=0)
        botao4.place(width=75,
                    height=25,
                    x=391,
                    y=455)

    # =============== BOTAO INSTRUCOES | GIF | IMPEDIR MULTIPLAS JANELAS INSTRUCOES ===============
    # ponte para função instruções
    def ativar_botao1(self, listaBotoes):
        root = self.root
        img1 = self.img1
        img2 = self.img2
        img3 = self.img3
        img4 = self.img4

        cm.recriar(root,img1,img2,img3,img4)           # criar botões falsos para congelar tela
        fc = Instrucoes()                              # chamar método com a gif
        fc.tela_instrucao(root)
        self.criar()                                   # criar novamente o botão no seu estado original
