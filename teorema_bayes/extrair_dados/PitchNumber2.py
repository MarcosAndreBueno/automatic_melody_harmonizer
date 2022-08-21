from music21 import pitch


class PitchNumber2:
    def get_pitch_from_name(self,name):
        name = name.pitches                 # ex: object music21.pitch.Pitch C4
        name = str(name)
        start = 21
        stop = len(name) - 3
        name = name[start:stop]             # ex: object music21.pitch.Pitch C4 -> n = C4
        altura = int(pitch.Pitch(name).ps)  # ex: C4 -> p = 60
        return altura
