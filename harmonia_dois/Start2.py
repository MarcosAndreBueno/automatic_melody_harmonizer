from harmonia_dois.HarmonizarMelodia2 import HarmonizarMelodia2
from harmonia_dois.ObterLocaisHarmonizacao2 import ObterLocaisHarmonizacao2
from harmonia_dois.FormulaCompasso2 import FormulaCompasso2
from harmonia_dois.PitchNumber2 import PitchNumber2
from harmonia_dois.TrabalhandoGaps2 import TrabalhandoGaps2
from harmonia_dois.Print2 import Print2
from harmonia_dois.ReescreverMelodia2 import ReescreverMelodia2
from music21 import stream, note, meter


class Start2:
    def startProgram2(self, partitura):

        # ====================Transpor para Dó Maior====================
        # código
        # código

        # ====================Extraindo valores partitura====================
        print('_'*10,'Etapa 1.Copiando todos dados importantes da partitura...')

        # extraindo notas da partitura e colocando em um array
        contador = 0
        listaNome = []
        listaOitava = []
        listaDuracao = []
        listaBeat = []
        listaCompasso = []
        listaSimbolos = []
        listaObjeto = []
        listaAlturas = []
        pn = PitchNumber2()
        for n in partitura.flat.notesAndRests:
            beat = n.beat                             # beat
            listaBeat.append(beat)
            compasso = n.measureNumber                # compasso
            listaCompasso.append(compasso)
            objeto = n                                # objeto music21
            listaObjeto.append(objeto)
            contador = contador
            listaSimbolos.append(contador)
            if type(n) is note.Note:
                notaAtual = n.pitch.name              # nome nota
                listaNome.append(notaAtual)
                notaAtual = n.pitch.octave            # oitava
                listaOitava.append(notaAtual)
                notaAtual = n.duration.quarterLength  # duração
                listaDuracao.append(notaAtual)
                listaAlturas = pn.obtendo_pitches(listaAlturas, 1, n)
            if type(n) is note.Rest:
                notaAtual = "P"
                listaNome.append(notaAtual)
                listaOitava.append(notaAtual)
                notaAtual = n.duration.quarterLength
                listaDuracao.append(notaAtual)
                listaAlturas = pn.obtendo_pitches(listaAlturas, 0, n)
            contador += 1

        # ====================Fórmula Compasso====================
        fc = FormulaCompasso2()
        listaFormulaCompasso = fc.get_formula_compasso2(partitura)

        # ====================Obtendo harmonia====================
        olh = ObterLocaisHarmonizacao2()
        listaBeatHarmonizar = olh.possiveis_locais(listaFormulaCompasso,listaBeat, listaNome)

        # ====================Printando====================
        Print2().print_partitura_original2(partitura, listaObjeto, listaSimbolos, listaNome,
                                           listaOitava, listaDuracao,listaBeat, listaCompasso,
                                           listaFormulaCompasso, listaAlturas, listaBeatHarmonizar)

        # ====================Transpor para tonalidade original====================
        # código
        # código

        # ====================Reescrevendo Melodia====================
        rc = ReescreverMelodia2()
        s1 = rc.melodia_original2(listaAlturas, listaOitava, listaDuracao, listaFormulaCompasso)

        # ====================Reescrevendo Harmonia====================
        hm = HarmonizarMelodia2()
        s2 = hm.harmonizando2(listaNome, listaAlturas, listaBeatHarmonizar, listaDuracao,
                              listaFormulaCompasso, listaCompasso)

        # ====================Preenchendo Gaps====================
        tg = TrabalhandoGaps2()
        s2 = tg.preenchendo_gaps(s2, listaDuracao)

        # ====================RESULTADO====================
        w = stream.Score(id='mainScore')      # Comando para criar partitura com 2 claves.
        w.insert(0, s1)                       # clave em sol com notas originais
        w.insert(0, s2)                       # clave em sol com notas harmonizadas
        w.show()