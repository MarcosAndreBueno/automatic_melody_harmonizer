import time
from random import randint

from harmonia_dois.PitchNumber2 import PitchNumber2
from harmonia_dois.Start2 import Start2
from interface_janela.CriandoJanela import CriandoJanela
from music21 import corpus, meter, pitch, note, stream, clef



def main():
    print("INICIALIZANDO...")

    # iniciar com interface
    CriandoJanela().iniciando_janela1()

    # iniciar sem interface
    # partitura = corpus.parse('testeA', 'Teste_Melodia_6')
    # Start2().startProgram2(partitura)


if __name__ == '__main__':
    main()