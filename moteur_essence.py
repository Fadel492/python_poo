from moteur_thermique import MoteurThermique


class MoteurEssence(MoteurThermique):
    def __init__(self, puissance):
        super().__init__(puissance)

    def decrire(self):
        return "moteur d'essence"

    def augmenter_tour(self):
        return (super().augmenter_tour() + "VRROUMMMM")
