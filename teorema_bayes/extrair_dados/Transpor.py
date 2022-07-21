from music21 import note, stream, pitch, key


class Transpor:
    def __init__(self,partitura):
        self.partitura = partitura

    def iniciar(self):
        partitura = self.partitura
        print('entrou', partitura)
        provisoria = stream.Stream()

        ks = key.KeySignature(1)  # 4 sustenidos, modo maior
        provisoria.append(ks)
        contador = 0
        for i in partitura.flat.notesAndRests:
            if type(i) is note.Note:
                nome = i.pitch.name                         # nome da nota
                altura = pitch.Pitch(nome)                  # altura da nota
                transposer = ks.transposePitchFromC(altura) # transpor para Mi maior
                novaNota = note.Note(transposer)            # criar nota transposta
            elif type(i) is note.Rest:
                pausa = i.duration.quarterLength
                novaNota = note.Rest(pausa)

            provisoria.append(novaNota)                 # adicionar à stream
            contador+=1

        return provisoria