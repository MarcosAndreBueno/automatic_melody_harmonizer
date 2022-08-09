from tkinter import Button

from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2


class BotoesStart:
    def __init__(self,newRoot):
        self.newRoot = newRoot
        self.corFundo = "#545454"
        self.corClick = "red"
        self.fonte = "Lucida Console bold"
        self.tamanho = 18
        self.corTexto = "white"
        self.borda = 0
        self.coluna1 = 140
        self.coluna2 = 448
        self.largura = 55
        self.altura = 30

    def criar(self):
        newRoot = self.newRoot
        corFundo = self.corFundo
        corClick = self.corClick
        fonte = self.fonte
        tamanho = self.tamanho
        corTexto = self.corTexto
        borda = self.borda
        coluna1 = self.coluna1
        coluna2 = self.coluna2
        largura = self.largura
        altura = self.altura

        button0 = Button(newRoot, text="Dó",
                        font=(fonte,tamanho),fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button0.place(width=largura, height=altura, x= coluna1, y= 270)
        button0.config(command=lambda: self.inserir("C",button0))

        button1 = Button(newRoot, text="Dó#",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button1.place(width=largura, height=altura, x=coluna1, y=320)
        button1.config(command=lambda: self.inserir("C#",button1))

        button2 = Button(newRoot, text="Ré",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button2.place(width=largura, height=altura, x=coluna1, y=372)
        button2.config(command=lambda: self.inserir("D",button2))

        button3 = Button(newRoot, text="Ré#",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button3.place(width=largura, height=altura, x=coluna1, y=423)
        button3.config(command=lambda: self.inserir("D#",button3))

        button4 = Button(newRoot, text="Mi",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button4.place(width=largura, height=altura, x=coluna1, y=473)
        button4.config(command=lambda: self.inserir("E",button4))

        button5 = Button(newRoot, text="Fá",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button5.place(width=largura, height=altura, x=coluna1, y=527)
        button5.config(command=lambda: self.inserir("F",button5))

        button6 = Button(newRoot, text="Fá#",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button6.place(width=largura, height=altura, x=coluna2, y=271)
        button6.config(command=lambda: self.inserir("F#",button6))

        button7 = Button(newRoot, text="Sol",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button7.place(width=largura, height=altura, x=coluna2, y=321)
        button7.config(command=lambda: self.inserir("G",button7))

        button8 = Button(newRoot, text="Sol#",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button8.place(width=largura, height=altura, x=coluna2, y=373)
        button8.config(command=lambda: self.inserir("G#",button8))

        button9 = Button(newRoot, text="Lá",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda,
                        activebackground= corClick)
        button9.place(width=largura, height=altura, x=coluna2, y=423)
        button9.config(command=lambda: self.inserir("A", button9))

        button10 = Button(newRoot, text="Lá#",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button10.place(width=largura, height=altura, x=coluna2, y=474)
        button10.config(command=lambda: self.inserir("A#",button10))

        button11 = Button(newRoot, text="Si",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button11.place(width=largura, height=altura, x=coluna2, y=527)
        button11.config(command=lambda: self.inserir("B", button11))

        button12 = Button(newRoot, text="Ok",
                        font=(fonte, tamanho), fg=corTexto,
                        bg=corFundo, borderwidth=borda)
        button12.place(width=largura, height=altura, x=282, y=184)
        button12.config(command=lambda: self.finalizar(newRoot))

    # anota a tonalidade correspondente ao botão clicado
    def inserir(self, nome,button):
        global tom
        tom = nome
        self.change_selected_button(button)

    def change_selected_button(self,button):
        global selected_button
        corFundo = self.corFundo
        corClick = self.corClick
        if selected_button is not None:
            selected_button.config(bg=corFundo)
        button.config(bg=corClick)
        selected_button = button

    # destrói a janela e devolve a tonalidade inserida ao clicar em ok
    def finalizar(self,newRoot):
        newRoot.destroy()
        tl = Tonalidade2()
        tl.set_tom(tom)

selected_button = None
