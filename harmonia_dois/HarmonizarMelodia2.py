from harmonia_dois.CompletarAcorde2 import CompletarAcorde2
from harmonia_dois.ObterEnarmonia2 import ObterEnarmonia2
from harmonia_dois.ObterOitava2 import ObterOitava2
from harmonia_dois.ObterHarmonias2 import ObterHarmonias2
from harmonia_dois.TrabalhandoGaps2 import TrabalhandoGaps2
from music21 import stream, note


class HarmonizarMelodia2:
    def harmonizando2(self, listaNome, listaAlturas, listaBeatHarmonizar,
                      listaDuracao, listaFormulaCompasso, listaCompasso):
        s2 = stream.Stream()
        oh = ObterHarmonias2()
        oo = ObterOitava2()
        ca = CompletarAcorde2()
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
            nomeNota = ObterEnarmonia2().enarmonia(listaAlturas, contador)
            beatHarmonizar = listaBeatHarmonizar[contador]
            if beatHarmonizar == 1: # se o beat atual for aceito para ser harmonizado
                altura = listaAlturas[contador]
                oitava = oo.oitava()
                # se não for o último acorde
                if nomeNota != "P" and contador != ultimoAcorde:
                    altura = oh.obter_harmonias(nomeNota, altura, oitava)
                    # se a nota atual não for acidente ocorrente
                    if altura != "acidente ocorrente":
                        listaAcorde = ca.completando_acorde(oitava, altura)
                        s2 = ca.escrevendo_acorde(s2, contador, formulaAnterior,
                                                  listaAcorde, listaBeatHarmonizar,
                                                  listaDuracao, listaFormulaCompasso,
                                                  listaCompasso, haveraGaps)
                # se for o último acorde, escolher harmonização = tônica da tonalidade
                if nomeNota != "P" and contador == ultimoAcorde:
                    altura = oh.obter_ultimo_acorde(altura, oitava)
                    if altura != "acidente ocorrente":
                        listaAcorde = ca.completando_acorde(oitava, altura)
                        s2 = ca.escrevendo_acorde(s2, contador, formulaAnterior,
                                                  listaAcorde, listaBeatHarmonizar,
                                                  listaDuracao, listaFormulaCompasso,
                                                  listaCompasso, haveraGaps)

                    # se pausa, seguir adiante
                elif nomeNota == "P":
                    continue

            # se o beat for 0, prepara listaAcorde para próximo for
            else:
                listaAcorde.clear()

            formulaAnterior = listaFormulaCompasso[contador]
            contador+=1
        return s2

    '''
    1. Itera lista nome
    2. Reconhece se o beat é igual a 1
    3. Se sim, vai para possiveis harmonizações
    4. Lá dentro sortea uma nota
    5. Completa os acordes dessa nota
    6. Duração? 
    Se divisível por 2 e denominador 4 = 2, denominador 8 = 1
    se divisível por 3 e denominador 4 = 3, denominador 8 = 1.5

    for i em listaNome:
        pega nome

        se X faça:
            harmoniaSorteada = sorteia harmonia
            duracao = analise formula de comp. e devolve a duração
    '''