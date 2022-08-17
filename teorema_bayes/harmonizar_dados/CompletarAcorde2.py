from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.extrair_dados.Tonalidade.Escala2 import Escala2
from teorema_bayes.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2
from teorema_bayes.harmonizar_dados.ObterOitava2 import ObterOitava2


class CompletarAcorde2:
    def __init__(self):
        oo = ObterOitava2()
        oh = ObterHarmonias2()
        ho = HarmoniaObtida2()
        edp = ExtrairDadosPartitura()
        ec = Escala2()

        self.contador = ho.getContador()
        self.degrau = ec.get_degrau_from_harmonizar()
        self.altura = edp.getAlturas(self.contador)
        self.harmonia = oh.get()
        self.oitava = oo.oitava()

    def completando_acorde(self):
        global listaAcorde
        listaAcorde = []

        # acorde maior na tonalidade maior -> degraus 1,4,5
        if self.degrau == 1 or self.degrau == 4 or self.degrau == 5:
            nota1 = self.altura + self.oitava
            nota2 = self.altura + 4 +self.oitava
            nota3 = self.altura + 7 +self.oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde menor na tonalidade maior -> degraus 2,3,6
        elif self.degrau == 2 or self.degrau == 3 or self.degrau == 6:
            nota1 = self.altura + self.oitava
            nota2 = self.altura + 3 + self.oitava
            nota3 = self.altura + 7 + self.oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde diminuto na tonalidade maior -> degrau 7
        elif self.degrau == 7:
            nota1 = self.altura + self.oitava
            nota2 = self.altura + 3 + self.oitava
            nota3 = self.altura + 6 + self.oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)

    def get(self):
        return listaAcorde
