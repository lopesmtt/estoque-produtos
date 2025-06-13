class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} faz um som generico") 

class Cachorro(Animal):
    def falar(self):
        print(f"{self.nome} faz Au au!") 

class Gato(Animal):
    def falar(self):
        print(f"{self.nome} faz Miau!") 

dog = Cachorro("Rex")
cat = Gato("Mimi") 

dog.falar()
cat.falar()

