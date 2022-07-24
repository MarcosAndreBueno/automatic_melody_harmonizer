from tkinter import Label, Tk, Image
from PIL import Image, ImageTk, ImageSequence
import time
from interface_janela.janelas.DimensoesJanela import DimensoesJanela
from interface_janela.janelas.Titulo import Titulo as t


class TelaLoading:
    # criando função loading na mesma classe da função play_gif para evitar bugs do Tkinter.
    def loading(self):
        dp = DimensoesJanela()
        newRoot = Tk()
        t().titulo(newRoot)
        dp.dimensoes(newRoot, 600, 600)               # chamar função dimensões e posição da janela
        img = Image.open(r"arquivos\loading.gif")     # abre arquivo gif pela library PIL
        lbl = Label(newRoot)                          # adicona uma label na janela
        lbl.place(x=0, y=0)
        self.play_gif(newRoot,lbl,img)

    def play_gif(self,newRoot,lbl,img):
        for img in ImageSequence.Iterator(img):
            time.sleep(0.022)                         # diminui velocidade do gif
            frame = ImageTk.PhotoImage(img)           # retorna cada frame dentro do gif
            lbl.config(image=frame)                   # inseri na label o frame atual
            newRoot.update()

        # mantendo a referência da imagem só para evitar "garbage collection" (funciona sem isso)
        lbl.image = frame

        if number != 1:
            # após o último frame dentro da gif, retorna a função do frame 0
            newRoot.after(0, self.play_gif(newRoot, lbl, img))  # manter gif
            newRoot.mainloop()
        else:
            newRoot.destroy()

    def stop_gif(self):
        global number   # chamado pela classe Start2
        number=1
