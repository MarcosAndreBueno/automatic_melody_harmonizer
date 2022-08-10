from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura
from teorema_bayes.extrair_dados.PitchNumber2 import PitchNumber2
from music21 import note, corpus, key


class ExtrairDadosPartitura:
    global listaNome, listaOitava,listaDuracao,listaBeat,listaCompasso,\
        listaSimbolos,listaObjeto,listaAlturas, listaKeySign, listaOffSetKeySign
    listaNome = []
    listaOitava = []
    listaDuracao = []
    listaBeat = []
    listaCompasso = []
    listaSimbolos = []
    listaObjeto = []
    listaAlturas = []
    listaKeySign = []
    listaOffSetKeySign = []
    def extrair(self):
        ip = InserirPartitura()
        filePath = ip.get_path()
        partitura = corpus.parse(filePath)

        pn = PitchNumber2()
        contador = 0

        # extraindo notas da partitura e colocando em arrays
        for n in partitura.flat:
            contador = contador
            if type(n) is note.Note:                # se nota
                beat = n.beat  # beat
                compasso = n.measureNumber  # compasso
                nome = n.pitch.name                 # nome nota
                oitava = n.pitch.octave             # oitava
                duracao = n.duration.quarterLength  # duração
                altura = pn.obtendo_pitches(n)
                objeto = n  # objeto music21
                self.setNotesAndRests(nome,oitava,duracao,beat,compasso,altura, objeto)
            elif type(n) is note.Rest:                # se pausa
                nome = "P"
                oitava = "P"
                duracao = n.duration.quarterLength
                beat = n.beat  # beat
                compasso = n.measureNumber  # compasso
                altura = "P"
                objeto = n  # objeto music21
                self.setNotesAndRests(nome,oitava,duracao,beat,compasso,altura, objeto)
            elif type(n) is key.KeySignature:
                keySign = n
                offKeySign = n.offset
                listaKeySign.append(keySign)
                listaOffSetKeySign.append(offKeySign)

            listaSimbolos.append(contador)
            contador += 1

    def setNotesAndRests(self,nome,oitava,duracao,beat,compasso,altura, objeto):
        listaNome.append(nome)
        listaOitava.append(oitava)
        listaDuracao.append(duracao)
        listaBeat.append(beat)
        listaCompasso.append(compasso)
        listaAlturas.append(altura)
        listaObjeto.append(objeto)

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

    def getKeySignature(self):
        return listaKeySign

    def getOffSetKeySignature(self):
        return listaOffSetKeySign