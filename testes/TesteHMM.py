from hmm_viterbi.Viterbi import Viterbi
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from teorema_bayes.extrair_dados.compasso.PrimeiroCompasso import PrimeiroCompasso
from testes import TesteHarmonizacao

from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2
th = TesteHarmonizacao

def calcularViterbi():
    vt = Viterbi()
    vt.interface_viterbi()

def incomplete_compass():
    pc = PrimeiroCompasso()
    pc.set_compasso_status()

def print_viterbi():
    edp = ExtrairDadosPartitura()
    incomplete_compass()
    bho = BeatsHarmonizarObtidos2()
    vt = Viterbi()
    nomeLista = edp.getNome()
    beatHarm = bho.get_beat_harm()
    hid_states = vt.get_hidden_state()
    observated = vt.get_observated_states()
    compasso = edp.getCompasso()
    print("Tonalidade inserida: Dó Maior")
    print('melodia:   ', end=' ')
    for i in nomeLista: print(i, end=', ')
    print('\ncompasso:  ', end=' ')
    for i in compasso: print(i,end=', ')
    print('\nbeatHarm:  ', end=' ')
    for i in beatHarm: print(i, end=', ')
    print('\nobservated:', end=' ')
    for i in observated: print(i,end=', ')
    print('\nhid_states:', end=' ')
    for i in hid_states: print(i,end=', ')

def testeViterbi():
    th.extrairDadosPartitura()
    incomplete_compass()
    th.extrairBeatsHarmonizacao()
    calcularViterbi()
    print_viterbi()

