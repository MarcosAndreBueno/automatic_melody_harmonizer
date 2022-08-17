from teorema_bayes.extrair_dados.ExtrairDadosPartitura import ExtrairDadosPartitura
from teorema_bayes.extrair_dados.beat.BeatsHarmonizarObtidos2 import BeatsHarmonizarObtidos2
from teorema_bayes.extrair_dados.Tonalidade.Escala2 import Escala2

edp = ExtrairDadosPartitura()
listaNome = edp.getNome()
listaBeat = edp.getBeat()
bho = BeatsHarmonizarObtidos2()
listaBeatHarmonizar = bho.get()

def validar_beat_ternario(contador):
    beat = listaBeat[contador]
    beat = str(beat)
    edp = ExtrairDadosPartitura()
    nomeLista = edp.getNome()
    nome = nomeLista[contador]
    ec = Escala2()
    degrau = ec.get_degrau_from_harmonizar(contador)

    if beat == "1.0" and nome != 'P' and degrau != None: # ignorar pausas e acidentes ocorrentes
        listaBeatHarmonizar.append(1)  # beat aceito para harmonizar_dados
    else:
        listaBeatHarmonizar.append(0)  # beat não aceito para harmonizar_dados

    return listaBeatHarmonizar
