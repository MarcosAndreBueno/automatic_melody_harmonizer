from teorema_bayes.harmonizar_dados.ObterDuracao2 import ObterDuracao2
from music21 import note, chord, meter

class EscreverAcorde:
    def escrevendo_acorde(self, s2, contador, formulaAnterior, listaAcorde, listaBeatHarmonizar,
                          listaDuracao, listaFormulaCompasso, listaCompasso, haveraGaps, listaObjeto):
        hd = ObterDuracao2()
        duracaoNota = hd.harmonizando2(contador, listaBeatHarmonizar, listaDuracao, listaCompasso)
        # designando fórmula de compasso
        formulaAtual = listaFormulaCompasso[contador]
        if formulaAtual != formulaAnterior:
            ts = meter.TimeSignature(formulaAtual)
            s2.append(ts)
        # formando notas do acorde
        nota1 = listaAcorde[0]
        nota2 = listaAcorde[1]
        nota3 = listaAcorde[2]
        n1 = note.Note(pitch=nota1,
                       quarterLength=duracaoNota)  # criando notas com base nos valores retirados das listas.
        n2 = note.Note(pitch=nota2,
                       quarterLength=duracaoNota)  # criando acordes com base nos valores retirados das listas.
        n3 = note.Note(pitch=nota3,
                       quarterLength=duracaoNota)  # criando acordes com base nos valores retirados das listas
        c1 = chord.Chord([n1, n2, n3])

        # com insert especificamos a posição do acorde na partitura
        if haveraGaps == True:
            # nota objeto music21 usaremos o offset da melodia harmonizada como index para o acorde.
            notaAtual = listaObjeto[contador]
            notaAtual = notaAtual.offset
            s2.insert(notaAtual, c1)
        # com append não especificamos a posição, mas adicionamos em lista, à frente do último acorde adicionado
        else:
            s2.append(c1)
        return s2