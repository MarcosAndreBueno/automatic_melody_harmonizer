import time

from teorema_bayes.DestruirLoading import DestruirLoading
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.harmonizar_dados.HarmonizarMelodia2 import HarmonizarMelodia2
from teorema_bayes.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from teorema_bayes.escrever.ReescreverMelodia2 import ReescreverMelodia2
from music21 import stream


class InterfaceHarmonizacao:
    def startProgram2(self):
        print('_'*10,'Etapa 1.Copiando todos dados importantes da partitura...')

        controle = time.time()
        start = time.time() # cronometrar processamento

        # ====================Extraindo Valores da Partitura====================
        epd = ExtrairDadosPartitura()
        epd.extrair()

        # ====================Fórmula de Compasso====================
        fc = FormulaCompasso2()
        fc.extrair()

        # ====================Reescrevendo Melodia====================
        print("Tempo decorrido:",controle - time.time())
        print('_'*10,'Etapa 2.Reescrevendo a melodia de base...')
        s1 = stream.Stream()
        HarmoniaObtida2().setStreamMelodia(s1)
        rc = ReescreverMelodia2()
        rc.melodia_original2()

        # ====================Obtendo Harmonia====================
        print("Tempo decorrido:",controle - time.time())
        print('_'*10,'Etapa 3.Gerando harmonia !...')
        olh = ObterBeatsHarmonizacao2()
        olh.obter_beats()

        # ====================Reescrevendo Harmonia====================
        s2 = stream.Stream()
        HarmoniaObtida2().setStreamHarmonia(s2)
        hm = HarmonizarMelodia2()
        hm.harmonizando2()

        # ====================Criar partitura====================
        print("Tempo decorrido:",controle - time.time())
        print('_'*10,'Etapa 4.Abrindo resultado no music21...')
        ho = HarmoniaObtida2()
        s1 = ho.getStreamMelodia()
        s2 = ho.getStreamHarmonia()

        # inserir streams na partitura
        w = stream.Score(id='mainScore')      # Comando para criar partitura com 2 claves.
        w.insert(0, s1)                       # clave em sol com notas originais
        w.insert(0, s2)                       # clave em sol com notas harmonizadas

        # ====================Abrir partitura após 5 segundos de loading====================
        print("Tempo decorrido:",controle - time.time())
        # destruir janela loading
        dl = DestruirLoading()
        dl.destruir(start)
        # abrir partitura no music21
        w.show()