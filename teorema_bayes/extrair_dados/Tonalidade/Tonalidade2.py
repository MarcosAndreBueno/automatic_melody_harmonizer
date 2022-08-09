from music21 import note, scale


class Tonalidade2:
    def set_tom(self,nome):
        global tom
        tom=nome

    def get_tom(self):
        return tom
