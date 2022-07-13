from teorema_bayes.ObterDuracao2 import ObterDuracao2
from music21 import note, chord, meter, scale


class CompletarAcorde2:
    def completando_acorde(self, oitava, altura):
        # transformando número da nota em nome de nota
        notaAltura = note.Note(altura)            # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name         # Ex: music21 note 60 = Dó
        sc = scale.MajorScale('C')                      # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        listaAcorde = []
        print("grau escala",degrau,"nota",notaAtual)

        # acorde maior na tonalidade maior -> degraus 1,4,5
        if degrau == 1 or degrau == 4 or degrau == 5:
            nota1 = altura+oitava
            nota2 = altura+4+oitava
            nota3 = altura+7+oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde menor na tonalidade maior -> degraus 2,3,6
        elif degrau == 2 or degrau == 3 or degrau == 6:
            nota1 = altura + oitava
            nota2 = altura + 3 + oitava
            nota3 = altura + 7 + oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        # acorde diminuto na tonalidade maior -> degrau 7
        elif degrau == 7:
            nota1 = altura + oitava
            nota2 = altura + 3 + oitava
            nota3 = altura + 6 + oitava
            listaAcorde.append(nota1)
            listaAcorde.append(nota2)
            listaAcorde.append(nota3)
        return listaAcorde

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

        # insert especifica posição do acorde na partitura
        if haveraGaps == True:
            # nota objeto music21 usaremos o offset da nota harmonizada como index para o acorde.
            notaAtual = listaObjeto[contador]
            notaAtual = notaAtual.offset
            s2.insert(notaAtual, c1)
        # append não especifica posição, mas adiciona em lista, à frente do último acorde adicionado
        else:
            s2.append(c1)
        return s2


