'''
    esta classe retorna true se o compasso e o beat forem escolhidos para serem harmonizados
    todos compassos pares aceitam o beat impar e ignoram o beat par
    todos compassos ímpares, que podem ser divididos por 3, ignoram 2 beats a cada 1 beat aceito
    se o beat terminar diferente de .0, é ignorado
    (Ex: Fórmula de Compasso 5/4 -> beats validos -> 1 e 3 | beats invalidos -> 2,4, 1.5, 3.25 etc)
    Em suma, os beats fora da cabeça do tempo e que servem de condução serão ignorados.
'''
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.extrair_dados.beat.ValidarBeats2 import ValidarBeats2

class ObterBeatsHarmonizacao2:
    def __init__(self):
        fc = FormulaCompasso2()
        self.listaFormulaCompasso = fc.get_fc()
        self.tamanhoLista = len(self.listaFormulaCompasso)

    def obter_beats(self):
        contador = 0
        cfc = ContadorFormulaCompasso2()
        vb = ValidarBeats2()
        listaBeatHarmonizar = []
        while contador < self.tamanhoLista:
            # compasso repetições
            quantidade = cfc.repeticoes_compasso(contador)
            vb.validar_beats(contador)
            # iterar todos compassos iguais
            contador+=quantidade