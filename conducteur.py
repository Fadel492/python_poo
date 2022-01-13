import random
from camion import Camion
from engin_motorise import EnginMotorise
from garage import Garage
from moto import Moto
from person import Person
from voiture import Voiture


class Conducteur(Person):
    def __init__(self, age, nom, garage: Garage):
        super().__init__(age, nom)

        self._garage = garage

    def presenter_garage(self):
        print(f"{self._garage.presenter_garage_complet()}")

    def conduire(self, engin: EnginMotorise):
        print(engin.accelerer())
        print(engin.freiner())
        if (type(engin) is Voiture):
            print(engin.reculer())
        if (type(engin) is Camion):
            print(engin.attacher_remorque())
            print(engin.detacher_remorque())
        if (type(engin) is Moto):
            print(engin.faire_wheling())

    def faire_un_tour(self):
        rnd = random.randint(0,len(self._garage._liste_engin)-1)
        vehicule = self._garage._liste_engin[rnd]
        self.conduire(vehicule)