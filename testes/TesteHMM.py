from hmm_viterbi.Viterbi import Viterbi
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2


def inserirTomC():
    Tonalidade2().set_tom('A')
def extrairDadosPartitura():
    edp = ExtrairDadosPartitura()
    edp.extrair()
def extrairFormulaCompasso():
    fc = FormulaCompasso2()
    fc.extrair()
def extrairBeatsHarmonizacao():
    extrairFormulaCompasso()
    inserirTomC()
    ObterBeatsHarmonizacao2().obter_beats()
    edp = ExtrairDadosPartitura()
    bho = BeatsHarmonizarObtidos2()
    nomeLista = edp.getNome()
    beatHarm = bho.get()
    print("Tonalidade inserida: Dó Maior")
    print(nomeLista)
    for x in range(0, len(nomeLista)):
        if x == 0: print("[",end='')
        print("'"+str(beatHarm[x]),end="'")
        if x == len(nomeLista)-1: print("]",end="\n")
        else:
            print(end=', ')

def testeViterbi():
    extrairDadosPartitura()
    extrairBeatsHarmonizacao()
    Viterbi().interface_viterbi()
