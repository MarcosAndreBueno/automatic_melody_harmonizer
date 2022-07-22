from music21 import note, scale


class Tonalidade2:
    def set_tom(self,tom):
        global tomInserido
        tomInserido=tom

    def get_tom(self):
        return tomInserido

    def degrau_nota(self, altura,tom):
        if altura == "P":
            return None
        print("altura",altura)
        notaAltura = note.Note(altura)            # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name         # Ex: music21 note 60 = Dó
        print(notaAtual, tom)
        sc = scale.MajorScale(tom)                # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        return degrau