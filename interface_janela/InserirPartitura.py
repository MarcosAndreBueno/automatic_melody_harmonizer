from tkinter import Tk, filedialog


class InserirPartitura:
    def inserindo(self, number: int | None = ...):
        if number != 1:
            global filePath # global permite usar a variável na próxima vez que o método for chamado
            filePath = filedialog.askopenfilename() # pop_up para inserir partitura

        # if chamado pelo StartHarmonizacaoPelaInterface
        if number == 1: # poderia ser uma def ao invés de if
            return filePath