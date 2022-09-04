from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from harmonizar_viterbi.harmonizar_dados.ObterEnarmonia2 import ObterEnarmonia2
from music21 import note


class TrabalhandoGaps2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()

        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaDuracao = edp.getDuracao()
        self.listaBeatHarmonizar = bho.get_beat_harm()

    def havera_gaps(self):
        global haveraGaps
        haveraGaps = False
        tamanhoLista = len(self.listaBeatHarmonizar)
        for x in range(0,tamanhoLista):
            altura = self.listaAlturas[x]
            nomeNota = ObterEnarmonia2().enarmonia(altura)
            beatHarmonizar = self.listaBeatHarmonizar[x]

            if beatHarmonizar == 1 and nomeNota == "P":
                haveraGaps = True
                break
            elif beatHarmonizar == 1 and nomeNota != "C" and\
                                       nomeNota != "D" and\
                                       nomeNota != "E" and\
                                       nomeNota != "F" and\
                                       nomeNota != "G" and\
                                       nomeNota != "A" and\
                                       nomeNota != "B":
                haveraGaps = True
                break
            elif beatHarmonizar == -1 and nomeNota == "P":
                haveraGaps = True
                break

    # inserir pausas em todos gaps
    def preenchendo_gaps(self):
        ho = HarmoniaObtida2()
        s2 = ho.getStreamHarmonia()
        gap = s2.findGaps()
        if gap is None:
            return s2
        else:
            for x in gap:
                posicao = int(x.offset)
                duracao = self.listaDuracao[posicao]
                # insertAndShift sobrepõe as pausas onde há gaps
                s2.insertAndShift(posicao, note.Rest(quarterLength=duracao))
        return s2

    def get(self):
        return haveraGaps
