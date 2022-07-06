import numpy
from music21 import meter, note


class FormulaCompasso2:
    def get_formula_compasso2(self, partitura):
        listaFormulaCompasso = []
        for n in partitura.flat:
            if type(n) is meter.TimeSignature:
                string = str(n)
                start = 29
                stop = int(len(string))-1
                formula = string[start:stop]
            if type(n) is note.Note or type(n) is note.Rest:
                listaFormulaCompasso.append(formula)

        return listaFormulaCompasso