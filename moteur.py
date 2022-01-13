class Moteur(object):
    _puissance: int = 0

    def __init__(self, puissance) -> None:
        self._puissance = puissance

    @property
    def puissance(self):
        return self._puissance

    @puissance.setter
    def puissance(self, value):
        self.puissance = value

    def augmenter_tour(self):
        return f" le tour du moteur augmente avec une puissance de {self.puissance}"
