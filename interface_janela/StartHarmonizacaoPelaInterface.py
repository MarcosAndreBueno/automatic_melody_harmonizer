from harmonia_dois.Start2 import Start2
from interface_janela.InserirPartitura import InserirPartitura
from music21 import converter


class StartHarmonizacaoPelaInterface:
    def start_harmonizacao_interface(self, valor):
        # obtendo diretório partitura em string
        caminho_diretorio = InserirPartitura()

        # None pois não passaremos o primeiro atributo janela # também poderia ser escrito assim:
        # filePath = caminho_diretorio.inserindo(number = valor)
        # number se refere ao nome da variável na função que está sendo chamada
        # valor se refere ao valor que será passado para essa posição especifica
        filePath = caminho_diretorio.inserindo(None, valor)

        # parse na partitura
        partitura = converter.parse(filePath)

        # começando harmonização
        inicio = Start2()
        inicio.startProgram2(partitura)