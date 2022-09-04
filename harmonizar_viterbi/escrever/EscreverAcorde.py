from harmonizar_viterbi.escrever.EscreverArmaduraClave import EscreverArmaduraClave
from harmonizar_viterbi.escrever.EscreverFormulaCompasso import EscreverFormulaCompasso
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
from harmonizar_viterbi.harmonizar_dados.CompletarAcorde2 import CompletarAcorde2
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from harmonizar_viterbi.harmonizar_dados.ObterDuracao2 import ObterDuracao2
from music21 import note, chord, meter, stream


class EscreverAcorde:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        fc = FormulaCompasso2()
        bho = BeatsHarmonizarObtidos2()
        ho = HarmoniaObtida2()
        ca = CompletarAcorde2()

        self.listaNome = edp.getNome()
        self.listaAlturas = edp.getAlturas()
        self.listaDuracao = edp.getDuracao()
        self.listaCompasso = edp.getCompasso()
        self.listaObjeto = edp.getObjeto()
        self.listaBeatHarmonizar = bho.get_beat_harm()
        self.listaFormulaCompasso = fc.get_fc()
        self.listaAcorde = ca.get_lista_acorde()
        self.contador = ho.getContador()
        self.objeto = edp.getObjeto(self.contador)
        self.s2 = ho.getStreamHarmonia()

    def escrevendo_acorde(self):
        od = ObterDuracao2()
        od.duracao_harmonia()
        duracao = od.get()

        # escrever formula de compasso da posição atual
        efc = EscreverFormulaCompasso()
        efc.escrever_f_c_harmonia()

        # escrever armadura de clave da posição atual
        eac = EscreverArmaduraClave()
        eac.escrever_a_c_harmonia()

        # formando notas do acorde
        nota1 = self.listaAcorde[0]
        nota2 = self.listaAcorde[1]
        nota3 = self.listaAcorde[2]
        n1 = note.Note(pitch=nota1,
                       quarterLength=duracao)  # criando notas com base nos valores retirados das listas.
        n2 = note.Note(pitch=nota2,
                       quarterLength=duracao)  # criando acordes com base nos valores retirados das listas.
        n3 = note.Note(pitch=nota3,
                       quarterLength=duracao)  # criando acordes com base nos valores retirados das listas
        c1 = chord.Chord([n1, n2, n3])

        # nota objeto music21 usaremos o offset da melodia harmonizada como index para o acorde.
        notaAtualOffSet = self.objeto
        notaAtualOffSet = notaAtualOffSet.offset
        self.s2.insert(notaAtualOffSet, c1)


        ho = HarmoniaObtida2()
        ho.setStreamHarmonia(self.s2)
