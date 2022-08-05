from janelas_interativas.janelas.TelaAbertura import TelaAbertura
from janelas_interativas.janelas.TelaPrincipal import TelaPrincipal

class InterfaceInterativa:
    global root
    def iniciar(self):

        # ========================tela de abertura=========================
        ta = TelaAbertura()
        ta.criar()

        # =======================janela principal==========================
        tp = TelaPrincipal()
        tp.criar()

