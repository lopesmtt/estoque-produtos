class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("Som generico do animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")     

class Gato(Animal):
    def fazer_som(self):
        print("Miau!") 

dog = Cachorro("Rex", 5)
cat = Gato("Mimi", 3)

print(f"{dog.nome} diz:", end="")
dog.fazer_som()

print(f"{cat.nome} diz:", end=" ")
cat.fazer_som()