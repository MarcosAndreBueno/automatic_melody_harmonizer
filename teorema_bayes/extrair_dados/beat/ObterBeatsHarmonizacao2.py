'''
    esta classe retorna true se o compasso e o beat forem escolhidos para serem harmonizados
    todos compassos pares aceitam o beat impar e ignoram o beat par
    todos compassos ímpares, que podem ser divididos por 3, ignoram 2 beat a cada 1 beat aceito
    se o beat terminar diferente de .0, é ignorado (Ex: 5/4 > beats validos > 1 e 3 > beats invalidos 2,4, 1.5, 3.25 etc)
'''
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.extrair_dados.beat.ValidarBeats2 import ValidarBeats2

class ObterBeatsHarmonizacao2:
    def __init__(self):
        fc = FormulaCompasso2()
        self.listaFormulaCompasso = fc.get()
        self.tamanhoLista = len(self.listaFormulaCompasso)

    def obter_beats(self):
        contador = 0
        cfc = ContadorFormulaCompasso2()
        vb = ValidarBeats2()
        listaBeatHarmonizar = []
        while contador < self.tamanhoLista:
            # compasso repetições
            quantidade = cfc.repeticoes_compasso(contador)
            # itera esse numero de repetições, começando sempre da posição ainda não iterada
            vb.validar_beats(contador)
            contador+=quantidade