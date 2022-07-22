from music21 import *

listaAcorde = []

nota = note.Note('C')
listaAcorde.append(nota)
nota = note.Note('D')
listaAcorde.append(nota)
nota = note.Note('E')
listaAcorde.append(nota)
nota = note.Note('F')
listaAcorde.append(nota)
nota = note.Note('G')
listaAcorde.append(nota)
nota = note.Note('A')
listaAcorde.append(nota)
nota = note.Note('B')
listaAcorde.append(nota)

sc = scale.MajorScale('C')                      # Ex: escala de "C"
for i in listaAcorde:
    degrau = sc.getScaleDegreeFromPitch(i)  # Ex: nota C = degrau 1, nota A = degrau 6...
    print("Dó Maior: NOTA",i,"degrau",degrau)

print("\n\n")

listaAcorde.clear()

nota = note.Note('A')
listaAcorde.append(nota)
nota = note.Note('B')
listaAcorde.append(nota)
nota = note.Note('C#')
listaAcorde.append(nota)
nota = note.Note('D')
listaAcorde.append(nota)
nota = note.Note('E-')
listaAcorde.append(nota)
nota = note.Note('F#')
listaAcorde.append(nota)
nota = note.Note('G#')
listaAcorde.append(nota)

sc = scale.MajorScale('A')                      # Ex: escala de "C"
for i in listaAcorde:
    degrau = sc.getScaleDegreeFromPitch(i)  # Ex: nota C = degrau 1, nota A = degrau 6...
    print("Lá Maior, NOTA", i, "degrau", degrau)
