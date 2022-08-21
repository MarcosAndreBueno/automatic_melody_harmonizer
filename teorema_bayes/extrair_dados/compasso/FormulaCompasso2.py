import numpy
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from music21 import meter, corpus, note


class FormulaCompasso2:
    global listaFormulaCompasso
    listaFormulaCompasso = []

    def set_fc(self):
        ip = InserirPartitura()
        filePath = ip.get_path()
        partitura = corpus.parse(filePath)
        for n in partitura.flat:
            if type(n) is meter.TimeSignature:
                string = str(n)
                start = 29
                stop = int(len(string))-1
                formula = string[start:stop]
            if type(n) is note.Note or type(n) is note.Rest:
                listaFormulaCompasso.append(formula)

    def get_fc(self, contador=None):
        if contador != None:
            return listaFormulaCompasso[contador]
        else:
            return listaFormulaCompasso