class BuscarBeat2:
    def encontrando_beats(self, contador, quantidade, listaFormulaCompasso, listaBeat, listaBeatHarmonizar, listaNome):
        formulaAtual = listaFormulaCompasso[contador]
        formulaAtual = int(formulaAtual[0])
        final = contador + quantidade   # o iterador começará de onde parou a última vez, e parará quando o formula de compasso mudar
        for x in range(contador, final):
            # binária
            if formulaAtual % 2 == 0:
                listaBeatHarmonizar = self.validar_beat_binario(contador, listaBeat, listaBeatHarmonizar, listaNome)

            # ternária
            elif formulaAtual % 3 == 0:
                listaBeatHarmonizar = self.validar_beat_ternario(contador, listaBeat, listaBeatHarmonizar, listaNome)

            contador += 1  # pois o contador estará parado na fórmula de compasso que já foi iterada
        return listaBeatHarmonizar

    def validar_beat_binario(self, contador, listaBeat, listaBeatHarmonizar, listaNome):
        # se pausa, não harmonizar
        nome = listaNome[contador]
        # binário
        beat = listaBeat[contador]
        beat = str(beat)
        if beat == "1.0" or beat == "3.0":
            if nome == "P":
                listaBeatHarmonizar.append(2)
            else:
                listaBeatHarmonizar.append(1)
        else:
            # se o beat não for harmaonizado, ele ainda sim deve ser considerado
            # na formação da stream, mesmo que seja para ser ignorado, por isso receberá 0.
            listaBeatHarmonizar.append(0)
        return listaBeatHarmonizar

    def validar_beat_ternario(self, contador, listaBeat, listaBeatHarmonizar, listaNome):
        nome = listaNome[contador]
        if nome == "P":
            listaBeatHarmonizar.append(0)
            return listaBeatHarmonizar

        # ternária
        beat = listaBeat[contador]
        beat = str(beat)
        if beat == "1.0":
            listaBeatHarmonizar.append(1)
        else:
            listaBeatHarmonizar.append(0)

        return listaBeatHarmonizar