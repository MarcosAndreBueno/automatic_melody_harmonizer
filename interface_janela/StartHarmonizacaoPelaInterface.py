import time
from tkinter import Tk, Label, PhotoImage

from PIL import Image, ImageTk
from harmonia_dois.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.TelaLoading import TelaLoading
from threading import Thread
from music21 import converter


class StartHarmonizacaoPelaInterface:
    def start_harmonizacao_interface(self, valor, root):
        # obtendo diretório partitura em string
        ip = InserirPartitura()

        # None pois não passaremos o primeiro atributo janela # também poderia ser escrito assim:
        # filePath = ip.inserindo(number = valor)
        # number se refere ao nome da variável na função que está sendo chamada
        # valor se refere ao valor que será passado para essa posição especifica
        filePath = ip.inserindo(valor)

        # parse na partitura
        partitura = converter.parse(filePath)

        # começando harmonização
        #st.startProgram2(partitura)

        # ==================== PRECISA CONTINUAR TELA LOADING ==========================
        if filePath != " ":
            # destruir tela menu
            root.destroy()

            tl = TelaLoading()
            st = Start2()

            # threads
            t1 = Thread(target=tl.loading)
            # precisa vírgula e (): a string partitura vira tupla, assim o kwarg não a quebra em vários args
            t2 = Thread(target=st.startProgram2, args=(partitura,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()