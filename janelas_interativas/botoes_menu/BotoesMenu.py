from tkinter import Button

import janelas_interativas.botoes_menu.botao_instrucoes.CongelarMenu as cm
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from janelas_interativas.botoes_menu.botao_instrucoes.Instrucoes import Instrucoes
from janelas_interativas.botoes_menu.botao_sobre.Sobre import Sobre
from janelas_interativas.botoes_menu.botoes_start.Harmonizar import Harmonizar
from janelas_interativas.botoes_menu.EstruturaBotoesTelaPrincipal import EstruturaBotoesTelaPrincipal
from janelas_interativas.botoes_menu.ImagensBotoesTelaPrincipal import ImagensBotaoTelaPrincipal


class BotoesMenu:
    def __init__(self, root):
        self.root = root


    def criar(self):
        root = self.root
        ibtp = ImagensBotaoTelaPrincipal()
        ebtp = EstruturaBotoesTelaPrincipal()

        # Instruções
        listaBotoes = []
        botao1 = Button(root,
                       image= ibtp.get(1),  # get imagem 1 do botão 1
                       command=lambda: self.ativar_botao1(),
                       borderwidth=0)       # borda = 0
        listaBotoes.append(botao1)          # guarda uma referência do botao
        ebtp.setPlace(botao1,1)

        # Inserir partitura
        fc2 = InserirPartitura()
        botao2 = Button(root,
                       image=ibtp.get(2),   # get imagem 2 do botão 2
                       command=lambda: fc2.set_path(),  # lambda: botão só ativa com click
                       borderwidth=0)
        ebtp.setPlace(botao2,2)

        # Start program
        fc3 = Harmonizar()
        botao3 = Button(root,
                       image=ibtp.get(3),   # get imagem 3 do botão 3
                       command=lambda: fc3.harmonizar(root),  # lambda: botão só ativa com click
                       borderwidth=0)  # borda = 0
        ebtp.setPlace(botao3,3)

        # Sobre nós
        fc4 = Sobre()
        botao4 = Button(root,
                        image=ibtp.get(4),  # get imagem 4 do botão 4
                        command=lambda: fc4.tela_sobre(root),
                        borderwidth=0)
        ebtp.setPlace(botao4,4)

    # =============== BOTAO INSTRUCOES | GIF | IMPEDIR MULTIPLAS JANELAS INSTRUCOES ===============
    # ponte para função instruções
    def ativar_botao1(self):
        root = self.root

        cm.recriar(root)                               # criar botões falsos para congelar tela
        fc = Instrucoes()                              # chamar método com a gif
        fc.tela_instrucao(root)
        self.criar()                                   # criar novamente os botões
