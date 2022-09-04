from harmonizar_viterbi.escrever.EscreverArmaduraClave import EscreverArmaduraClave
from harmonizar_viterbi.escrever.EscreverFormulaCompasso import EscreverFormulaCompasso
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from music21 import stream, meter, note
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class ReescreverMelodia2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        ho = HarmoniaObtida2()
        self.s1 = ho.getStreamMelodia()
        self.listaAlturas = edp.getAlturas()
        self.listaOitava = edp.getOitava()
        self.listaDuracao = edp.getDuracao()
        self.listaFormulaCompasso = fc.get_fc()
        self.tamanhoLista = len(self.listaFormulaCompasso)
        self.listaObjeto = edp.getObjeto()

    def melodia_original2(self):
        # contador para estabelecer index para escrever a fórmula de compasso
        contador = 0
        ho = HarmoniaObtida2()
        ho.setContador(contador)

        cfc = ContadorFormulaCompasso2()
        efc = EscreverFormulaCompasso()
        eac = EscreverArmaduraClave()

        while contador < self.tamanhoLista:
            # contador para estabelecer index para escrever a fórmula de compasso
            ho.setContador(contador)

            # quantidade = chamar contadorformula
            quantidade = cfc.repeticoes_compasso(contador)

            # iterando fórmulas de compassos
            final = contador+quantidade
            for x in range(contador, final):
                # escrever formula de compasso da posição atual
                efc.escrever_f_c_melodia()

                # escrever armadura de clave da posição atual
                eac.escrever_a_c_melodia()

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
                notaAtualOffSet = self.listaObjeto[x]
                notaAtualOffSet = notaAtualOffSet.offset
                self.s1.insert(notaAtualOffSet, n1)

                # setContador evita armadura de clave ser reescrita no offSet 0
                ho.setContador(1)

            # contador+quantidade para evitar reescrever mesmas fórmulas (ex 4/4 -> 4/4)
            contador+=quantidade

        ho = HarmoniaObtida2()
        ho.setStreamMelodia(self.s1)
