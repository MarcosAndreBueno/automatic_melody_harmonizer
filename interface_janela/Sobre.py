from tkinter import Tk, Toplevel, PhotoImage, Label
from PIL import ImageTk, Image


class Sobre:
    def tela_sobre(self, root):
        outraJanela = Toplevel()
        outraJanela.geometry("600x600+0+0")
        img = PhotoImage(file=r"arquivos/sobre.png")
        lbl = Label(outraJanela, image=img)
        lbl.pack()

        # impedir outras janelas enquanto esta não for fechada
        outraJanela.transient(root)
        outraJanela.grab_set()
        root.wait_window(outraJanela)