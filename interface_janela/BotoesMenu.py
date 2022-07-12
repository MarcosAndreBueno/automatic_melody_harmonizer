from tkinter import PhotoImage, Button, Label

from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.Instrucoes import Instrucoes
from interface_janela.Sobre import Sobre
from interface_janela.Harmonizar import Harmonizar


class BotoesMenu:
    def criar(self,number, root,img):

        # Instruções
        if number == 1:
            listaBotoes = []
            botao = Button(root,
                           image=img,
                           command=lambda: self.ponte(root, img, listaBotoes), # lambda: botão só ativa com click
                           borderwidth=0)  # borda = 0
            listaBotoes.append(botao)      # guarda uma referência do botao
            botao.place(width=130,
                        height=30,
                        x=365,
                        y=210)
        # Inserir partitura
        if number == 2:
            fc = InserirPartitura()
            botao = Button(root,
                           image=img,
                           command=lambda: fc.inserindo(),
                           borderwidth=0)
            botao.place(width=165,
                        height=35,
                        x=345,
                        y=280)
        # Start program
        if number == 3:
            fc = Harmonizar()
            botao = Button(root,
                           image=img,
                           command=lambda: fc.start_harmonizacao(1, root),  # lambda: botão só ativa com click
                           borderwidth=0)  # borda = 0
            botao.place(width=150,
                        height=25,
                        x=355,
                        y=370)
        # Sobre nós
        if number == 4:
            fc = Sobre()
            botao = Button(root,
                            image=img,                      # img Button
                            command=lambda: fc.tela_sobre(root),
                            borderwidth=0)

            botao.place(width=75,
                        height=25,
                        x=391,
                        y=455)

    # =============== BOTAO INSTRUCOES | GIF | IMPEDIR MULTIPLAS JANELAS INSTRUCOES ===============
    # ponte para função instruções
    def ponte(self, root, img, listaBotoes):
        botao = listaBotoes[0].config(state="disable") # botao desabilitado após o click
        listaBotoes.clear()                            # preparar lista para próximo click, limpando-a
        self.recriar(root, img)                        # criar um botão falso para cancelar cor cinza após disabled
        fc = Instrucoes()                              # chamar método com a gif
        fc.tela_instrucao(root, botao)
        self.criar(1, root, img)                       # criar novamente o botão no seu estado original
    # falso botão instrução (impedir multiplas janelas)
    def recriar(self, root, img):
        botao = Label(root,
                       image=img)
        botao.place(width=130,
                    height=30,
                    x=365,
                    y=210)