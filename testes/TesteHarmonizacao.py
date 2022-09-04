from tkinter import Tk

from hmm_viterbi.Viterbi import Viterbi
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from janelas_interativas.botoes_menu.botoes_start.TelaTonalidade import TelaTonalidade
from music21 import stream, corpus, key
from harmonizar_viterbi.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from harmonizar_viterbi.InterfaceHarmonizacao import InterfaceHarmonizacao
from harmonizar_viterbi.escrever.ReescreverMelodia2 import ReescreverMelodia2
from harmonizar_viterbi.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from harmonizar_viterbi.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from harmonizar_viterbi.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from harmonizar_viterbi.extrair_dados.compasso.PrimeiroCompasso import PrimeiroCompasso
from harmonizar_viterbi.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from harmonizar_viterbi.harmonizar_dados.HarmonizarMelodia2 import HarmonizarMelodia2
from harmonizar_viterbi.harmonizar_dados.TrabalhandoGaps2 import TrabalhandoGaps2
from testes.Print2 import Print2
from harmonizar_viterbi.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2

ip = InserirPartitura()
ip.set_path()

def inserirTomC():
    tonalidade = ""
    while tonalidade != 'C' and tonalidade != 'D' and tonalidade != 'E' and tonalidade != 'F' \
        and tonalidade != 'G' and tonalidade != 'A' and tonalidade != 'B':
        tonalidade = input("Inserir tonalidade: ex: 'C', 'D', 'E', 'F', 'G', 'A' 'B': \n"
                           "(todos serão considerados tonalidades maiores)\n").upper()
        Tonalidade2().set_tom(tonalidade)

def inserirTonalidade():
    root = Tk()
    tl = TelaTonalidade()
    tl.inserir(root)

def extrairDadosPartitura():
    edp = ExtrairDadosPartitura()
    edp.extrair()
def extrairFormulaCompasso():
    fc = FormulaCompasso2()
    fc.set_fc()
def extrairBeatsHarmonizacao():
    extrairFormulaCompasso()
    ObterBeatsHarmonizacao2().obter_beats()
def reescreverMelodia():
    ho = HarmoniaObtida2()
    s1 = stream.Stream()
    ho.setStreamMelodia(s1)
    ReescreverMelodia2().melodia_original2()
def escreverHarmonia():
    ho = HarmoniaObtida2()
    s2 = stream.Stream()
    ho.setStreamHarmonia(s2)
    HarmonizarMelodia2().harmonizando2()
# def haveraGaps():
#     tg = TrabalhandoGaps2()
#     tg.havera_gaps()
#     print(tg.get())
def incomplete_compass():
    pc = PrimeiroCompasso()
    pc.set_compasso_status()

def mostrarPartituraMelodia():
    ho = HarmoniaObtida2()
    s1 = ho.getStreamMelodia()
    s1.show('t')
    teclado = ''
    while teclado != "Y" or teclado != "N":
        teclado = input("Abrir no musescore? Y or N\n").upper()
        if teclado == 'Y':
            s1.show()
        else:
            pass

def mostrarPartituraHarmmonizada():
    ho = HarmoniaObtida2()
    s1 = ho.getStreamMelodia()
    s2 = ho.getStreamHarmonia()
    w = stream.Score(id='mainScore')  # Comando para criar partitura com 2 claves.
    w.insert(0, s1)  # clave em sol com notas originais
    w.insert(0, s2)  # clave em sol com notas harmonizadas
    w.show('t')
    teclado = ''
    while input != "Y" or input != "N":
        teclado = input("Abrir no musescore? Y or N\n").upper()
        if teclado == 'Y':
            w.show()
        elif teclado == 'N':
            break

def testeExtrairDadosPartitura():
    extrairDadosPartitura()
    edp = ExtrairDadosPartitura()
    print(edp.getObjeto(),'\n', edp.getSimbolos(),'\n', edp.getNome(),'\n', edp.getAlturas(),'\n',
          edp.getOitava(),'\n', edp.getDuracao(),'\n', edp.getCompasso(),'\n', edp.getBeat())

def testeFormulaCompasso2():
    extrairFormulaCompasso()
    print(FormulaCompasso2().get_fc())

def testeObterBeatsHarmonizacao2():
    extrairDadosPartitura()
    inserirTomC()
    incomplete_compass()
    extrairBeatsHarmonizacao()
    edp = ExtrairDadosPartitura()
    bho = BeatsHarmonizarObtidos2()
    nomeLista = edp.getNome()
    beatHarm = bho.get_beat_harm()
    print(nomeLista)
    for x in range(0, len(nomeLista)):
        if x == 0: print("[",end='')
        print("'"+str(beatHarm[x]),end="'")
        if x == len(nomeLista)-1: print("]",end="\n")
        else:
            print(end=', ')

def testePrint2():
    inserirTomC()
    extrairDadosPartitura()
    incomplete_compass()
    extrairBeatsHarmonizacao()
    Print2().print_partitura_original2()
    Viterbi().interface_viterbi()

def testeReescreverMelodia2():
    extrairDadosPartitura()
    extrairFormulaCompasso()
    reescreverMelodia()
    ho = HarmoniaObtida2()
    mostrarPartituraMelodia()

# def testeTrabalhandoGaps2():
#     extrairDadosPartitura()
#     incomplete_compass()
#     extrairBeatsHarmonizacao()

def testeHarmonizarMelodia2():
    inserirTomC()
    extrairDadosPartitura()
    incomplete_compass()
    extrairBeatsHarmonizacao()
    calcularViterbi()
    reescreverMelodia()
    escreverHarmonia()
    mostrarPartituraHarmmonizada()

def testePrimeiroCompasso():
    extrairDadosPartitura()
    incomplete_compass()
    pc = PrimeiroCompasso()
    print("música começa com compasso anacruse/acéfalo:",pc.get_compasso_status())
    if pc.get_compasso_status() == True:
        print("Se True, quantas notas o compasso tem?", pc.get_compass_tamanho())

def testeInterfaceHarmonizacao():
    inserirTomC()
    InterfaceHarmonizacao().startProgram2()

def calcularViterbi():
    vt = Viterbi()
    vt.interface_viterbi()