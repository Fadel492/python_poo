class Person(object):
    _age:int=0
    _nom:str=''
    
    def __init__(self,age,nom):
        self._nom=nom
        self._age=age

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age=value
    @property
    def nom(self):
        return self._nom
    
    def se_presenter(self):
        print(f"{self._nom}->{self.age}")
        