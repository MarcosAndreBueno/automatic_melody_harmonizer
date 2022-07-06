from tkinter import Tk, filedialog


class InserirPartitura:
    def inserindo(self, janela1: Tk | None = ..., number: int | None = ...):
        if number != 1:
            global filePath # global permite usar a variável na próxima vez que o método for chamado
            janela1 = Tk()
            janela1.withdraw()
            filePath = filedialog.askopenfilename()

        if number == 1: # poderia ser uma def ao invés de if
            return filePath