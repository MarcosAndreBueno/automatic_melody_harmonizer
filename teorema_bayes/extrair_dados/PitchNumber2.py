from music21 import pitch


class PitchNumber2:
    def obtendo_pitches(self, listaAlturas, number, n):
        if number == 1:                 # is note.Note
            n = n.pitches               # ex: object music21.pitch.Pitch C4
            n = str(n)
            start = 21
            stop = len(n) - 3
            n = n[start:stop]           # ex: object music21.pitch.Pitch C4 -> n = C4
            p = int(pitch.Pitch(n).ps)  # ex: C4 -> p = 60
            listaAlturas.append(p)
            return listaAlturas
        if number == 0:     # is note.Rest
            listaAlturas.append("P")
            return listaAlturas