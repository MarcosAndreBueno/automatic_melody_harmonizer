from music21 import stream, key, note, pitch

# ___Criando uma partitura em Dó maior com poucas notas
s1 = stream.Stream()
ks = key.KeySignature(2)  # 2 sustenidos, modo maior
s1.append(ks)
print(ks.asKey(), "sustenidos", ks.sharps)
nota1 = note.Note("C4")
nota2 = note.Note("D4")
nota3 = note.Note("E4")
nota4 = note.Note("F4")
nota5 = note.Note("G4")
nota6 = note.Note("A4")
nota7 = note.Note("B4")
nota8 = note.Note("C4")
s1.append(nota1)
s1.append(nota2)
s1.append(nota3)
s1.append(nota4)
s1.append(nota5)
s1.append(nota6)
s1.append(nota7)
s1.append(nota8)

# visualizar partitura
for i in s1.notes:
    print(i.pitch.nameWithOctave, end=' ')

# ___Adicionar clave de Mi maior e transpor notas
ks = key.KeySignature(4)  # 4 sustenidos, modo maior
s1.append(ks)
for i in s1.notes:
    nome = i.pitch.name
    altura = pitch.Pitch(nome)
    transposer = ks.transposePitchFromC(altura)
    novaNota = note.Note(transposer)
    s1.append(novaNota)
    print("nome", nome, "altura", altura, "transposer", transposer)
# resultado