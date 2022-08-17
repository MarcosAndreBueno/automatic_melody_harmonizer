import testes.TesteInterface as ti
import testes.TesteHarmonizacao as th
import testes.TesteHMM as thmm
from janelas_interativas.botoes_menu.botao_inserir.InserirPartitura import InserirPartitura

print("INICIALIZANDO...")

def main():
    ip = InserirPartitura()
    ip.set_path()
    # ti.testeTelaAbertura()
    # ti.testeTelaPrincipal()
    # ti.testeTelaTonalidade()
    # ti.testeTelaLoading()
    # ti.testeInterfaceInterativa()
    # th.testeExtrairDadosPartitura()
    # th.testeFormulaCompasso2()
    # th.testeObterBeatsHarmonizacao2()
    # th.testePrint2()
    # th.testeReescreverMelodia2()
    # th.testeHarmonizarMelodia2()
    # th.testeTrabalhandoGaps2()
    # th.testeHarmonizarMelodia2()
    # th.testeInterfaceHarmonizacao()
    thmm.testeViterbi()

# mudar degraus da harmonização com base na tonalidade inserida
# botoes
# resolver viterbi
# aplicar viterbi
# sortear com base no viterbi

if __name__ == "__main__":
    main()
