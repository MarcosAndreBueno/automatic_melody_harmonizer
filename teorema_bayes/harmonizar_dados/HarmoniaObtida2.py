class HarmoniaObtida2:
    def setAltura(self,nome):
        global altura
        altura = nome

    def getAltura(self):
        return altura

    def setFormulaCompasso(self, nome):
        global compasso
        compasso = nome

    def getFormulaCompasso(self):
        return compasso

    def setContador(self, numero):
        global contador
        contador = numero

    def getContador(self):
        return contador

    def setNomeNota(self, nome):
        global nomeNota
        nomeNota = nome

    def getNomeNota(self):
        return nomeNota

    def setObjeto(self, nome):
        global objeto
        objeto = nome

    def getObjeto(self):
        return objeto

    def setStreamMelodia(self,valores):
        global streamM
        streamM = valores

    def getStreamMelodia(self):
        return streamM

    def setStreamHarmonia(self,valores):
        global streamH
        streamH = valores

    def getStreamHarmonia(self):
        return streamH