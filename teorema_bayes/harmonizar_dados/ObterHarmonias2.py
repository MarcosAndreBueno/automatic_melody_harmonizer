from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.harmonizar_dados.Escala2 import Escala2
from teorema_bayes.harmonizar_dados.ObterOitava2 import ObterOitava2
from teorema_bayes.harmonizar_dados.SortearHarmonia2 import SortearHarmonia2

class ObterHarmonias2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()
        oo = ObterOitava2()
        ho = HarmoniaObtida2()
        ec = Escala2()

        self.degrau = ec.degrau_nota()
        self.altura = ho.getAltura()
        self.oitava = oo.oitava()
        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaBeatHarmonizar = bho.get()

    def obter_harmonias(self):
        global harmonia
        oitava = self.oitava
        sh = SortearHarmonia2()

        # retorna primeiro grau da harmoniaPrimeiroGrau
        match self.degrau:
            case 1:  # se a nota for Dó quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)                            # pedindo para trazer a oitava da harmonia_um
                if sorteio == 1:
                    harmonia = self.altura+oitava                         # se valor sorteado = 1, nota = 60+(-12) = Dó3
                else:
                    harmonia = self.altura+9+oitava                       # se valor sorteado = 2, nota = 60+(-12) = Sol3

            case 2:  # se a nota for Ré quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+9+oitava                      # +9 resulta na 6 maior de ré (Ré natural)

            case 3:  # se a nota for Mi quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+8+oitava                      # +8 resulta na 6 menor de mi (Dó natural)

            case 4:  # se a nota for Fá quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+9+oitava                      # +9 resulta na 6 maior de fá (Ré natural)

            case 5:  # se a nota for Sol quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+9+oitava                      # +9 resulta na 6 maior de sol (Mi natural)

            case 6:  # se a nota for Lá quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+8+oitava                      # +8 resulta na 6 menor de lá (Fá natural)

            case 7:  # se a nota for Si quais serão as possíveis harmonias?
                sorteio = sh.sortear(1,2)
                if sorteio == 1:
                    harmonia = self.altura+oitava
                else:
                    harmonia = self.altura+8+oitava                      # +8 resulta na 6 menor de si (Sol natural)

            case _:                                                      # case _ funciona como else
                harmonia = "AO" # acidente ocorrente

    def get(self):
        return harmonia
