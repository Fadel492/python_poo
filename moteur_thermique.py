from moteur import Moteur


class MoteurThermique(Moteur):
    def __init__(self, puissance):
        super().__init__(puissance)

    def faire_plein(self):
       return 'le moteur thermique est plein' 