from tkinter import Tk, Toplevel, PhotoImage, Label

from PIL import ImageTk, Image


class Sobre:
    def tela_sobre(self, img, root):

        # criar janela
        outraJanela = Toplevel()
        Label(outraJanela, image=img).pack()

        # impedir outras janelas enquanto esta não for fechada
        outraJanela.transient(root)
        outraJanela.grab_set()
        root.wait_window(outraJanela)