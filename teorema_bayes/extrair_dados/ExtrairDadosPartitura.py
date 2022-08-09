from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from teorema_bayes.extrair_dados.PitchNumber2 import PitchNumber2
from music21 import note, corpus


class ExtrairDadosPartitura:
    global listaNome, listaOitava,listaDuracao,listaBeat,listaCompasso,listaSimbolos,listaObjeto,listaAlturas
    listaNome = []
    listaOitava = []
    listaDuracao = []
    listaBeat = []
    listaCompasso = []
    listaSimbolos = []
    listaObjeto = []
    listaAlturas = []
    def extrair(self):
        ip = InserirPartitura()
        filePath = ip.get_path()
        partitura = corpus.parse(filePath)

        pn = PitchNumber2()
        contador = 0

        # extraindo notas da partitura e colocando em arrays
        for n in partitura.flat.notesAndRests:
            beat = n.beat                           # beat
            compasso = n.measureNumber              # compasso
            objeto = n                              # objeto music21
            contador = contador
            if type(n) is note.Note:                # se nota
                nome = n.pitch.name                 # nome nota
                oitava = n.pitch.octave             # oitava
                duracao = n.duration.quarterLength  # duração
                altura = pn.obtendo_pitches(n)
            if type(n) is note.Rest:                # se pausa
                nome = "P"
                duracao = n.duration.quarterLength
                oitava = "P"
                altura = "P"
            listaNome.append(nome)
            listaOitava.append(oitava)
            listaDuracao.append(duracao)
            listaBeat.append(beat)
            listaCompasso.append(compasso)
            listaObjeto.append(objeto)
            listaAlturas.append(altura)
            listaSimbolos.append(contador)
            contador += 1

    def getNome(self):
        return listaNome

    def getOitava(self):
        return listaOitava

    def getDuracao(self):
        return listaDuracao

    def getBeat(self):
        return listaBeat

    def getCompasso(self):
        return listaCompasso

    def getSimbolos(self):
        return listaSimbolos

    def getObjeto(self):
        return listaObjeto

    def getAlturas(self):
        return listaAlturas