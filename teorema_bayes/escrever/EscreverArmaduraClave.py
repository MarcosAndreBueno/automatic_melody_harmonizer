from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.harmonizar_dados.HarmoniaObtida2 import HarmoniaObtida2


class EscreverArmaduraClave:
    def __init__(self):
        self.ho = HarmoniaObtida2()
        edp = ExtrairDadosPartitura()
        self.keySignature = edp.getKeySignature()
        self.getOffSetKeySignature = edp.getOffSetKeySignature()

    def escrever_a_c(self, stream):
        global count # controle contador da lista keySignature

        # após primeiro compasso
        if self.ho.getContador() > 0:
            if count < len(self.keySignature):
                keyAtualOffSet = self.getOffSetKeySignature[count]
                keySign = self.keySignature[count]
                keySignAnt = self.keySignature[count-1]
                if keySign != keySignAnt:                   # reescrever a armadura de clave, caso mude
                    stream.insert(keyAtualOffSet, keySign)  # inserir A.C. na posição correta usando offset
                    count += 1

        # primeiro compasso: escrever armadura de clave
        else:
            keySign = self.keySignature[0]
            stream.insert(0, keySign)                       # inserir na posição inicial, compasso 0
            count = 1

    def escrever_a_c_harmonia(self):
        s2 = self.ho.getStreamHarmonia()
        self.escrever_a_c(s2)

    def escrever_a_c_melodia(self):
        s1 = self.ho.getStreamMelodia()
        self.escrever_a_c(s1)