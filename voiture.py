from engin_motorise import EnginMotorise
from moteur import Moteur


class Voiture(EnginMotorise):
    
    def __init__(self, marque, moteur: Moteur):
        super().__init__(marque, moteur)

    def reculer(self):
        return f"la Voiture de marque {self.marque} recule"