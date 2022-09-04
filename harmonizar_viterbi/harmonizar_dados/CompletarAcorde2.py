from music21 import scale
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from harmonizar_viterbi.extrair_dados.Tonalidade.Escala2 import Escala2
from harmonizar_viterbi.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2
from harmonizar_viterbi.harmonizar_dados.ObterOitava2 import ObterOitava2


class CompletarAcorde2:
    def __init__(self):
        oh = ObterHarmonias2()
        ho = HarmoniaObtida2()
        tl = Tonalidade2()

        self.contador = ho.getContador()
        self.harmoniaDegrau = oh.get_harmonia_from_degrau()
        self.tom = tl.get_tom()

    def completando_acorde(self):
        global listaAcorde
        listaAcorde = []

        # return pitch da fundamental escolhida pra harmonizar
        ec = Escala2()
        fundamental = ec.get_pitch_from_degrau(self.harmoniaDegrau) # em pitch Ex C -> 60

        # return oitava escolhida para harmonizar
        oo = ObterOitava2()
        oitava = oo.get_oitava_harm(fundamental, self.contador)

        # harmonia obtida por degrau
        match self.harmoniaDegrau:  # o match é desnecessário por enquanto, mas vale a pena visualizar
        # caso 1 = estamos no 1 grau ex: C
            case 1:
                nota1 = fundamental+oitava
                nota2 = fundamental+4+oitava
                nota3 = fundamental+7+oitava
                listaAcorde.append(nota1)
                listaAcorde.append(nota2)
                listaAcorde.append(nota3)
        # caso 4 = estamos no 4 grau ex: F
            case 4:
                nota1 = fundamental+oitava
                nota2 = fundamental+4+oitava
                nota3 = fundamental+7+oitava
                listaAcorde.append(nota1)
                listaAcorde.append(nota2)
                listaAcorde.append(nota3)
        # caso 5 = estamos no quinto grau ex: G
            case 5:
                nota1 = fundamental+oitava
                nota2 = fundamental+4+oitava
                nota3 = fundamental+7+oitava
                listaAcorde.append(nota1)
                listaAcorde.append(nota2)
                listaAcorde.append(nota3)

            case _:
                return None

    def get_lista_acorde(self):
        return listaAcorde
