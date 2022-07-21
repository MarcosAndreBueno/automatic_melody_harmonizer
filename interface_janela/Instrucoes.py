import time
from tkinter import Tk, Toplevel, Label, Button

from PIL import Image, ImageTk, ImageSequence


class Instrucoes:
    def tela_instrucao(self, root):
        outraJanela = Toplevel(root)
        outraJanela.geometry("600x600+0+0")
        img = Image.open(r"arquivos\instrucoes.gif")  # abre arquivo gif pela library PIL
        lbl = Label(outraJanela)                      # adicona uma label na janela
        lbl.place(x=0, y=0)

        # rodar gif
        self.play_gif(outraJanela,lbl,img, root)

    def play_gif(self, outraJanela, lbl, img, root):
        booleano = True
        while booleano:                                   # rodar gif enquanto janela estiver aberta
            for img in ImageSequence.Iterator(img):
                time.sleep(0.050)                         # diminui velocidade do gif
                frame = ImageTk.PhotoImage(img)           # retorna cada frame dentro do gif
                try:    # try apenas para evitar msg de erro
                    lbl.config(image=frame)               # inseri na label o frame atual
                except:
                    outraJanela.destroy()
                    return root                           # importante usar return e não break
                finally:
                    outraJanela.update()
