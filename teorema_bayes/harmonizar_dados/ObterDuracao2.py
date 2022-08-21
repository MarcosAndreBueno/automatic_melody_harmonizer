from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class ObterDuracao2:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        bho = BeatsHarmonizarObtidos2()
        ho = HarmoniaObtida2()
        fc = FormulaCompasso2()

        self.listaCompasso = edp.getCompasso()
        self.contador = ho.getContador()
        self.listaDuracao = edp.getDuracao()
        self.listaBeatHarmonizar = bho.get_beat_harm()

    def duracao_harmonia(self):
        global duracaoFinal
        # obtendo repetições da mesma fórmula de compasso
        tamanhoLista = len(self.listaBeatHarmonizar)
        duracaoFinal = 0
        controle = 0
        compassoAnterior = self.listaCompasso[self.contador]

        for x in range(self.contador, tamanhoLista):
            beatHarm = self.listaBeatHarmonizar[x]
            compassoAtual = self.listaCompasso[x]
            duracao = self.listaDuracao[x]
            if compassoAtual != compassoAnterior:
                break               # duracao acorde não ultrapassará valor máximo do compasso
            if beatHarm == 1 and controle != 0:
                break
            duracaoFinal += duracao # duracao acorde = soma das duracoes entre dois beatHarmonizar=1
            controle+=1

    def get(self):
        return duracaoFinal
