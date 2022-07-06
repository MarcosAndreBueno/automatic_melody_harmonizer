from tkinter import Tk, Toplevel, PhotoImage, Label

from PIL import ImageTk, Image


class SobreNos:
    def tela_sobre_nos(self):
        outraJanela = Tk()
        img = PhotoImage(file=r"arquivos\Logo programa.png")
        label_imagem = Label(outraJanela, image=img).pack()