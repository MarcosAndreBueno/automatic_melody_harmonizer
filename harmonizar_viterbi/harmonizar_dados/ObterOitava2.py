from random import randint

from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.PitchNumber2 import PitchNumber2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class ObterOitava2:
    def __init__(self):
        self.edp = ExtrairDadosPartitura()
        self.pn = PitchNumber2()

    # oitava definida para harmonizar
    def get_oitava_harm(self, fundamental, contador):
        oitava = -12
        # note = self.edp.getObjeto(contador)
        # alturaAtual = self.pn.get_pitch_from_object(note)
        # fundamental += oitava
        # print(alturaAtual - fundamental, alturaAtual, fundamental)
        # # se a harmonização for gerar cruzamento de vozes, descer mais uma oitava
        # if alturaAtual - fundamental < 10:
        #     fundamental += oitava
        #     print("nova fundamental",fundamental)
        return oitava

    # oitava da melodia atual
    def get_oitava_from_actual_object(self, contador):
        note = self.edp.getObjeto(contador)
        oitava = note.octave
        return oitava