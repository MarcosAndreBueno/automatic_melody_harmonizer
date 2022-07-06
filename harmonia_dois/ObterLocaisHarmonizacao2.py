'''
    esta classe retorna true se o compasso e o beat forem escolhidos para serem harmonizados
    todos compassos pares aceitam o beat impar e ignoram o beat par
    todos compassos ímpares, que podem ser divididos por 3, ignoram 2 beat a cada 1 beat aceito
    se o beat terminar diferente de .0, é ignorado (Ex: 5/4 > beats validos > 1 e 3 > beats invalidos 2,4, 1.5, 3.25 etc)
'''
from harmonia_dois.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from harmonia_dois.BuscarBeat2 import BuscarBeat2

class ObterLocaisHarmonizacao2:
    def possiveis_locais(self, listaFormulaCompasso, listaBeat, listaNome):
        contador = 0
        cfc = ContadorFormulaCompasso2()
        bb = BuscarBeat2()
        tamanhoLista = len(listaFormulaCompasso)
        listaBeatHarmonizar = []
        while contador < tamanhoLista:
            # compasso repetições
            quantidade = cfc.repeticoes_compasso(listaFormulaCompasso, tamanhoLista, contador)
            # itera esse numero de repetições, começando sempre da posição ainda não iterada
            listaBeatHarmonizar = bb.encontrando_beats(contador, quantidade, listaFormulaCompasso, listaBeat, listaBeatHarmonizar, listaNome)
            contador+=quantidade
        return listaBeatHarmonizar