from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2

edp = ExtrairDadosPartitura()
listaNome = edp.getNome()
listaBeat = edp.getBeat()
bho = BeatsHarmonizarObtidos2()
listaBeatHarmonizar = bho.get()

def validar_beat_binario(contador):
    beat = listaBeat[contador]
    beat = str(beat)

    if beat == "1.0" or beat == "3.0":
        listaBeatHarmonizar.append(1)  # beat aceito para harmonizar_dados
    else:
        listaBeatHarmonizar.append(0)  # beat não aceito para harmonizar_dados

    return listaBeatHarmonizar
