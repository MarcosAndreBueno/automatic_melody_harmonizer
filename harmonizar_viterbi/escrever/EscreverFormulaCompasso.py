from music21 import meter
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2

class EscreverFormulaCompasso:
    def __init__(self):
        self.ho = HarmoniaObtida2()
        fc = FormulaCompasso2()
        self.listaFormulaCompasso = fc.get_fc()

    def escrever_f_c(self, stream):
        # escrever a fórmula de compasso
        contador = self.ho.getContador()
        if contador > 0:
            formulaAtual = self.listaFormulaCompasso[contador]
            formulaAnterior = self.listaFormulaCompasso[contador-1]
            if formulaAtual != formulaAnterior:  # reescrever a fórmula, caso mude
                ts = meter.TimeSignature(formulaAtual)
                stream.append(ts)
        else:                                    # escrever fórmula no primeiro compasso
            formulaAtual = self.listaFormulaCompasso[contador]
            ts = meter.TimeSignature(formulaAtual)
            stream.insert(contador, ts)

    def escrever_f_c_harmonia(self):
        s2 = self.ho.getStreamHarmonia()
        self.escrever_f_c(s2)

    def escrever_f_c_melodia(self):
        s1 = self.ho.getStreamMelodia()
        self.escrever_f_c(s1)
