from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura


class PrimeiroCompasso:
    def __init__(self):
        edp = ExtrairDadosPartitura()
        self.firstNote = edp.getNome(0)
        self.compasso = edp.getCompasso()

    def set_compasso_status(self):
        global incomplete_compass, incomplete_tamanho
        incomplete_tamanho = 0

        if self.firstNote == 'P':
            incomplete_compass = True
            x = 0
            while (self.compasso[x] == 1):
                incomplete_tamanho += 1
                x+=1
        else:
            incomplete_compass = False

    def get_compasso_status(self):
        return incomplete_compass

    def get_compass_tamanho(self):
        return incomplete_tamanho