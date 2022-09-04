from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from harmonizar_viterbi.extrair_dados.compasso.PrimeiroCompasso import PrimeiroCompasso
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from harmonizar_viterbi.harmonizar_dados.CompletarAcorde2 import CompletarAcorde2
from harmonizar_viterbi.escrever.EscreverAcorde import EscreverAcorde
from harmonizar_viterbi.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2
from harmonizar_viterbi.harmonizar_dados.UltimoAcorde2 import UltimoAcorde2


class HarmonizarMelodia2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        bho = BeatsHarmonizarObtidos2()

        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaBeatHarmonizar = bho.get_beat_harm()
        self.listaCompasso = edp.getCompasso()
        self.listaFormulaCompasso = fc.get_fc()
        self.listaObjeto = edp.getObjeto()

    def harmonizando2(self):
        contador = 0

        # se nota final fizer parte da tríade da tônica, força harmonização na tônica.
        for i in self.listaNome:
            ho = HarmoniaObtida2()
            ho.setContador(contador)
            beatHarmonizar = self.listaBeatHarmonizar[contador]
            # se o beat atual for aceito para ser harmonizado
            if beatHarmonizar == 1:
                nomeNota = self.listaNome[contador]

                # obter fundamental da harmonia
                oh = ObterHarmonias2()
                oh.set_harmonias()
                harmoniaDegrau = oh.get_harmonia_from_degrau()

                # ignorar acidentes ocorrentes e pausas
                if harmoniaDegrau != None and nomeNota != "P":
                    ca = CompletarAcorde2()
                    ca.completando_acorde()
                    ea = EscreverAcorde()
                    ea.escrevendo_acorde()

                    '''
                    Trabalhar últimoAcorde na tônica
                    
                    oua = UltimoAcorde2()
                    ultimoAcorde = oua.posicao_ultimo_acorde()
                    
                    if contador != ultimoAcorde: # se não for o último acorde
                        ca.completando_acorde()
                        ea = EscreverAcorde()
                        ea.escrevendo_acorde()
                    else:                        # se for último acorde, harmonizar na tônica
                        ca.completando_acorde()
                        ea = EscreverAcorde()
                        ea.escrevendo_acorde()
                    '''


            contador+=1
