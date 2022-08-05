import time
from janelas_interativas.janelas.TelaLoading import TelaLoading

class DestruirLoading:
    def destruir(self,start):
        stop = time.time()                    # stop cronometragem processamento
        tempoTotal = stop - start             # tempoTotal de processamento
        if tempoTotal >= 5:
            tl = TelaLoading()
            tl.stop_gif()
        else:
            esperar = 5-tempoTotal
            time.sleep(esperar)
            tl = TelaLoading()
            tl.stop_gif()