import time
from tkinter import Tk, Toplevel, Label, Button

from PIL import Image, ImageTk, ImageSequence
from janelas_interativas.janelas.CriarTela import CriarTela


class Instrucoes:
    def tela_instrucao(self, root):
        outraRoot = Toplevel(root)
        ct = CriarTela()
        ct.criarTelasPos0(outraRoot)

        img = Image.open(r"arquivos\instrucoes.gif")  # abre arquivo gif pela library PIL
        lbl = Label(outraRoot)                        # onde exibirá a imagem
        lbl.place(x=0, y=0)                           # coloca a label na root, serve de base pra gif rodar

        # rodar gif
        self.play_gif(outraRoot,lbl,img, root)

    def play_gif(self, outraRoot, lbl, img, root):
        booleano = True
        while booleano:                                   # rodar gif enquanto janela estiver aberta
            for img in ImageSequence.Iterator(img):
                time.sleep(0.050)  # diminui velocidade do gif
                frame = ImageTk.PhotoImage(img)           # retorna cada frame dentro do gif
                try:    # try apenas para evitar msg de erro
                    lbl.config(image=frame)               # inseri na label o frame atual
                except:
                    outraRoot.destroy()
                    return root                           # importante usar return e não break
                finally:
                    outraRoot.update()

