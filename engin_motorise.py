import re
from moteur import Moteur


class EnginMotorise(object):
    _marque: str = ''
    _moteur: Moteur

    def __init__(self, marque, moteur: Moteur):
        self._marque = marque
        self._moteur = moteur

    @property
    def marque(self):
        return self._marque

    @property
    def moteur(self):
        return self._moteur

    @moteur.setter
    def moteur(self, value):
        self._moteur = value

    def accelerer(self):
        return (f"le conducteur accelere {self.moteur.augmenter_tour()}")

    def freiner(self):
        return 'je freine'

    def decrire(self):
        return f"on un vehicule de marque {self.marque} et de puissance{self.moteur.puissance}"