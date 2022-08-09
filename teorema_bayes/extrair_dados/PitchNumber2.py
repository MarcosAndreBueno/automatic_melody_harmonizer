from music21 import pitch


class PitchNumber2:
    def obtendo_pitches(self,nota):
        nota = nota.pitches                 # ex: object music21.pitch.Pitch C4
        nota = str(nota)
        start = 21
        stop = len(nota) - 3
        nota = nota[start:stop]             # ex: object music21.pitch.Pitch C4 -> n = C4
        altura = int(pitch.Pitch(nota).ps)  # ex: C4 -> p = 60
        return altura
