class ObterDuracao2:
    def harmonizando2(self, contador, listaBeatHarmonizar, listaDuracao, listaCompasso):
        # obtendo repetições da mesma fórmula de compasso
        tamanhoLista = len(listaBeatHarmonizar)
        duracaoFinal = 0
        controle = 0
        compassoAnterior = compassoAtual = listaCompasso[contador]
        for x in range(contador, tamanhoLista):
            beatHarm = listaBeatHarmonizar[x]
            compassoAtual = listaCompasso[x]
            duracao = listaDuracao[x]
            if compassoAtual != compassoAnterior:
                break                           # duracao acorde não ultrapassará valor máximo do compasso
            if beatHarm == 1 and controle != 0:
                break
            duracaoFinal += duracao             # duracao acorde = soma das duracoes entre dois beatHarmonizar=1
            controle+=1
        return duracaoFinal

