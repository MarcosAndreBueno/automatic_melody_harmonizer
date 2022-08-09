from tkinter import Tk, Button

from janelas_interativas.InterfaceInterativa import InterfaceInterativa
from janelas_interativas.botoes_menu.botoes_start.TelaTonalidade import TelaTonalidade
from janelas_interativas.janelas.TelaAbertura import TelaAbertura
from janelas_interativas.janelas.TelaLoading import TelaLoading
from janelas_interativas.janelas.TelaPrincipal import TelaPrincipal
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2


def testeInterfaceInterativa():
    InterfaceInterativa().iniciar()

def testeTelaAbertura():
    TelaAbertura().criar()

def testeTelaPrincipal():
    TelaPrincipal().criar()

def testeTelaTonalidade():
    root = Tk()
    root.title("Janela de Teste")
    root.geometry('250x250')
    botao = Button(command=lambda:TelaTonalidade().inserir(root))
    botao.place(width= 50, height=50, x=100, y=100)
    root.mainloop()
    tl = Tonalidade2()
    tom = tl.get_tom()
    print("tom inserido", tom)

def testeTelaLoading():
    TelaLoading().criar()

