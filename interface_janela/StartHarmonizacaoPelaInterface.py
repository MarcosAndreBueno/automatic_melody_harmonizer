from tkinter import Tk, Label, PhotoImage

from harmonia_dois.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from interface_janela.TelaLoading import TelaLoading
from music21 import converter


class StartHarmonizacaoPelaInterface:
    def start_harmonizacao_interface(self, valor, root):
        # obtendo diretório partitura em string
        ip = InserirPartitura()

        # None pois não passaremos o primeiro atributo janela # também poderia ser escrito assim:
        # filePath = ip.inserindo(number = valor)
        # number se refere ao nome da variável na função que está sendo chamada
        # valor se refere ao valor que será passado para essa posição especifica
        filePath = ip.inserindo(None, valor)

        if filePath != " ":
            # parse na partitura
            partitura = converter.parse(filePath)

            # destruir tela menu, construir tela loading.gif
            root.destroy()
            newRoot = Tk()                                 # index = velocidade dos frames
            newRoot.geometry("600x600")
            TelaLoading().play_gif(newRoot, partitura)

            # começando harmonização
            inicio = Start2()
            inicio.startProgram2(partitura, newRoot)