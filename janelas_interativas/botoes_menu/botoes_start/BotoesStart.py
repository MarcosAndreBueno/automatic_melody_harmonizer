from tkinter import Button, PhotoImage, Label, messagebox

from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2


class BotoesStart:
    def __init__(self, newRoot):
        self.newRoot = newRoot
        self.corFundo = "#292828"
        self.corClick = "red"
        self.fonte = "Lucida Console bold"
        self.tamanho = 15
        self.corTexto = "white"
        self.borda = 0
        self.nome = ""
        self.acidente = ""
        self.modo = ""
        self.lbl = ''
        self.lbl2 = ''
        self.lbl3 = ''

    def criar(self):
        newRoot = self.newRoot
        corFundo = self.corFundo
        corClick = self.corClick
        fonte = self.fonte
        tamanho = self.tamanho
        corTexto = self.corTexto
        borda = self.borda

        # notas
        largura = 47
        altura = 19
        button0 = Button(newRoot, text="Dó",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button0.place(width=largura, height=altura, x=104, y=261)
        button0.config(command=lambda: self.setNome("C"))

        button2 = Button(newRoot, text="Ré",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button2.place(width=largura, height=altura, x=188, y=261)
        button2.config(command=lambda: self.setNome("D"))

        button4 = Button(newRoot, text="Mi",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button4.place(width=largura, height=altura, x=273, y=261)
        button4.config(command=lambda: self.setNome("E"))

        button5 = Button(newRoot, text="Fá",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button5.place(width=largura, height=altura, x=59, y=307)
        button5.config(command=lambda: self.setNome("F"))

        button7 = Button(newRoot, text="Sol",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button7.place(width=largura, height=altura, x=148, y=307)
        button7.config(command=lambda: self.setNome("G"))

        button9 = Button(newRoot, text="Lá",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button9.place(width=largura, height=altura, x=235, y=307)
        button9.config(command=lambda: self.setNome("A"))

        button11 = Button(newRoot, text="Si",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button11.place(width=largura, height=altura, x=315, y=307)
        button11.config(command=lambda: self.setNome("B"))

        # acidentes
        largura = 80
        altura = 30
        button12 = Button(newRoot, text="♯",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button12.place(width=largura, height=altura, x=63, y=410)
        button12.config(command=lambda: self.setAcidente("#"))

        button13 = Button(newRoot, text="♭",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button13.place(width=largura, height=altura, x=63, y=453)
        button13.config(command=lambda: self.setAcidente("-"))

        button14 = Button(newRoot, text="♮",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button14.place(width=largura, height=altura, x=63, y=496)
        button14.config(command=lambda: self.setAcidente(""))

        largura = 86
        altura = 31
        # modos
        button15 = Button(newRoot, text="Maior",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button15.place(width=largura, height=altura, x=271, y=411)
        button15.config(command=lambda: self.setAcidente("M"))

        button16 = Button(newRoot, text="Menor",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button16.place(width=largura, height=altura, x=271, y=473)
        button16.config(command=lambda: self.error())

        # seguir
        button12 = Button(newRoot, image=imgBotao4,  # imagem instanciada fora na classe TelaTonalidade
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button12.place(width=83, height=71, x=477, y=344)
        button12.config(command=lambda: self.finalizar(newRoot))

        # label informações inseridas
        self.lbl = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo)
        self.lbl.place(width=152, height=77, x=435, y=210)

        self.lbl2 = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo)
        self.lbl2.place(width=152, height=77, x=437, y=210)

        self.lbl3 = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo)
        self.lbl3.place(width=152, height=77, x=439, y=210)

    # anota a tonalidade correspondente ao botão clicado
    def setNome(self, nome):
        self.nome = nome
        self.lbl.config(text=nome)

    def setAcidente(self, nome):
        self.acidente = nome
        self.lbl2.config(text=nome)

    def setModo(self, nome):
        self.modo = nome
        self.lbl3.config(text=nome)

    def error(self):
        messagebox.showerror('Desculpa, função indisponível!          ')

    # destrói a janela e devolve a tonalidade inserida ao clicar em ok
    def finalizar(self, newRoot):
        newRoot.destroy()
        tl = Tonalidade2()
        tom = self.nome + self.acidente
        tl.set_tom(tom)  # por enquanto, modo sempre maior

    def setImg(self, img):
        global imgBotao4
        imgBotao4 = img


selected_button = None
from tkinter import Button, PhotoImage, Label, messagebox

from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2


class BotoesStart:
    def __init__(self, newRoot):
        self.newRoot = newRoot
        self.corFundo = "#292828"
        self.corClick = "red"
        self.fonte = "Lucida Console bold"
        self.tamanho = 15
        self.corTexto = "white"
        self.borda = 0
        self.nome = ""
        self.acidente = ""
        self.modo = ""
        self.lbl = ''
        self.lbl2 = ''
        self.lbl3 = ''

    def criar(self):
        newRoot = self.newRoot
        corFundo = self.corFundo
        corClick = self.corClick
        fonte = self.fonte
        tamanho = self.tamanho
        corTexto = self.corTexto
        borda = self.borda

        # notas
        largura = 47
        altura = 19
        button0 = Button(newRoot, text="Dó",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button0.place(width=largura, height=altura, x=104, y=261)
        button0.config(command=lambda: self.setNome("C"))

        button2 = Button(newRoot, text="Ré",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button2.place(width=largura, height=altura, x=188, y=261)
        button2.config(command=lambda: self.setNome("D"))

        button4 = Button(newRoot, text="Mi",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button4.place(width=largura, height=altura, x=273, y=261)
        button4.config(command=lambda: self.setNome("E"))

        button5 = Button(newRoot, text="Fá",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button5.place(width=largura, height=altura, x=59, y=307)
        button5.config(command=lambda: self.setNome("F"))

        button7 = Button(newRoot, text="Sol",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button7.place(width=largura, height=altura, x=148, y=307)
        button7.config(command=lambda: self.setNome("G"))

        button9 = Button(newRoot, text="Lá",
                         font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo, borderwidth=borda)
        button9.place(width=largura, height=altura, x=235, y=307)
        button9.config(command=lambda: self.setNome("A"))

        button11 = Button(newRoot, text="Si",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button11.place(width=largura, height=altura, x=315, y=307)
        button11.config(command=lambda: self.setNome("B"))

        # acidentes
        largura = 80
        altura = 30
        button12 = Button(newRoot, text="♯",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button12.place(width=largura, height=altura, x=63, y=410)
        button12.config(command=lambda: self.setAcidente("♯"))

        button13 = Button(newRoot, text="♭",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button13.place(width=largura, height=altura, x=63, y=453)
        button13.config(command=lambda: self.setAcidente("♭"))

        button14 = Button(newRoot, text="♮",
                          font=(20, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button14.place(width=largura, height=altura, x=63, y=496)
        button14.config(command=lambda: self.setAcidente("♮"))

        largura = 86
        altura = 31
        # modos
        button15 = Button(newRoot, text="Maior",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button15.place(width=largura, height=altura, x=271, y=411)
        button15.config(command=lambda: self.setModo("M"))

        button16 = Button(newRoot, text="Menor",
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button16.place(width=largura, height=altura, x=271, y=473)
        button16.config(command=lambda: self.error())

        # seguir
        button17 = Button(newRoot, image=imgBotao4,  # imagem instanciada fora na classe TelaTonalidade
                          font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo, borderwidth=borda)
        button17.place(width=83, height=71, x=477, y=344)
        button17.config(command=lambda: self.finalizar(newRoot))

        largura = 20
        altura = 20
        # label informações inseridas
        self.lbl = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                         bg=corFundo)
        self.lbl.place(width=largura, height=altura, x=435, y=210)

        self.lbl2 = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo)
        self.lbl2.place(width=largura, height=altura, x=455, y=210)

        self.lbl3 = Label(newRoot, font=(fonte, tamanho), fg=corTexto,
                          bg=corFundo)
        self.lbl3.place(width=largura, height=altura, x=475, y=210)

    # anota a tonalidade correspondente ao botão clicado
    def setNome(self, nome):
        self.nome = nome
        self.lbl.config(text=nome)

    def setAcidente(self, nome):
        self.lbl2.config(text=nome)
        if self.nome[-1] == '♯':
            tom = self.acidente = '#'
        elif self.nome[-1] == '♭':
            tom = self.acidente = 'b'
        else: # ♮
            tom = self.acidente = ""


    def setModo(self, nome):
        self.modo = nome
        self.lbl3.config(text=nome)

    def error(self):
        messagebox.showerror('Desculpa, função indisponível!          ')

    # destrói a janela e devolve a tonalidade inserida ao clicar em ok
    def finalizar(self, newRoot):
        newRoot.destroy()
        tl = Tonalidade2()
        tom = self.nome + self.acidente
        tl.set_tom(tom)  # por enquanto, modo sempre maior

    def setImg(self, img):
        global imgBotao4
        imgBotao4 = img


selected_button = None
