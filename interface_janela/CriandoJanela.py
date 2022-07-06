# esse método cria uma janela utilizando imagem
from tkinter import Tk, PhotoImage, Label, Frame, Button

from interface_janela.DimensoesJanela import DimensoesJanela
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.Instrucoes import Instrucoes
from interface_janela.SobreNos import SobreNos
from interface_janela.StartHarmonizacaoPelaInterface import StartHarmonizacaoPelaInterface
from interface_janela.TelaAbertura import TelaAbertura


class CriandoJanela:
    global janela1
    def iniciando_janela1(self):
        # ====================dimensões e tela abertura====================
        dp = DimensoesJanela()
        TelaAbertura().tela_abertura()
        janela1 = Tk() # cria a janela

        # ====================imagem interface====================
        img = PhotoImage(file=r"arquivos\interface programa.png")
        label_imagem = Label(janela1, image=img).pack()
        janela1.title("HARMONIZAÇÃO AUTOMÁTICA DE MELODIAS FFCLRP_2022")
        dp.dimensoes(janela1, 600, 600) # chamar função dimensões e posição da janela

        # ============================================================
        # ====================criando os botões=======================
        # ============================================================
        fc1 = SobreNos()
        fc2 = InserirPartitura()
        fc3 = StartHarmonizacaoPelaInterface()
        fc4 = Instrucoes()
        # ====================Instruções====================
        img1 = PhotoImage(file=r"arquivos\botao1.png")
        botao1 = Button(janela1,
                        image=img1,
                        command=lambda: fc4.tela_instrucao(),  # lambda: botão só ativa com click
                        borderwidth=0)  # borda = 0
        botao1.place(width=155,
                     height=30,
                     x=350,
                     y=205)
        # ====================Sobre nós====================
        img4 = PhotoImage(file=r"arquivos\botao4.png")
        botao4 = Button(janela1,
                        image=img4,
                        command=lambda: fc1.tela_sobre_nos(),
                        borderwidth=0)
        botao4.place(width=150,
                     height=30,
                     x=355,
                     y=450)
        # ====================Inserir partitura====================
        img2 = PhotoImage(file=r"arquivos\botao2.png")
        botao2 = Button(janela1,
                        image=img2,
                        command=lambda: fc2.inserindo(janela1),
                        borderwidth=0)
        botao2.place(width=165,
                     height=35,
                     x=345,
                     y=280)
        # ====================Start program====================
        img3 = PhotoImage(file=r"arquivos\botao3.png")
        botao3 = Button(janela1,
                        image=img3,
                        command=lambda: fc3.start_harmonizacao_interface(1),  # lambda: botão só ativa com click
                        borderwidth=0)  # borda = 0
        botao3.place(width=150,
                     height=25,
                     x=355,
                     y=370)

        # mantém janela aberta
        janela1.mainloop()

