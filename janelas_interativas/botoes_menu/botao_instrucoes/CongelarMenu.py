# =============== BOTAO INSTRUCOES | GIF | IMPEDIR MULTIPLAS JANELAS INSTRUCOES ===============
# ponte para função instruções
from tkinter import Label


# falso botão instrução (impedir multiplas janelas)
from janelas_interativas.botoes_menu.EstruturaBotoesTelaPrincipal import EstruturaBotoesTelaPrincipal
from janelas_interativas.botoes_menu.ImagensBotoesTelaPrincipal import ImagensBotaoTelaPrincipal


def recriar(root):
    ibtp = ImagensBotaoTelaPrincipal()
    ebtp = EstruturaBotoesTelaPrincipal()

    # instruções
    botao1 = Label(root,
                  image=ibtp.get(1))
    ebtp.setPlace(botao1, 1)

    # inserir partitura
    botao2 = Label(root,
                  image=ibtp.get(2))
    ebtp.setPlace(botao2, 2)

    # Start program
    botao3 = Label(root,
                  image=ibtp.get(3))
    ebtp.setPlace(botao3, 3)

    # Sobre nós
    botao4 = Label(root,
                  image=ibtp.get(4))
    ebtp.setPlace(botao4, 4)
