class ContadorFormulaCompasso2:
    def repeticoes_compasso(self, listaFormulaCompasso, tamanhoLista, contador):
        formulaAtual = listaFormulaCompasso[contador]
        formulaAntiga = formulaAtual
        quantidade = 0
        for x in range(contador, tamanhoLista):
            formulaAtual = listaFormulaCompasso[contador]
            if formulaAtual == formulaAntiga:
                quantidade += 1
            if formulaAtual != formulaAntiga:
                return quantidade
            formulaAntiga = formulaAtual
            contador += 1
        return quantidade