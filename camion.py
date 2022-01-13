from voiture import Voiture
from moteur import Moteur


class Camion(Voiture):
    def __init__(self, marque, moteur: Moteur):
        super().__init__(marque, moteur)


def attacher_remorque(self):
    return "camion attacher"


def detacher_remorque(self):
    return "Camion detacher"
