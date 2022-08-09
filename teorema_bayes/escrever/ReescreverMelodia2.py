from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from music21 import stream, meter, note
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class ReescreverMelodia2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        ho = HarmoniaObtida2()
        self.s1 = ho.getStreamMelodia()
        self.listaAlturas = edp.getAlturas()
        self.listaOitava = edp.getOitava()
        self.listaDuracao = edp.getDuracao()
        self.listaFormulaCompasso = fc.get()
        self.tamanhoLista = len(self.listaFormulaCompasso)

    def melodia_original2(self):
        contador = 0
        cfc = ContadorFormulaCompasso2()

        while contador < self.tamanhoLista:
            # quantidade = chamar contadorformula
            quantidade = cfc.repeticoes_compasso(contador)
            # formula atual
            formulaAtual = self.listaFormulaCompasso[contador]
            # set formula atual na stream
            ts = meter.TimeSignature(formulaAtual)
            self.s1.append(ts)
            # iterando fórmulas de compassos
            final = contador+quantidade
            for x in range(contador, final):
                notaAtual = self.listaAlturas[x]
                if notaAtual == "P":
                    d1 = self.listaDuracao[x]
                    n1 = note.Rest(quarterLength=d1)
                else:
                    pitch = self.listaAlturas[x]
                    nota = note.Note(pitch).pitch.name
                    oitava = str(self.listaOitava[x])
                    nota = nota+oitava
                    d1 = self.listaDuracao[x]
                    n1 = note.Note(nameWithOctave=nota, quarterLength=d1)
                self.s1.append(n1)
            contador+=quantidade
        ho = HarmoniaObtida2()
        ho.setStreamMelodia(self.s1)
