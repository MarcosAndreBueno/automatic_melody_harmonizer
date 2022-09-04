from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.extrair_dados.beat import ValidarBeatBinario, ValidarBeatTernario
from harmonizar_viterbi.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2


class ValidarBeats2:
    def __init__(self):
        fc = FormulaCompasso2()
        self.listaFormulaCompasso = fc.get_fc()

    def validar_beats(self, contador):
        quantidade = ContadorFormulaCompasso2().get()
        formulaAtual = self.listaFormulaCompasso[contador]  # fórmula de compasso
        formulaAtual = int(formulaAtual[0])                 # 4/4 = 4 ... 3/4 = 3 ...
        # o iterador começará de onde parou a última vez, e parará quando o formula de compasso mudar
        final = contador + quantidade
        for x in range(contador, final):
            # binária
            if formulaAtual % 2 == 0:
                listaBeatHarmonizar = ValidarBeatBinario.validar_beat_binario(contador)

            # ternária
            elif formulaAtual % 3 == 0:
                listaBeatHarmonizar = ValidarBeatTernario.validar_beat_ternario(contador)

            contador += 1  # pois o contador estará parado na fórmula de compasso que já foi iterada

        bho = BeatsHarmonizarObtidos2()
        bho.set_beat_harm(listaBeatHarmonizar)
