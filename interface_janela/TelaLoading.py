from tkinter import Label, Tk, Image, Button
from PIL import Image, ImageTk, ImageSequence
import time

from harmonia_dois.Start2 import Start2


class TelaLoading:
    def play_gif(self, newRoot, partitura):
        global img
        img = Image.open(r"arquivos\loading.gif")   # abre arquivo gif pela library PIL
        lbl = Label(newRoot)                        # adicona a uma label
        lbl.place(x=0,y=0)

        for img in ImageSequence.Iterator(img):
            time.sleep(0.022)                         # diminui velocidade do gif
            frame = ImageTk.PhotoImage(img)           # retorna cada frame dentro do gif
            lbl.config(image=frame)                   # torna a imagem o frame atual
            newRoot.update()
        # manter gif acontecendo
        newRoot.after(0,self.play_gif(newRoot, None)) # após o último frame dentro da gif, retorna a função do frame 0

    def stop_gif(self, newRoot):
        newRoot.destroy()

        newRoot.mainloop()
