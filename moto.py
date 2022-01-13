from engin_motorise import EnginMotorise
from moteur import Moteur


class Moto(EnginMotorise):
   
    def __init__(self, marque, moteur: Moteur):
        super().__init__(marque, moteur)

    def faire_wheling(self):
        return "on fait du wheling"