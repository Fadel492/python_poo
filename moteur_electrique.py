from moteur import Moteur


class MoteurElectrique(Moteur):
    def __init__(self, puissance):
        super().__init__(puissance)


    def recharger(self):
        return 'le moteur est en train de recharger'

    def augmenter_tour(self):
        return (super().augmenter_tour() +"silencieusement")