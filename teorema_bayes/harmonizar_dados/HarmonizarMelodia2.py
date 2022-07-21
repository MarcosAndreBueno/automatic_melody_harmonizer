from teorema_bayes.harmonizar_dados.CompletarAcorde2 import CompletarAcorde2
from teorema_bayes.escrever.EscreverAcorde import EscreverAcorde
from teorema_bayes.harmonizar_dados.ObterEnarmonia2 import ObterEnarmonia2
from teorema_bayes.harmonizar_dados.ObterOitava2 import ObterOitava2
from teorema_bayes.harmonizar_dados.ObterHarmonias2 import ObterHarmonias2
from teorema_bayes.harmonizar_dados.TrabalhandoGaps2 import TrabalhandoGaps2
from music21 import stream


class HarmonizarMelodia2:
    def harmonizando2(self, listaNome, listaAlturas, listaBeatHarmonizar,
                      listaDuracao, listaFormulaCompasso, listaCompasso, listaObjeto):
        s2 = stream.Stream()
        oe = ObterEnarmonia2()
        oh = ObterHarmonias2()
        oo = ObterOitava2()
        ca = CompletarAcorde2()
        ea = EscreverAcorde()
        tg = TrabalhandoGaps2()
        listaAcorde = []
        formulaAnterior = 0
        contador = 0
        # se verdadeiro, utiliza stream.insert ao invés de stream.append
        haveraGaps = tg.havera_gaps(listaBeatHarmonizar, listaNome, listaAlturas)
        # se nota final fizer parte da tríade da tônica, força harmonização na tônica.
        ultimoAcorde = oh.posicao_ultimo_acorde(listaNome, listaBeatHarmonizar)

        for i in listaNome:
            # Transforma o pitch em nota para considerar enarmonia. ex: 64(E#) -> vira -> F
            nomeNota = oe.enarmonia(listaAlturas, contador)
            beatHarmonizar = listaBeatHarmonizar[contador]

            # se o beat atual for aceito para ser harmonizado e não for pausa
            if beatHarmonizar == 1:
                altura = listaAlturas[contador]
                oitava = oo.oitava()
                altura = oh.obter_harmonias(nomeNota, altura, oitava)

                if altura != "acidente ocorrente" and nomeNota != "P": # ignorar acidentes e pausas
                    if contador != ultimoAcorde: # se não for o último acorde
                        listaAcorde = ca.completando_acorde(oitava, altura)
                        s2 = ea.escrevendo_acorde(s2, contador, formulaAnterior,
                                                  listaAcorde, listaBeatHarmonizar,
                                                  listaDuracao, listaFormulaCompasso,
                                                  listaCompasso, haveraGaps, listaObjeto)

                    elif contador == ultimoAcorde: # se último acorde, harmonizar_dados na tônica
                        listaAcorde = ca.completando_acorde(oitava, altura)
                        s2 = ea.escrevendo_acorde(s2, contador, formulaAnterior,
                                                  listaAcorde, listaBeatHarmonizar,
                                                  listaDuracao, listaFormulaCompasso,
                                                  listaCompasso, haveraGaps, listaObjeto)

            # se o beat for 0, prepara listaAcorde para próximo for
            else:
                listaAcorde.clear()

            formulaAnterior = listaFormulaCompasso[contador]
            contador+=1
        return s2