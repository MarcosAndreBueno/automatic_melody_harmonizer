from music21 import note, chord, meter, scale


class CompletarAcorde2:
    def completando_acorde(self, oitava, altura):
        # transformando número da nota em nome de nota
        notaAltura = note.Note(altura)            # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name         # Ex: music21 note 60 = Dó
        sc = scale.MajorScale('C')                      # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        listaAcorde = []

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


