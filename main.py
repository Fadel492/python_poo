
from conducteur import Conducteur
from garage import Garage
from moteur_essence import MoteurEssence
from moto import Moto
from voiture import Voiture
from moteur_electrique import MoteurElectrique
ma_moteur=MoteurElectrique("150")
ma_voiture=Voiture("Tesla",ma_moteur)
mon_moteur = MoteurEssence(500)
ma_moto = Moto("Honda", mon_moteur)
mon_garage=Garage()
mon_garage.ajouter_engin(ma_voiture)
mon_garage.ajouter_engin(ma_moto)
mon_garage.presenter_garage_complet()

conducteur = Conducteur(25, "thomas", mon_garage)


conducteur.faire_un_tour()
