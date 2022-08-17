class HarmoniaObtida2:
    def setContador(self, numero):
        global contador
        contador = numero

    def getContador(self):
        return contador

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