from harmonia_dois.Start2 import Start2 as st2
from interface_janela.CriandoJanela import CriandoJanela

print("INICIALIZANDO...")

def main():

    # iniciar com interface
    CriandoJanela().iniciando_janela1()


    # partitura = corpus.parse('testeA', 'Teste_Melodia_7')
    # st2().startProgram2(partitura)
    # #note.Note().pitchChanged()

if __name__ == "__main__":
    main()