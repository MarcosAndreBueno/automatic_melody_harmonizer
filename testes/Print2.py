# este método serve apenas para facilitar a leitura dos dados (da melodia) usados para harmonização.

from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from music21 import corpus, converter
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2


class Print2:
    def print_partitura_original2(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        bho = BeatsHarmonizarObtidos2()

        # get path partitura
        ip = InserirPartitura()
        filePath = ip.get_path()
        partitura = converter.parse(filePath)

        # get listas
        listaObjeto = edp.getObjeto()
        listaSimbolos = edp.getSimbolos()
        listaNome = edp.getNome()
        listaAlturas = edp.getAlturas()
        listaOitava = edp.getOitava()
        listaDuracao = edp.getDuracao()
        listaCompasso = edp.getCompasso()
        listaFormulaCompasso = fc.get_fc()
        listaBeat = edp.getBeat()
        listaBeatHarmonizar = bho.get_beat_harm()

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