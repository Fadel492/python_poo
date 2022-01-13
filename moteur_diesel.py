from moteur_thermique import MoteurThermique


class MoteurDiesel(MoteurThermique):
    def __init__(self, puissance):
        super().__init__(puissance)

    def decrire(self):
        return "un moteur Diesel"

    def augmenter_tour(self):
        return (super().augmenter_tour() + "VROUMMMM POLUANT")
