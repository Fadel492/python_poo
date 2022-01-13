from engin_motorise import EnginMotorise


class Garage(object):
    _liste_engin: list[EnginMotorise]= []
    
    def __init__(self) -> None:
        pass

    def ajouter_engin(self,engin):
        self._liste_engin.append(engin)
    
    def retirer_engin(self,engin):
        self._liste_engin.remove(engin)

    def presenter_garage_complet(self):
        for engin in self._liste_engin:
            print(engin.decrire())
    