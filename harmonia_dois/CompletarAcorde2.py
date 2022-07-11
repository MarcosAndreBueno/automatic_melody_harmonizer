from harmonia_dois.ObterDuracao2 import ObterDuracao2
from music21 import note, chord, meter


class CompletarAcorde2:
    def completando_acorde(self, oitava, altura):
        # transformando número da nota em nome de nota
        notaAltura = note.Note(altura)            # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name         # Ex: music21 note 60 = Dó
        listaAcorde = []
        # acorde maior na tonalidade maior
        if notaAtual == 'C' or notaAtual == 'F' or notaAtual == 'G':
            nota1 = altura+oitava
            nota2 = altura+4+oitava
            nota3 = altura+7+oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde menor na tonalidade maior
        if notaAtual == 'D' or notaAtual == 'E' or notaAtual == 'A':
            nota1 = altura + oitava
            nota2 = altura + 3 + oitava
            nota3 = altura + 7 + oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde diminuto na tonalidade maior
        if notaAtual == 'B':
            nota1 = altura + oitava
            nota2 = altura + 3 + oitava
            nota3 = altura + 6 + oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        return listaAcorde

    def escrevendo_acorde(self, s2, contador, formulaAnterior, listaAcorde, listaBeatHarmonizar,
                          listaDuracao, listaFormulaCompasso, listaCompasso, haveraGaps):
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

        # usar append evita o trabalho de ter bugs que teriam que ser corrigidos com offset
        if haveraGaps == True:
            s2.insert(contador, c1)
        if haveraGaps == False:
            s2.append(c1)
        return s2


