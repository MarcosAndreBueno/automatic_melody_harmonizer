from tkinter import Tk, filedialog


class InserirPartitura:
    # set chamado pelo botão inserir
    def set_path(self):
        global filePath  # global permite usar a variável na próxima vez que o método for chamado
        filePath = filedialog.askopenfilename() # pop_up para inserir partitura

    # get chamado pelo botão start
    def get_path(self):
        return filePath

filePath = None