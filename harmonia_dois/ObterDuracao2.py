from harmonia_dois.ContadorFormulaCompasso2 import ContadorFormulaCompasso2


class ObterDuracao2:
    def harmonizando2(self, contador, listaBeatHarmonizar, listaDuracao, listaCompasso):
        '''
        Todas fórmulas da música vão ser simplificadas em strong beats,
        e esse valor de simplificação guiará a escolha de durações.
        Esse valor é a soma de todas as durações do x em beatHarm
        que vão do valor 1 até o próximo 1

        Ex:
        listaDuracao        = ['1.0','1.0', '1.0', '0.5', '0.5', '1.0']
        listaBeatHarmoninar = ['1  ','0  ', '1  ', '0  ', '0  ', '0  ']
        listaAcordesDuracao = ['2  ',       '3  ']  # a duracao foi a soma do beat harmonizado + não harmonizados

        Ex: 4/4 > simplificação > 2
        Todos beats que serão harmonizados recebem a duração de 2 tempo
        Então, essa classe encontra quanto vale 2 denominadores dessa fórmula (neste caso 2 semínimas)

        Ex: 5/4 > simplificação > 2.3 ou 3.2
        se 2.3 beat 1 recebe duração de 2 tempos e beat 3 recebe duração de 3 tempos
        se 3.2 beat 1 recebe duração de 3 tempos e beat 3 recebe duração de 2 tempos
        Então,
        se 2.3 beat 1 vale 2 tempos (neste caso 2 semínimas)
               beat 2 vale 3 tempos (neste caso 3 semínimas)
        se 3.2 beat 1 vale 3 tempos (neste caso 3 semínimas)
               beat 3 vale 2 tempos (neste caso 2 semínimas)

        :return: duracaFinal (duracao específica para este acorde)
        '''

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

