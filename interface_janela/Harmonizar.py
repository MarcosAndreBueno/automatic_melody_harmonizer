import time
from tkinter import messagebox

from PIL import Image, ImageTk
from interface_janela.BotaoTonalidade import BotaoTonalidade
from teorema_bayes.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.TelaLoading import TelaLoading
from threading import Thread
from music21 import converter
from teorema_bayes.extrair_dados.Tonalidade2 import Tonalidade2


class Harmonizar:
    def harmonizar(self, root):
        # retorna diretório da partitura
        ip = InserirPartitura()
        filePath = ip.get_path()

        if filePath is not None and filePath != "": # usuario já inseriu partitura!
            # inserir tonalidade da melodia que será harmonizada
            tl = BotaoTonalidade()
            tl.inserir(root)
            # resgatar valor tonalidade inserida
            tl = Tonalidade2()
            tom = tl.get_tom()
            # parse na partitura
            partitura = converter.parse(filePath)

            if tom != None:
                self.start_harmonizacao(root, partitura, tom)

        else: # usuario não inseriu partitura!
            messagebox.showerror("Erro", "Por favor, insira a partitura!")

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
