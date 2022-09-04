from music21 import note
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2


class UltimoAcorde2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()

        self.listaNome = edp.getNome()
        self.listaBeatHarmonizar = bho.get_beat_harm()

    # encontra a última nota a ser harmonizada
    def posicao_ultimo_acorde(self):
        tamanhoL = len(self.listaNome)
        for x in self.listaNome[::-1]:
            tamanhoL -= 1
            nomeNota = self.listaNome[tamanhoL]
            beatHarmonizar = self.listaBeatHarmonizar[tamanhoL]
            if nomeNota != "P" and beatHarmonizar == 1:
                ultimoAcorde = tamanhoL
                return ultimoAcorde
        return -1   # caso não haja nota alguma, apenas pausas

    # completa com Dó maior a última nota
    def obter_ultimo_acorde(self, altura, oitava):
        n1 = note.Note(altura)
        nomeNota = n1.pitch.name
        if nomeNota == "C" or "E" or "G":   # se nota da tríade da tônica, acorde = tônica
            altura = altura+oitava
        else:                               # se não, sortear um acorde
            oh = ObterHarmonias2()
            oh.set_harmonias(nomeNota, altura, oitava)
        return altura