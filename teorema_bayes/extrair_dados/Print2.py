# este método serve apenas para facilitar a leitura dos dados (da melodia) usados para harmonização.
from teorema_bayes.extrair_dados.Tonalidade2 import Tonalidade2


class Print2:
    def print_partitura_original2(self, partitura, listaObjeto, listaSimbolos, listaNome,
                                  listaOitava, listaDuracao, listaBeat, listaCompasso,
                                  listaFormulaCompasso, listaAlturas, listaBeatHarmonizar):

        # print tonalidade
        tl = Tonalidade2()
        tom = tl.get_tom()
        print('Tonalidade inserida pelo usuario: ', tom)
        print('Tonalidade encontrada pelo music21: ', partitura.analyze('key'))

        listaObjetoPrint = []
        for i in listaObjeto:
            objeto = str(i) + "  "
            listaObjetoPrint.append(objeto)
        print('listaObjetoPrint music21 nome:      ', listaObjetoPrint)
        listaObjetoPrint.clear()

        listaSimbolosPrint = []
        for i in listaSimbolos:
            objeto = str(i) + "  "
            listaSimbolosPrint.append(objeto)
        print('listaSimbolosPrint music21 nome:    ', listaSimbolosPrint)
        listaSimbolosPrint.clear()

        listaNomePrint = []
        for i in listaNome:
            objeto = str(i) + "  "
            listaNomePrint.append(objeto)
        print('listaNomePrint music21 nome:        ', listaNomePrint)
        listaNomePrint.clear()

        # print pitchesNumbers
        listaAlturasPrint = []
        for i in listaAlturas:
            if i == 'P':
                objeto = str(i) + "  "
            else:
                objeto = str(i) + " "
            listaAlturasPrint.append(objeto)
        print('listaAlturasPrint music21 nome:     ', listaAlturasPrint)
        listaAlturasPrint.clear()

        contador = 0
        listaOitavaPrint = []
        for i in listaOitava:
            objeto = str(i) + "  "
            listaOitavaPrint.append(objeto)
        print("listaOitavaPrint music21 nome:      ", listaOitavaPrint)
        listaOitavaPrint.clear()

        listaDuracaoPrint = []
        for i in listaDuracao:
            if i == 'P':
                objeto = str(i) + "  "
            else:
                objeto = str(i)
            listaDuracaoPrint.append(objeto)
        print('listaDuracaoPrint music21 nome:     ', listaDuracaoPrint)
        listaDuracaoPrint.clear()

        listaCompassoPrint = []
        for i in listaCompasso:
            objeto = str(i) + "  "
            listaCompassoPrint.append(objeto)
        print('listaCompassoPrint music21 nome:    ', listaCompassoPrint)
        listaCompassoPrint.clear()

        print('listaFormulaCompassoPrint:          ', listaFormulaCompasso)

        listaBeatPrint = []
        for i in listaBeat:
            objeto = str(i)
            listaBeatPrint.append(objeto)
        print('listaBeatPrint music21 nome:        ', listaBeatPrint)
        listaBeatPrint.clear()

        # beats escolhidos para harmonizar_dados
        listaBeatHarmonizarPrint = []
        for i in listaBeatHarmonizar:
            objeto = str(i) + "  "
            listaBeatHarmonizarPrint.append(objeto)
        print('listaBeatHarmonizarPrint music21:   ', listaBeatHarmonizarPrint)
        listaBeatHarmonizarPrint.clear()