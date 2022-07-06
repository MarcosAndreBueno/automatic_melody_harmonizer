from harmonia_dois.SortearHarmonia2 import SortearHarmonia2
from music21 import note


class ObterHarmonias2:
    def obter_harmonias(self, nomeNota, altura, oitava):
        # As funções poderiam ser If's, mas deixaria o método HarmonizarMelodia2 menos visual.
        if nomeNota == "C":  # se a nota for Dó quais serão as possíveis harmonias?
            sh = SortearHarmonia2()                              # pedindo para sortear números
            sorteio = sh.sortear(1,2)                            # pedindo para trazer a oitava da harmonia_um
            if sorteio == 1:
                altura = altura+oitava                           # se valor sorteado = 1, nota = 60+(-12) = Dó3
            else:
                altura = altura+9+oitava                         # se valor sorteado = 2, nota = 60+(-12) = Sol3
            return altura

        if nomeNota == "D":  # se a nota for Ré quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+9+oitava                        # +9 resulta na 6 maior de ré (Ré natural)
            return altura

        if nomeNota == "E":  # se a nota for Mi quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+8+oitava                        # +8 resulta na 6 menor de mi (Dó natural)
            return altura

        if nomeNota == "F":  # se a nota for Fá quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+9+oitava                        # +9 resulta na 6 maior de fá (Ré natural)
            return altura

        if nomeNota == "G":  # se a nota for Sol quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+9+oitava                        # +9 resulta na 6 maior de sol (Mi natural)
            return altura

        if nomeNota == "A":  # se a nota for Lá quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+8+oitava                        # +8 resulta na 6 menor de lá (Fá natural)
            return altura

        if nomeNota == "B":  # se a nota for Si quais serão as possíveis harmonias?
            sh = SortearHarmonia2()
            sorteio = sh.sortear(1,2)
            if sorteio == 1:
                altura = altura+oitava
            else:
                altura = altura+8+oitava                        # +8 resulta na 6 menor de si (Sol natural)
            return altura

        else:
            return "acidente ocorrente"

    # encontra a última nota a ser harmonizada
    def posicao_ultimo_acorde(self, listaNome, listaBeatHarmonizar):
        tamanhoL = len(listaNome)
        for x in listaNome[::-1]:
            tamanhoL -= 1
            nomeNota = listaNome[tamanhoL]
            beatHarmonizar = listaBeatHarmonizar[tamanhoL]
            if nomeNota != "P" and beatHarmonizar == 1:
                ultimoAcorde = tamanhoL
                return ultimoAcorde
        return -1   # caso não haja nota alguma, apenas pausas

    # completa com Dó maior a última nota
    def obter_ultimo_acorde(self, altura, oitava):
        n1 = note.Note(altura)
        nomeNota = n1.pitch.name
        if nomeNota == "C" or "E" or "G":
            altura = altura+oitava                           # se valor sorteado = 1, nota = 60+(-12) = Dó3
        else:
            self.obter_harmonias(nomeNota, altura, oitava)
        return altura