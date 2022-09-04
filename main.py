print("INICIALIZANDO...")

def main():
    # =====================================================================
        # _____Testes da tela interativa
    # import testes.TesteInterface as ti
    # ti.testeTelaAbertura()
    # ti.testeTelaPrincipal()
    # ti.testeTelaTonalidade()
    # ti.testeTelaLoading()
    # ti.testeInterfaceInterativa()

    # =====================================================================
    # _____Testes harmonização:
    # import testes.TesteHarmonizacao as th
    # th.testeExtrairDadosPartitura()
    # th.testeFormulaCompasso2()
    # th.testeObterBeatsHarmonizacao2()
    # th.testePrint2()
    # th.testeReescreverMelodia2()
    # th.testeHarmonizarMelodia2()
    # th.testePrimeiroCompasso()
    # th.testeHarmonizarMelodia2()
    # th.testeInterfaceHarmonizacao()

    # =====================================================================
    # ___Teste HMM Viterbi
    # import testes.TesteHMM as thmm
    # thmm.testeViterbi()

    # =====================================================================
    # ___Testar programa completo:
    from janelas_interativas.InterfaceInterativa import InterfaceInterativa as ii
    ii().iniciar()

if __name__ == "__main__":
    main()