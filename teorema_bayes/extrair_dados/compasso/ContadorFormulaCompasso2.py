from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2


class ContadorFormulaCompasso2:
    def __init__(self):
        fc = FormulaCompasso2()
        self.listaFormulaCompasso = fc.get()
        self.tamanhoLista = len(self.listaFormulaCompasso)

    def repeticoes_compasso(self, contador):
        global quantidade
        formulaAtual = self.listaFormulaCompasso[contador]
        formulaAntiga = formulaAtual
        quantidade = 0
        for x in range(contador, self.tamanhoLista):
            formulaAtual = self.listaFormulaCompasso[contador]
            if formulaAtual == formulaAntiga:
                quantidade += 1
            if formulaAtual != formulaAntiga:
                return quantidade
            formulaAntiga = formulaAtual
            contador += 1
        return quantidade

    def get(self):
        return quantidade