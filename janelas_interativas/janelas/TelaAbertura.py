from tkinter import Tk, PhotoImage, Label
from janelas_interativas.janelas.CriarTela import CriarTela


class TelaAbertura():
    def criar(self):
        opening_root = Tk()
        ct = CriarTela()
        ct.dimensaoMedia()
        ct.criarTelaCentralizada(opening_root)

        # imagem da janela
        img = PhotoImage(file="arquivos\logo.png")
        label_imagem = Label(opening_root, image=img).pack()

        # estrutura da janela: executar superclass EstruturaJanela
        super().__init__()

        # tempo que a janela mostrará
        opening_root.after(1000*4, opening_root.destroy)  # ms para s = 4 segundos
        opening_root.mainloop()
