from hmm_viterbi.Viterbi import Viterbi
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.extrair_dados.Tonalidade.Escala2 import Escala2

class ObterHarmonias2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()
        ho = HarmoniaObtida2()
        self.ec = Escala2()

        self.contador = ho.getContador()
        self.degrau = self.ec.get_degrau_from_harmonizar(self.contador)
        self.altura = edp.getAlturas(self.contador)
        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaBeatHarmonizar = bho.get_beat_harm()

    def obter_harmonias(self):
        global harmoniaDegrau

        # retornar estados ocultos para harmonização
        vt = Viterbi()
        hidden_st = vt.get_hidden_state(self.contador)

        # retorna primeiro grau da harmoniaPrimeiroGrau
        match hidden_st:
            case 'T':  # se Tônica, harmonia = degrau 1 da escala
                harmoniaDegrau = 1

            case 'S':  # se Subdominante, harmonia = degrau 4 da escala
                harmoniaDegrau = 4

            case 'D':  # se Dominante, harmonia = degrau 5 da escala
                harmoniaDegrau = 5

            case _:
                harmoniaDegrau = None

    def get_harmonia_from_degrau(self):
        return harmoniaDegrau
