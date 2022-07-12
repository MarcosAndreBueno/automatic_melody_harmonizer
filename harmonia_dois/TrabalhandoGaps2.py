from harmonia_dois.ObterEnarmonia2 import ObterEnarmonia2
from music21 import note


class TrabalhandoGaps2:
    def havera_gaps(self, listaBeatHarmonizar, listaNome, listaAlturas):
        haveraGaps = False
        tamanhoLista = len(listaNome)
        for x in range(0,tamanhoLista):
            nomeNota = ObterEnarmonia2().enarmonia(listaAlturas, x)
            beatHarmonizar = listaBeatHarmonizar[x]
            if beatHarmonizar == 2 and nomeNota == "P":
                return True
            if beatHarmonizar == 1 and nomeNota != "C" and\
                                       nomeNota != "D" and\
                                       nomeNota != "E" and\
                                       nomeNota != "F" and\
                                       nomeNota != "G" and\
                                       nomeNota != "A" and\
                                       nomeNota != "B":
                return True
            if beatHarmonizar == -1 and nomeNota == "P":
                return True
        return haveraGaps

    def encontrando_gaps(self, s2):
        gap = s2.findGaps()
        return gap

    def preenchendo_gaps(self, s2, listaDuracao):
        gap = self.encontrando_gaps(s2)
        if gap is None:
            return s2
        else:
            for x in gap:
                posicao = int(x.offset)
                duracao = listaDuracao[posicao]
                # insertAndShift sobrepõe as pausas onde há gaps
                s2.insertAndShift(posicao, note.Rest(quarterLength=duracao))
        return s2
