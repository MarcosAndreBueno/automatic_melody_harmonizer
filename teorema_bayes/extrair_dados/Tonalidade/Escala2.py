from music21 import note, scale
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class Escala2:
    def __init__(self):
        tl = Tonalidade2()
        self.tom = tl.get_tom()
        self.contador = 0
        self.altura = 0
        self.listaAlturas = []
        self.listaDegrau = []
        self.edp = ExtrairDadosPartitura()
        self.ho = HarmoniaObtida2()

    # se chamado de dentro do diretório harmonizar_dados, retorna 1 altura
    def get_degrau_from_harmonizar(self, contador=None):
        if contador == None :
            contador = self.ho.getContador()
        altura = self.edp.getAlturas(contador)
        degrau = self.get_degrau(altura)
        return degrau

    # se chamado de outros métodos retorna lista com todas alturas
    def get_degrau_from_another(self):
        self.listaAlturas = self.edp.getAlturas()
        for i in self.listaAlturas:
            self.listaDegrau.append(self.get_degrau(i))
        return self.listaDegrau

    def get_degrau(self, altura):
        if altura == "P":
            return None
        notaAltura = note.Note(altura)             # Ex: note.Note(60)
        notaAtual = notaAltura.pitch.name               # Ex: music21 note 60 = Dó
        sc = scale.MajorScale(self.tom)                 # Ex: escala de "C"
        degrau = sc.getScaleDegreeFromPitch(notaAtual)  # Ex: nota C = degrau 1, nota A = degrau 6...
        return degrau