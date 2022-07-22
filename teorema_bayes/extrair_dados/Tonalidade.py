from music21 import note, scale


class Tonalidade2:
    def __init__(self):
        self.tonalidade = "C"

    def degrau_nota(self, altura):
        if altura == "P":
            return None
        tonalidade = self.tonalidade
        notaAltura = note.Note(altura)            # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name         # Ex: music21 note 60 = Dó
        sc = scale.MajorScale(tonalidade)               # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        return degrau