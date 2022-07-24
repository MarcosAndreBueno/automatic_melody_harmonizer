from tkinter import Tk, filedialog


class InserirPartitura:
    def set_path(self):
        global filePath # global permite usar a variável na próxima vez que o método for chamado
        filePath = filedialog.askopenfilename() # pop_up para inserir partitura

        # if chamado pelo StartHarmonizacaoPelaInterface
    def get_path(self):
            return filePath

filePath = None