from tkinter import Toplevel, PhotoImage, Label

from interface_janela.botoes_menu.botoes_start.BotoesStart import BotoesStart


class TelaTonalidade:
    def inserir(self,root):
        # tentar criar subjanela, só deixar para fazer pack aqui
        outraJanela = Toplevel()
        print("=-"*20,outraJanela,"=-"*20)
        print("=-"*20,"tipo",type(outraJanela),"=-"*20)
        outraJanela.geometry("600x600+0+0")
        img = PhotoImage(file="arquivos/botao4.2 tonalidade.png")
        lbl = Label(outraJanela, image=img)
        lbl.pack()

        # criar botões da aba inserir tonalidade e retornar tonalidade
        bs = BotoesStart(outraJanela)
        bs.criar()
        # impedir outras janelas enquanto esta não for fechada
        outraJanela.transient(root)
        outraJanela.grab_set()
        root.wait_window(outraJanela)

        # Destrói a janela, caso ela tenha sido fechada por outro meio que não o botão "Ok"
        outraJanela.destroy()
        outraJanela.update()
