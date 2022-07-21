from music21 import note


class ObterEnarmonia2:
    def enarmonia(self, listaAlturas,contador):
        altura = listaAlturas[contador]
        if altura != "P":
            n1 = note.Note(altura)
            nomeNota = n1.pitch.name
        else:
            return "P"
        return nomeNota