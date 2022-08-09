from music21 import note, scale
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class Escala2:
    def __init__(self):
        tl = Tonalidade2()
        edp = ExtrairDadosPartitura()
        ho = HarmoniaObtida2()

        self.altura = ho.getAltura()
        self.tom = tl.get_tom()
        self.listaAlturas = edp.getAlturas()

    def degrau_nota(self):
        if self.altura == "P":
            return None
        notaAltura = note.Note(self.altura)             # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name               # Ex: music21 note 60 = Dó
        sc = scale.MajorScale(self.tom)                 # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        return degrau