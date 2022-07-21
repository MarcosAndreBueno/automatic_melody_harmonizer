import time

from teorema_bayes.DestruirLoading import DestruirLoading
from teorema_bayes.harmonizar_dados.HarmonizarMelodia2 import HarmonizarMelodia2
from teorema_bayes.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.extrair_dados.PitchNumber2 import PitchNumber2
from teorema_bayes.harmonizar_dados.TrabalhandoGaps2 import TrabalhandoGaps2
from teorema_bayes.extrair_dados.Print2 import Print2
from teorema_bayes.escrever.ReescreverMelodia2 import ReescreverMelodia2
from music21 import stream, note


class Start2:
    def startProgram2(self, partitura):
        start = time.time() # cronometrar processamento

        # ====================Definir Escala====================

        # ====================Extraindo valores partitura====================
        print('_'*10,'Etapa 1.Copiando todos dados importantes da partitura...')

        # extraindo notas da partitura e colocando em arrays
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
            if type(n) is note.Note:    # se nota
                notaAtual = n.pitch.name              # nome nota
                listaNome.append(notaAtual)
                notaAtual = n.pitch.octave            # oitava
                listaOitava.append(notaAtual)
                notaAtual = n.duration.quarterLength  # duração
                listaDuracao.append(notaAtual)
                listaAlturas = pn.obtendo_pitches(listaAlturas, 1, n)
            if type(n) is note.Rest:    # se pausa
                notaAtual = "P"
                listaNome.append(notaAtual)                             # lista nome recebe P
                listaOitava.append(notaAtual)                           # lista oitava recebe P
                notaAtual = n.duration.quarterLength
                listaDuracao.append(notaAtual)                          # lista duração recebe duração
                listaAlturas = pn.obtendo_pitches(listaAlturas, 0, n)   # lista alturas recebe P
            contador += 1

        # ====================Fórmula Compasso====================
        fc = FormulaCompasso2()
        listaFormulaCompasso = fc.get_formula_compasso2(partitura)

        # ====================Obtendo harmonia====================
        olh = ObterBeatsHarmonizacao2()
        listaBeatHarmonizar = olh.beats_escolhidos(listaFormulaCompasso,listaBeat, listaNome)

        # ====================Printando====================
        Print2().print_partitura_original2(partitura, listaObjeto, listaSimbolos, listaNome,
                                           listaOitava, listaDuracao,listaBeat, listaCompasso,
                                           listaFormulaCompasso, listaAlturas, listaBeatHarmonizar)

        # ====================Reescrevendo Melodia====================
        rc = ReescreverMelodia2()
        s1 = rc.melodia_original2(listaAlturas, listaOitava, listaDuracao, listaFormulaCompasso)

        # ====================Reescrevendo Harmonia====================
        hm = HarmonizarMelodia2()
        s2 = hm.harmonizando2(listaNome, listaAlturas, listaBeatHarmonizar, listaDuracao,
                              listaFormulaCompasso, listaCompasso, listaObjeto)

        # ====================Preenchendo Gaps====================
        tg = TrabalhandoGaps2()
        s2 = tg.preenchendo_gaps(s2, listaDuracao)

        # ====================Criar partitura====================
        # inserir streams na partitura
        w = stream.Score(id='mainScore')      # Comando para criar partitura com 2 claves.
        w.insert(0, s1)                       # clave em sol com notas originais
        w.insert(0, s2)                       # clave em sol com notas harmonizadas

        # ====================Abrir partitura após 5 segundos de loading====================
        # destruir janela loading
        dl = DestruirLoading()
        dl.destruir(start)

        # abrir partitura no music21
        w.show()