from tkinter import Tk, PhotoImage, Label

from interface_janela.janelas.DimensoesJanela import DimensoesJanela
from interface_janela.janelas.Titulo import Titulo as t

class TelaAbertura():
    def tela_abertura(self):
        janela_abertura = Tk()
        t().titulo(janela_abertura)
        janela_abertura.title("HARMONIZAÇÃO AUTOMÁTICA DE MELODIAS FFCLRP_2022")

        img = PhotoImage(file="arquivos\logo.png")
        label_imagem = Label(janela_abertura, image=img).pack()

        dp = DimensoesJanela()
        dp.dimensoes(janela_abertura, 500, 500)

        janela_abertura.after(1000*4, janela_abertura.destroy)  # ms para s = 4 segundos
        janela_abertura.mainloop()
