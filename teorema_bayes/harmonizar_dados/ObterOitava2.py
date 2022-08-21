from random import randint

from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class ObterOitava2:
    # oitava definida para harmonizar
    def get_oitava_harm(self):
        aleatorio = randint(1,2)
        if aleatorio == 1:
            oitava = -12
        if aleatorio == 2:
            oitava = -12
        return oitava

    # oitava da melodia atual
    def get_oitava_from_actual_object(self):
        ho = HarmoniaObtida2()
        contador = ho.getContador()
        edp = ExtrairDadosPartitura()
        note = edp.getObjeto(contador)
        oitava = note.octave
        return oitava