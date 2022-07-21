import time
from tkinter import Tk, Label, PhotoImage

from PIL import Image, ImageTk
from teorema_bayes.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.TelaLoading import TelaLoading
from threading import Thread
from music21 import converter


class Harmonizar:
    def start_harmonizacao(self, valor, root):
        # obtendo diretório partitura em string
        ip = InserirPartitura()

        # retorna diretório da partitura
        filePath = ip.inserindo(valor)

        # parse na partitura
        partitura = converter.parse(filePath)

        # ==================== threads ==========================
        if filePath != " ":
            # destruir tela menu
            root.destroy()

            tl = TelaLoading()
            st = Start2()

            # criar tela loading (transitória)
            t1 = Thread(target=tl.loading)
            # precisa vírgula e (): a string partitura vira tupla, assim o kwarg não a quebra em vários args
            t2 = Thread(target=st.startProgram2, args=(partitura,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()