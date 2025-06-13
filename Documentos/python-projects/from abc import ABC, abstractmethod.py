from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class  Cachorro(Animal):
    def fazer_som(self):
        print("Cachorro:  au au!")

class Gato(Animal):
    def fazer_som(self):
        print("Gato: Miau!")        
class Vaca(Animal):
    def fazer_som(self):
        print("Vaca: Muuu!") 

fazenda = [Cachorro(), Gato(), Vaca(), Gato()]                   

for animal in fazenda:
    animal.fazer_som()