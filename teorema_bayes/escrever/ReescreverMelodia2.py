from teorema_bayes.extrair_dados.compasso.ContadorFormulaCompasso2 import ContadorFormulaCompasso2
from music21 import stream, meter, note


class ReescreverMelodia2:
    def melodia_original2(self, listaAlturas, listaOitava, listaDuracao, listaFormulaCompasso):
        contador = 0
        s1 = stream.Stream()  # lista dos elementos que serão inseridos na partitura.
        cfc = ContadorFormulaCompasso2()
        # tamanho listaformula
        tamanhoLista = len(listaFormulaCompasso)
        # while contador < que tamanhoLista
        while contador < tamanhoLista:
            # quantidade = chamar contadorformula
            quantidade = cfc.repeticoes_compasso(listaFormulaCompasso, tamanhoLista, contador)
            # formula atual
            formulaAtual = listaFormulaCompasso[contador]
            # set formula atual na stream
            ts = meter.TimeSignature(formulaAtual)
            s1.append(ts)
            # iterando fórmulas de compassos
            final = contador+quantidade
            for x in range(contador, final):
                notaAtual = listaAlturas[x]
                if notaAtual == "P":
                    d1 = listaDuracao[x]
                    n1 = note.Rest(quarterLength=d1)
                else:
                    pitch = listaAlturas[x]
                    nota = note.Note(pitch).pitch.name
                    oitava = str(listaOitava[x])
                    nota = nota+oitava
                    d1 = listaDuracao[x]
                    n1 = note.Note(nameWithOctave=nota, quarterLength=d1)
                s1.append(n1)
            contador+=quantidade
        return s1