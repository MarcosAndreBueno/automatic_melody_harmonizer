from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.harmonizar_dados.CompletarAcorde2 import CompletarAcorde2
from teorema_bayes.escrever.EscreverAcorde import EscreverAcorde
from teorema_bayes.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2
from teorema_bayes.harmonizar_dados.UltimoAcorde2 import UltimoAcorde2


class HarmonizarMelodia2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        bho = BeatsHarmonizarObtidos2()

        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaBeatHarmonizar = bho.get()
        self.listaFormulaCompasso = fc.get()
        self.listaObjeto = edp.getObjeto()

    def harmonizando2(self):
        oua = UltimoAcorde2()
        contador = 0

        # se nota final fizer parte da tríade da tônica, força harmonização na tônica.
        ultimoAcorde = oua.posicao_ultimo_acorde()

        for i in self.listaNome:
            ho = HarmoniaObtida2()
            ho.setContador(contador)
            beatHarmonizar = self.listaBeatHarmonizar[contador]
            # se o beat atual for aceito para ser harmonizado
            if beatHarmonizar == 1:
                nomeNota = self.listaNome[contador]

                oh = ObterHarmonias2()
                oh.obter_harmonias()
                harmonia = oh.get()
                ca = CompletarAcorde2()

                if harmonia != None and nomeNota != "P": # ignorar acidentes ocorrentes e pausas
                    if contador != ultimoAcorde: # se não for o último acorde
                        ca.completando_acorde()
                        ea = EscreverAcorde()
                        ea.escrevendo_acorde()

                    else:                        # se for último acorde, harmonizar na tônica
                        ca.completando_acorde()
                        ea = EscreverAcorde()
                        ea.escrevendo_acorde()

            contador+=1