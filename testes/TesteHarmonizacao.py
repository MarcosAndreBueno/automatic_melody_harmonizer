from tkinter import Tk

from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from janelas_interativas.botoes_menu.botoes_start.TelaTonalidade import TelaTonalidade
from music21 import stream
from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.InterfaceHarmonizacao import InterfaceHarmonizacao
from teorema_bayes.escrever.ReescreverMelodia2 import ReescreverMelodia2
from teorema_bayes.extrair_dados.Tonalidade.Tonalidade2 import Tonalidade2
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.beat.ObterBeatsHarmonizacao2 import ObterBeatsHarmonizacao2
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2
from teorema_bayes.harmonizar_dados.HarmonizarMelodia2 import HarmonizarMelodia2
from teorema_bayes.harmonizar_dados.TrabalhandoGaps2 import TrabalhandoGaps2
from testes.Print2 import Print2
from teorema_bayes.extrair_dados.compasso.FormulaCompasso2 import FormulaCompasso2

ip = InserirPartitura()
ip.set_path()

def inserirTomC():
    Tonalidade2().set_tom('C')

def inserirTonalidade():
    root = Tk()
    tl = TelaTonalidade()
    tl.inserir(root)

def extrairDadosPartitura():
    edp = ExtrairDadosPartitura()
    edp.extrair()
def extrairFormulaCompasso():
    fc = FormulaCompasso2()
    fc.extrair()
def extrairBeatsHarmonizacao():
    extrairDadosPartitura()
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
def haveraGaps():
    tg = TrabalhandoGaps2()
    tg.havera_gaps()
    print(tg.get())
def mostrarPartitura():
    ho = HarmoniaObtida2()
    s1 = ho.getStreamMelodia()
    s2 = ho.getStreamHarmonia()
    w = stream.Score(id='mainScore')  # Comando para criar partitura com 2 claves.
    w.insert(0, s1)  # clave em sol com notas originais
    w.insert(0, s2)  # clave em sol com notas harmonizadas
    w.show()

def testeExtrairDadosPartitura():
    extrairDadosPartitura()
    edp = ExtrairDadosPartitura()
    print(edp.getObjeto(),'\n', edp.getSimbolos(),'\n', edp.getNome(),'\n', edp.getAlturas(),'\n',
          edp.getOitava(),'\n', edp.getDuracao(),'\n', edp.getCompasso(),'\n', edp.getBeat())

def testeFormulaCompasso2():
    extrairFormulaCompasso()
    print(FormulaCompasso2().get())

def testeObterBeatsHarmonizacao2():
    extrairBeatsHarmonizacao()
    print(BeatsHarmonizarObtidos2().get())

def testePrint2():
    inserirTonalidade()
    extrairDadosPartitura()
    extrairFormulaCompasso()
    extrairBeatsHarmonizacao()
    Print2().print_partitura_original2()

def testeReescreverMelodia2():
    extrairDadosPartitura()
    extrairFormulaCompasso()
    reescreverMelodia()
    ho = HarmoniaObtida2()
    s1 = ho.getStreamMelodia()
    s1.show('t')

def testeHarmonizarMelodia2():
    inserirTomC()
    extrairDadosPartitura()
    extrairFormulaCompasso()
    HarmonizarMelodia2()

def testeTrabalhandoGaps2():
    extrairDadosPartitura()
    extrairBeatsHarmonizacao()

def testeHarmonizarMelodia2():
    inserirTomC()
    extrairBeatsHarmonizacao()
    reescreverMelodia()
    haveraGaps()
    escreverHarmonia()
    mostrarPartitura()

def testeInterfaceHarmonizacao():
    inserirTomC()
    InterfaceHarmonizacao().startProgram2()
