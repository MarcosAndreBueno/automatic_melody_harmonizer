# =============== BOTAO INSTRUCOES | GIF | IMPEDIR MULTIPLAS JANELAS INSTRUCOES ===============
# ponte para função instruções
from tkinter import Label


# falso botão instrução (impedir multiplas janelas)
def recriar(root, img1,img2,img3,img4):
    # instruções
    botao = Label(root,
                  image=img1)
    botao.place(width=130,
                height=30,
                x=365,
                y=210)

    # inserir partitura
    botao = Label(root,
                  image=img2)
    botao.place(width=165,
                height=35,
                x=345,
                y=280)

    # Start program
    botao = Label(root,
                  image=img3)
    botao.place(width=150,
                height=25,
                x=355,
                y=370)

    # Sobre nós
    botao = Label(root,
                  image=img4)
    botao.place(width=75,
                height=25,
                x=391,
                y=455)
