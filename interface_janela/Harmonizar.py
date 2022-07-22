import time
from tkinter import Tk, Label, PhotoImage

from PIL import Image, ImageTk
from interface_janela.BotoesStart import BotoesStart
from interface_janela.Tonalidade import Tonalidade
from teorema_bayes.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.TelaLoading import TelaLoading
from threading import Thread
from music21 import converter


class Harmonizar:
    def harmonizar(self, valor, root):
        # retorna diretório da partitura
        ip = InserirPartitura()
        filePath = ip.inserindo(valor)

        if filePath != "": # usuario já inseriu partitura!
            # inserir tonalidade da melodia que será harmonizada
            tl = Tonalidade()
            tl.inserir(root)
            # resgatar valor tonalidade inserida
            bs = BotoesStart(None)
            tom = bs.finalizar(None)
            # parse na partitura
            partitura = converter.parse(filePath)

            if tom != None:
                self.start_harmonizacao(root, partitura, tom)

        else: # usuario não inseriu partitura!
            pass

    def start_harmonizacao(self, root, partitura, tom):
        # ==================== threads ==========================
        # destruir tela menu
        root.destroy()

        tl = TelaLoading()
        st = Start2()

        # criar tela loading (transitória)
        t1 = Thread(target=tl.loading)
        # precisa vírgula e (): a string partitura vira tupla, assim o kwarg não a quebra em vários args
        t2 = Thread(target=st.startProgram2, args=(partitura,tom))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
